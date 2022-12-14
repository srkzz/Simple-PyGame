import pygame
from sys import exit


def display_score():
    current_time = pygame.time.get_ticks() - tempo_inicio
    score_surf = test_font.render(f'SCORE: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/PixelType.ttf', 70)
game_active = True
tempo_inicio = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# text_surf = test_font.render('O MEU JOGO', False, 'Black')
restart_surf = test_font.render('SPACE para jogar outra vez!', False, 'White')
restart_rect = restart_surf.get_rect(center=(400, 200))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:  # qualquer butao do rato premido
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20  # diminuir a gravidade quando saltamos

            if event.type == pygame.KEYDOWN:  # seta para baixo premida
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20  # diminuir a gravidade quando saltamos
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                tempo_inicio = pygame.time.get_ticks()

        # if event.type == pygame.MOUSEMOTION:
        #   print(event.pos) , outra função para mouse tracking
        # if player_rect.collidepoint(event.pos): print('collision')

        # todos os elementos aqui
        # update a tudo aqui
    if game_active:  # jogo em si
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, 'Gold', score_rect)
        # pygame.draw.rect(screen, 'Gold', score_rect, 10)
        # screen.blit(score_surf, score_rect)
        display_score()

        # caracol
        snail_rect.x -= 4
        if snail_rect.right <= 0: snail_rect.left = 800
        screen.blit(snail_surf, snail_rect)

        # Jogador
        player_gravity += 1  # aumentar a gravidade
        player_rect.y += player_gravity  # relativo ao eixo
        if player_rect.bottom >= 300: player_rect.bottom = 300  # limites de terreno por causa do loop aumentar a gravidade
        screen.blit(player_surf, player_rect)

        #  if player_rect.colliderect(snail_rect):
        #      print('collision')
        # mouse_pos = pygame.mouse.get_pos()  # buscar a posiçao do rato
        # if player_rect.collidepoint(mouse_pos):  # ponto de colisao com algo
        #   print(pygame.mouse.get_pressed())

        # colisão
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:  # intro // menu
        screen.fill('Black')
        screen.blit(restart_surf, restart_rect)
        if snail_rect.colliderect(player_rect): snail_rect.left = 800

    pygame.display.update()
    clock.tick(60)
