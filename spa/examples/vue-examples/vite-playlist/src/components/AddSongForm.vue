<script setup lang="ts">
import { ref } from 'vue'
import type { Song } from '../types'

const emit = defineEmits<{
  'add-song': [song: Song]
}>()

const songName = ref('')
const artistName = ref('')

function submitSong(): void {
  const name = songName.value.trim()
  const artist = artistName.value.trim()

  if (!name) {
    return
  }

  emit('add-song', {
    name,
    artist,
  })

  songName.value = ''
  artistName.value = ''
}
</script>

<template>
  <form v-on:submit.prevent="submitSong" class="add-song-form">
    <input v-model="songName" type="text" size="40" placeholder="Song name" />
    <input v-model="artistName" type="text" size="30" placeholder="Artist name" />
    <input id="addButton" type="submit" value="Add Song" />
  </form>
</template>
