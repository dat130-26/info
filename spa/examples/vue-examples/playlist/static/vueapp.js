window.addEventListener("DOMContentLoaded", function () {
  // Read the initial playlist JSON that Flask/Jinja embedded into the HTML.
  const initialPlaylistScript = document.getElementById("initial-playlist");
  let initialPlaylist = [];
  if (initialPlaylistScript) {
    initialPlaylist = JSON.parse(initialPlaylistScript.textContent);
  }

  // songMatchesSearch is a helper function for search
  function songMatchesSearch(song, search) {
    const songName = (song.name || "").toLowerCase();
    const artistName = (song.artist || "").toLowerCase();
    return songName.includes(search) || artistName.includes(search);
  }

  // compareSongsByName is a helper function for sorting songs by name.
  function compareSongsByName(songA, songB) {
    return songA.name.localeCompare(songB.name);
  }

  // createApp() creates one Vue application instance for #app.
  const app = Vue.createApp({
    // data() defines reactive state used by template and methods.
    data() {
      return {
        playlist: initialPlaylist,
        newSongName: "",
        newArtistName: "",
        searchTerm: ""
      };
    },
    computed: {
      // computed values update automatically when dependent state changes.
      filteredSongs() {
        const search = this.searchTerm.toLowerCase();
        return this.playlist.filter(function (song) {
          return songMatchesSearch(song, search);
        });
      }
    },
    methods: {
      // methods are called from v-on event bindings in the template.
      addSong() {
        const name = this.newSongName.trim();
        const artist = this.newArtistName.trim();
        if (!name) {
          return;
        }

        this.playlist.push({
          name: name,
          artist: artist || "Unknown"
        });
        this.newSongName = "";
        this.newArtistName = "";
      },
      deleteSong(song) {
        const index = this.playlist.indexOf(song);
        if (index > -1) {
          this.playlist.splice(index, 1);
        }
      },
      sortSongs() {
        this.playlist.sort(compareSongsByName);
      }
    }
  });

  // Change Vue text delimiters to [[ ]] to avoid collision with Jinja {{ }}.
  app.config.compilerOptions.delimiters = ["[[", "]]" ];
  app.mount("#app");
});
