from pygame import mixer
from time import sleep
from download import *
import os

musicas = [f'./musicas/{music}' for music in os.listdir('./musicas')]
music_file = musicas[0]

mixer.init()

def atualizar_lista_musicas():
    global musicas
    musicas = [f'./musicas/{music}' for music in os.listdir('./musicas')]

def play_music():
    mixer.music.load(music_file)
    mixer.music.play()

def pause():
    mixer.music.pause()

def unpause():
    mixer.music.unpause()

def stop():
    mixer.music.stop()

def proxima():
    global music_file

    actual_music_index = musicas.index(music_file)
    last_song_index = musicas.index(musicas[-1])
    
    if actual_music_index != last_song_index:
        next_music_index = actual_music_index + 1
    else:
        next_music_index = 0
    
    music_file = musicas[next_music_index]
    mixer.music.load(musicas[next_music_index])
    mixer.music.play()

def anterior():
    global music_file

    actual_music_index = musicas.index(music_file)
    last_song_index = musicas.index(musicas[-1])

    if actual_music_index == 0:
        previous_music_index = 0
    elif actual_music_index != last_song_index:
        previous_music_index = actual_music_index - 1
    else:
        previous_music_index = 0

    music_file = musicas[previous_music_index]
    mixer.music.load(musicas[previous_music_index])
    mixer.music.play()

def pegar_opcao_menu():
    player_menu()
    opcao = input('Opção: ')
    return opcao

def player_menu():
    print('''
    [1] Pause
    [2] Retomar
    [3] Próxima
    [4] Anterior
    [5] Parar
    [6] Baixar uma música
     ''')

def verificar_opcao(opcao):
    opcoes_validas = ['1', '2', '3', '4', '5', '6']
    
    if opcao not in opcoes_validas:
        raise Exception('Insira uma opção válida.')
    
    if opcao == opcoes_validas[0]:
        pause()

    if opcao == opcoes_validas[1]:
        unpause()

    if opcao == opcoes_validas[2]:
        proxima()

    if opcao == opcoes_validas[3]:
        anterior()

    if opcao == opcoes_validas[4]:
        sleep(2)
        stop()
        raise SystemExit

    if opcao == opcoes_validas[5]:
        print('Baixar música do YouTube.')
        download_music()
        atualizar_lista_musicas()
