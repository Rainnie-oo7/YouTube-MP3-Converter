from pytube import YouTube
from pydub import AudioSegment
import os

def download_audio(youtube_url, filename):
    # Video herunterladen
    yt = YouTube(youtube_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    output_file = audio_stream.download(filename='audio.mp4')

    # Audiospur in MP3 konvertieren
    audio = AudioSegment.from_file(output_file)
    mp3_filename = f"{filename}.mp3"
    audio.export(mp3_filename, format='mp3')

    # Temporäre Datei löschen
    os.remove(output_file)

    print(f"Audiospur gespeichert als {mp3_filename}")

# Eingaben vom Benutzer
youtube_url = input("Gib die YouTube-URL ein: ")
filename = input("Gib den gewünschten Dateinamen ein (ohne Erweiterung): ")

# Funktion aufrufen
download_audio(youtube_url, filename)
