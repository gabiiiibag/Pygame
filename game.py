#integrantes: Cauê Shimmock, Gabriela Giolo.

import pygame
import random
pygame.init()
largura = 1385
altura = 800
tamanho = (largura, altura)
pygameDisplay = pygame.display
pygameDisplay.set_caption("Honey Capture")
gameDisplay = pygame.display.set_mode(tamanho)
gameIcon = pygame.image.load("assets/icone.webp")
pygameDisplay.set_icon(gameIcon)
bg = pygame.image.load("assets/fundo.jpg")


# Aqui Começa o jogo

vitoriaSound = pygame.mixer.Sound("assets/vitoria.mp3")
vitoriaSound.set_volume(0.2)
black = (0, 0, 0)
white = (255, 255, 255)
clock = pygame.time.Clock()
gameEvents = pygame.event
ursomorto = pygame.image.load("assets/URSOOO2.png")
corRosa = (255,20,147)

def vitoria(pontos):
    gameDisplay.blit(ursomorto,(0,0))
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(vitoriaSound)
    fonte = pygame.font.Font("freesansbold.ttf", 35)
    fonteContinue = pygame.font.Font("freesansbold.ttf", 35)
    texto = fonte.render("O urso já está satisfeito! eba! :) ", True, white)
    textoContinue = fonteContinue.render(
        "Press enter to restart...", True, white)
    gameDisplay.blit(textoContinue, (50, 200))
    gameDisplay.blit(texto, (50, 100))
    pygameDisplay.update()


def jogo():
    posicaoX = 0
    posicaoY = random.randrange(0, altura)
    direcao = True
    velocidade = 10
    posicaoXurso = 500
    posicaoYurso = 100
    movimentoXurso = 0
    movimentoYurso = 0
    pontos = 0
    mel = pygame.image.load("assets/mel.png")
    urso = pygame.image.load("assets/urso2.png")
    mel = pygame.transform.flip(mel, True, False)
    pygame.mixer.music.load("assets/musica2.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)

    alturaurso = 300
    larguraurso = 215
    alturamel = 89
    larguramel = 55
    dificuldade = 29

    urso = pygame.transform.scale(urso, (larguraurso, alturaurso))
    mel = pygame.transform.scale(mel, (larguramel, alturamel))
    jogando = True
    while True:
        # aqui é lido os eventos da tela
        for event in gameEvents.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    jogo()
                if event.key == pygame.K_LEFT:
                    movimentoXurso = - 10
                elif event.key == pygame.K_RIGHT:
                    movimentoXurso = 10
                elif event.key == pygame.K_UP:
                    movimentoYurso = -10
                elif event.key == pygame.K_DOWN:
                    movimentoYurso = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    movimentoXurso = 0
                    movimentoYurso = 0

        if jogando == True:
            # travando o movimento na tela
            posicaoXurso = posicaoXurso + movimentoXurso
            posicaoYurso = posicaoYurso + movimentoYurso
            if posicaoXurso < 0:
                posicaoXurso = 0
            elif posicaoXurso >= largura - larguraurso:
                posicaoXurso = largura - larguraurso

            if posicaoYurso < 0:
                posicaoYurso = 0
            elif posicaoYurso >= altura - alturaurso:
                posicaoYurso = altura - alturaurso

            # aqui termina a leitura de eventos
            # gameDisplay.fill(pink)
            gameDisplay.blit(bg, (0, 0))

            if direcao == True:
                if posicaoX < largura-150:
                    posicaoX = posicaoX + velocidade
                else:
                    direcao = False
                    posicaoY = random.randrange(0, altura)
                    mel = pygame.transform.flip(mel, True, False)
            else:
                if posicaoX >= 0:
                    posicaoX = posicaoX - velocidade
                else:
                    direcao = True
                    posicaoY = random.randrange(0, altura)
                    mel = pygame.transform.flip(mel, True, False)

            gameDisplay.blit(mel, (posicaoX, posicaoY))
            gameDisplay.blit(urso, (posicaoXurso, posicaoYurso))
            # pygame.draw.circle(
            #    gameDisplay, black, [posicaoX, posicaoY], 20, 0)
            fonte = pygame.font.Font("freesansbold.ttf", 20)
            texto = fonte.render("Gramas de Mel: "+str(pontos), True, corRosa)
            textoKg = fonte.render("o Urso precisa de 0,7 kg de mel para ganhar o jogo!", True, corRosa)
            gameDisplay.blit(textoKg,(20,40))
            gameDisplay.blit(texto, (20, 20))

            # análise de colisão (modelo 1)
            ursoRect = urso.get_rect()
            ursoRect.x = posicaoXurso
            ursoRect.y = posicaoYurso
            melRect = mel.get_rect()
            melRect.x = posicaoX
            melRect.y = posicaoY

            if ursoRect.colliderect(melRect):
                if pontos < 700:
                    pygame.mixer.Sound("assets/vitoria.mp3")
                    pontos = pontos + 1 
                else:
                    vitoria(pontos)
                    pygame.mixer.music.stop()
                    jogando = False
            
            # análise de colisão (modelo 2)

            '''pixelsYurso = list(
                range(posicaoYurso, posicaoYurso + alturaurso+1))
            pixelsXurso = list(
                range(posicaoXurso, posicaoXurso + larguraurso+1))

            pixelsYmel = list(range(posicaoY, posicaoY+alturamel+1))
            pixelsXmel = list(range(posicaoX, posicaoX+larguramel+1))'''
        

            # comparar e mostrar elementos iguais em duas listas
            # print(len(list(set(pixelsYmel) & set(pixelsYurso))))
            

            '''if len(list(set(pixelsYmel) & set(pixelsYurso))) > dificuldade:
                if len(list(set(pixelsXmel) & set(pixelsXurso))) > dificuldade:
                    jogando = False
                    vitoria(pontos)
                    '''

        pygameDisplay.update()
        clock.tick(60)


jogo()
