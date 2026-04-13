<template>
  <div class="container mt-4">
    <h1>Movies</h1>
    <div class="row">
      <div class="col-md-4 mb-4" v-for="movie in movies" :key="movie.id">
        <div class="card h-100">
          <img 
            :src="movie.poster" 
            class="card-img-top" 
            :alt="movie.title"
            style="height: 400px; object-fit: cover;"
          />
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
            <p class="card-text">{{ movie.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);

function fetchMovies() {
  fetch('/api/v1/movies')
    .then((response) => response.json())
    .then((data) => {
      movies.value = data.movies;
    })
    .catch((error) => console.log(error));
}

onMounted(() => {
  fetchMovies();
});
</script> 