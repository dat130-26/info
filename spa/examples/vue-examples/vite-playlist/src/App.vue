<script setup lang="ts">
import { computed, ref } from 'vue'
import AddSongForm from './components/AddSongForm.vue'
import SongListItem from './components/SongListItem.vue'
import type { Song } from './types'
import { compareSongsByName, songMatchesSearch } from './utils/playlist'

const initialPlaylist: Song[] = [
  { name: 'Test', artist: 'tester' },
  { name: 'Best song', artist: 'Bester' },
  { name: 'Another song', artist: 'Someone else' },
]

const playlist = ref<Song[]>([...initialPlaylist])
const searchTerm = ref('')

const filteredSongs = computed(function () {
  const search = searchTerm.value.toLowerCase()
  return playlist.value.filter(function (song) {
    return songMatchesSearch(song, search)
  })
})

function handleAddSong(song: Song): void {
  const name = song.name.trim()
  const artist = song.artist.trim()
  if (!name) {
    return
  }

  playlist.value.push({
    name,
    artist: artist || 'Unknown',
  })
}

function deleteSong(song: Song): void {
  const index = playlist.value.indexOf(song)
  if (index > -1) {
    playlist.value.splice(index, 1)
  }
}

function sortSongs(): void {
  playlist.value.sort(compareSongsByName)
}
</script>

<template>
  <main class="playlist-app">
    <h1>Playlist App Using Vue</h1>

    <AddSongForm v-on:add-song="handleAddSong" />
    <form v-on:submit.prevent class="sort-search-form">
      <input v-model="searchTerm" type="text" size="20" placeholder="search" />
      <input id="sortButton" type="button" value="Sort" v-on:click="sortSongs" />
    </form>

    <ul id="playlist">
      <SongListItem
        v-for="(song, index) in filteredSongs"
        v-bind:key="song.name + '-' + index"
        :song="song"
        v-on:delete-song="deleteSong"
      />
    </ul>
  </main>
</template>
