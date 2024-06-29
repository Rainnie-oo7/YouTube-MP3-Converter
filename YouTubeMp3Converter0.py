from pytube import YouTube
from pydub import AudioSegment
import os

def download_audio(youtube_url, filename):
    yt = YouTube(youtube_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    output_file = audio_stream.download(filename='audio.mp4')

    audio = AudioSegment.from_file(output_file)
    mp3_filename = f"{filename}.mp3"
    audio.export(mp3_filename, format='mp3')

    os.remove(output_file)
    print(f"Audiospur gespeichert als {mp3_filename}")

# Listen mit URLs und Namen
youtube_links = [
    "https://youtube.com/watch?v=y2p7U_M5jZU",
    "https://youtu.be/gsr19Kdf3Lk?si=g1uLTFFWqLqvOXJt",
    "https://youtube.com/watch?v=-gGtnwQjC_4",
    "https://youtube.com/watch?v=qEfwTHcDlUA",
    "https://youtube.com/watch?v=g_RNAXa6Zdc",
    "https://youtube.com/watch?v=lbJJjnLnJc8",
    "https://youtube.com/watch?v=x8A_LekKcYI",
    "https://youtube.com/watch?v=D1WLjCwmI3E",
    "https://youtube.com/watch?v=bUJwfesg71M",
    "https://youtube.com/watch?v=UC4YG-RV7K4",
    "https://youtube.com/watch?v=4sgM5fLmOac",
    "https://youtube.com/watch?v=mYzYRyNxae8",
    "https://youtube.com/watch?v=MR3obtuAMpY",
    "https://youtube.com/watch?v=PHNK3OBsA-0",
    "https://youtube.com/watch?v=7O_Fd_wo1GI",
    "https://youtube.com/watch?v=ymqBhDhbOdw",
    "https://youtube.com/watch?v=aKhDzykCmzs"

]

file_names = [
    "Fantasy Background Music - Celtic Relaxation - Free Use",
    "Adventure Time Music - No Copyright/Free - Mediacharger",
    "RPG Fantasy Music - No Copyright Music - DnD",
    "Conan Background Music - Creative Commons",
    "Angelic Music Choir - Powerful Background Music",
    "Ye Olde Tavern Music - Fantasy - Mediacharger",
    "Fantasy Battle Music - Roleplaying Music - Creative Commons",
    "Epic Boss Music - Orchestral Gaming Music",
    "[No Copyright Music] - The Vampire Hunter - Gothic ( Castlevania )",
    "Black Wake - Pirate Ship Battle Music - Mediacharger",
    "Ye Old Tavern Music - Medieval Fantasy Background Music - No Copyright",
    "No Copyright Fantasy Music  - Creative Commons Eastern Music",
    "Epic Industrial Trailer Music - No Copyright Trailers",
    "No Copyright Medieval Music - Medieval Fantasy Music - Creative Commons",
    "Cinematic Music No Copyright | Emotional Fantasy Music",
    "Fantasy Instrumental | Medieval Sounds | No Copyright Music |",
    "Dramatic Emotional Orchestral Instrumental Music For Videos | Ominous/Uplifting Music"

]

# Durch die Listen iterieren und die Dateien benennen
for index, (url, name) in enumerate(zip(youtube_links, file_names), start=1):
    formatted_name = f"{index:02d} {name}"
    download_audio(url, formatted_name)
