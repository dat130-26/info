<script setup lang="ts">
import type { Song } from '../types'

defineProps<{
  song: Song
}>()

const emit = defineEmits<{
  'delete-song': [song: Song]
}>()

function deleteSong(song: Song): void {
  emit('delete-song', song)
}
</script>

<template>
  <li class="song-item">
    <span>{{ song.name }} - {{ song.artist }}</span>
    <button class="delete" type="button" v-on:click="deleteSong(song)">Delete</button>
  </li>
</template>

<style scoped>
.song-item {
  position: relative;
  border-bottom: 1px solid #a9a9a9;
  padding: 10px;
  background-image: linear-gradient(#f9f9f9, #e3e3e3);
}

.song-item:last-child {
  border-bottom: none;
  border-bottom-right-radius: 5px;
  border-bottom-left-radius: 5px;
}

.song-item:first-child {
  border-top-right-radius: 5px;
  border-top-left-radius: 5px;
}

button.delete {
  position: absolute;
  right: 5px;
  top: 5px;
  border: 1px solid #888;
  border-radius: 4px;
  background: #fff;
  padding: 0.3rem 0.55rem;
  cursor: pointer;
}

button.delete:hover {
  background: #f3f3f3;
}
</style>
