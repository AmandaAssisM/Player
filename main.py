import player
from time import sleep
from random import choice


def init():
    player.play_music()

    while True:
        while True:
            try:
                opcao = player.pegar_opcao_menu()
                player.verificar_opcao(opcao)
                
            except SystemExit:
                print('Saindo...')
                sleep(2)
                return
            except Exception as erro:
                print(erro)
                continue

init()
