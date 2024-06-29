from pytube import Playlist

def get_video_links(playlist_url):
    playlist = Playlist(playlist_url)
    links = [video.watch_url for video in playlist.videos]
    return links

def get_video_titles(playlist_url):
    playlist = Playlist(playlist_url)
    titles = [video.title for video in playlist.videos]
    return titles

# Beispiel: URL deiner YouTube-Playlist
playlist_url = 'https://www.youtube.com/watch?v=y2p7U_M5jZU&list=PL63prxjFVV-eGLv4yv94c6VlUHNP3z3Fw'
links = get_video_links(playlist_url)
titles = get_video_titles(playlist_url)

# Ausgabe der Links
for link in links:
    print(link)

# Ausgabe der Titel
for title in titles:
    print(title)
