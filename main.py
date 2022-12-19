import pygame
from sys import exit
from random import randint


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - tempo_inicio
    score_surf = test_font.render(f'SCORE: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


def obst_movimento(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list: #todos os rectangulos dentro da lista ou seja os inimigos
            obstacle_rect.x -= 5 #determinar velocidade / objetos para a esquerda

            if obstacle_rect.bottom == 300:
                screen.blit(caracol_surf, obstacle_rect) # se for no chão é caracol
            else:
                screen.blit(mosca_surf, obstacle_rect) # no ceu é mosca
        # verificar se os obstaculos estao demasiado a esquerda para eliminar e não tornar o jogo lento, só copiamos
        # obstaculos apos essa condição verificada
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []

def colisoes(jogador, obstaculos):
    if obstaculos:
        for obstacle_rect in obstaculos:
            if jogador.colliderect(obstacle_rect):
                return False # qq colisão devolve Falso
    return True

def jogador_animacao():
    global jogador_surf, jogador_index

    if jogador_rect.bottom < 300:
        jogador_surf = jogador_salta #saltar se nao tiver no chão (300 coordenada)
        #salta
    else:                       #andar se tiver no chão
        jogador_index += 0.1
        if jogador_index >= len(jogador_anda):jogador_index = 0
        jogador_surf = jogador_anda[int(jogador_index)]

        #anda




pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/PixelType.ttf', 70)
game_active = False
tempo_inicio = 0
score = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# text_surf = test_font.render('O MEU JOGO', False, 'Black')

# Mensagem de Inicio / restart ao jogo
restart_surf = test_font.render('SPACE para JOGAR!', False, 'White')
restart_rect = restart_surf.get_rect(center=(400, 100))

# obstaculos
caracol_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
caracol_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
caracol_frames = [caracol_frame_1, caracol_frame_2]
caracol_frame_index = 0
caracol_surf = caracol_frames[caracol_frame_index]


mosca_frame_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
mosca_frame_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
mosca_frames = [mosca_frame_1, mosca_frame_2]
mosca_frame_index = 0
mosca_surf = mosca_frames[mosca_frame_index]


obstacle_rect_list = []

# jogador
jogador_anda_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
jogador_anda_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
jogador_anda = [jogador_anda_1, jogador_anda_2]
jogador_index = 0 # indicador da surf a usar , 1 andar ou 2 andar, só ha 1 salto logo nao precisamos para isso
jogador_salta = pygame.image.load('graphics/player/jump.png')
jogador_surf = jogador_anda[jogador_index]
jogador_rect = jogador_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

# Imagem de entrada
player_imagem = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_imagem = pygame.transform.rotozoom(player_imagem, 0, 2)
player_imagem_rect = player_imagem.get_rect(center=(400, 250))

# Temporizadores
obst_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obst_timer, 1500)  # qual o evento, a quantos milisegundos

caracol_animacao_tempo = pygame.USEREVENT + 2
pygame.time.set_timer(caracol_animacao_tempo, 500)

mosca_animacao_tempo = pygame.USEREVENT + 3
pygame.time.set_timer(mosca_animacao_tempo, 500)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:  # qualquer butao do rato premido
                if jogador_rect.collidepoint(event.pos) and jogador_rect.bottom >= 300:
                    player_gravity = -20  # diminuir a gravidade quando saltamos

            if event.type == pygame.KEYDOWN:  # seta para baixo premida
                if event.key == pygame.K_SPACE and jogador_rect.bottom >= 300:
                    player_gravity = -20  # diminuir a gravidade quando saltamos
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                tempo_inicio = int(pygame.time.get_ticks() / 1000)

        if game_active:
            if event.type == obst_timer:
                if randint(0, 2):
                    obstacle_rect_list.append(caracol_surf.get_rect(bottomright=(randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(mosca_surf.get_rect(center=(randint(900, 1100), 100)))

            if event.type == caracol_animacao_tempo:
                if caracol_frame_index == 0: caracol_frame_index = 1
                else: caracol_frame_index = 0
                caracol_surf = caracol_frames[caracol_frame_index]

            if event.type == mosca_animacao_tempo:
                if mosca_frame_index == 0: mosca_frame_index = 1
                else: mosca_frame_index = 0
                mosca_surf = mosca_frames[mosca_frame_index]




        # if event.type == pygame.MOUSEMOTION:
        #   print(event.pos) , outra função para mouse tracking
        # if jogador_rect.collidepoint(event.pos): print('collision')

        # todos os elementos aqui
        # update a tudo do jogo aqui
    if game_active:  # jogo em si
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, 'Gold', score_rect)
        # pygame.draw.rect(screen, 'Gold', score_rect, 10)
        # screen.blit(score_surf, score_rect)
        score = display_score()

        # caracol easy
        # snail_rect.x -= 4
        # if snail_rect.right <= 0: snail_rect.left = 800
        # screen.blit(caracol_surf, snail_rect)

        # Jogador
        player_gravity += 1  # aumentar a gravidade
        jogador_rect.y += player_gravity  # relativo ao eixo
        if jogador_rect.bottom >= 300: jogador_rect.bottom = 300  # limites de terreno por causa do loop aumentar a gravidade
        jogador_animacao()
        screen.blit(jogador_surf, jogador_rect)

        # movimento dos obstaculos
        obstacle_rect_list = obst_movimento(obstacle_rect_list)  # update continuo da lista

        # colisão

        game_active = colisoes(jogador_rect, obstacle_rect_list)

    else:  # intro // menu
        screen.fill('Black')
        screen.blit(player_imagem, player_imagem_rect)
        obstacle_rect_list.clear() # limpar todos os items da tela para resetar o jogo
        jogador_rect.midbottom = (80, 300)
        player_gravity = 0

        score_message = test_font.render(f'Os teus Pontos: {score}', False, 'White')
        score_message_rect = score_message.get_rect(center=(400, 370))
        screen.blit(restart_surf, restart_rect)
        if score == 0:
            screen.blit(restart_surf, restart_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)
