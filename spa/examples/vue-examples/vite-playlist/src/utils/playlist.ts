import type { Song } from '../types'

export function songMatchesSearch(song: Song, search: string): boolean {
  const songName = song.name.toLowerCase()
  const artistName = song.artist.toLowerCase()
  return songName.includes(search) || artistName.includes(search)
}

export function compareSongsByName(songA: Song, songB: Song): number {
  return songA.name.localeCompare(songB.name)
}
