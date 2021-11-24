from pytube import YouTube
from pytube.cli import on_progress
from moviepy.editor import *
import os

def download_music():
    link = input('Insira o link: ')
    yt = YouTube(link, on_progress_callback = on_progress)

    print('Título = ', yt.title)
    print('Baixando...')

    ys = yt.streams.get_highest_resolution()
    out_file_mp4 = ys.download("./musicas").split('./')[-1]
    out_file_mp3 = out_file_mp4.replace('.mp4', '.mp3')

    with VideoFileClip(out_file_mp4) as video:
        video.audio.write_audiofile(out_file_mp3)

    os.remove(out_file_mp4)
