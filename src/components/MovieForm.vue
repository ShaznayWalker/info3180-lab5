<template>
  <form id="movieForm" @submit.prevent="saveMovie" enctype="multipart/form-data">
    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input type="text" name="title" class="form-control" />
    </div>
    
    <div class="form-group mb-3">
      <label for="description" class="form-label">Description</label>
      <textarea name="description" class="form-control" rows="5"></textarea>
    </div>
    
    <div class="form-group mb-3">
      <label for="poster" class="form-label">Photo Upload</label>
      <input type="file" name="poster" class="form-control" />
    </div>
    
    <button type="submit" class="btn btn-primary">Submit</button>
    
    <!-- Success Message -->
    <div v-if="successMessage" class="alert alert-success mt-3">
      {{ successMessage }}
    </div>
    
    <!-- Error Messages -->
    <div v-if="errorMessages.length" class="alert alert-danger mt-3">
      <div v-for="error in errorMessages" :key="error">{{ error }}</div>
    </div>
  </form>
</template>

<script setup>
import { ref, onMounted } from "vue";

let csrf_token = ref("");
let successMessage = ref("");
let errorMessages = ref([]);

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      csrf_token.value = data.csrf_token;
    })
    .catch((error) => console.log(error));
}

function saveMovie() {
  successMessage.value = "";
  errorMessages.value = [];
  
  let movieForm = document.getElementById('movieForm');
  let form_data = new FormData(movieForm);
  
  fetch("/api/v1/movies", {
    method: 'POST',
    body: form_data,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  })
  .then((response) => {
    return response.json().then(data => ({ status: response.status, body: data }));
  })
  .then(({ status, body }) => {
    if (status === 201) {
      successMessage.value = body.message;
      document.getElementById('movieForm').reset();
    } else if (status === 400 && body.errors) {
      errorMessages.value = body.errors;
    }
  })
  .catch((error) => {
    console.log(error);
    errorMessages.value = ['An error occurred. Please try again.'];
  });
}

onMounted(() => {
  getCsrfToken();
});
</script> 