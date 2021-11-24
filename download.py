from pytube import YouTube
from pytube.cli import on_progress

import os


link = input('Insira o link: ')
yt = YouTube(link, on_progress_callback = on_progress)

print('Título = ', yt.title)
print('Baixando...')

ys = yt.streams.get_audio_only()
out_file = ys.download("./musicas")
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
