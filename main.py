import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/PixelType.ttf', 70)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# text_surf = test_font.render('O MEU JOGO', False, 'Black')

score_surf = test_font.render('SCORE', False, 'Black')
score_rect = score_surf.get_rect(center=(400, 50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # if event.type == pygame.MOUSEMOTION:
        #   print(event.pos) , outra função para mouse tracking
        # if player_rect.collidepoint(event.pos): print('collision')

        # todos os elementos aqui
        # update a tudo aqui

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    # screen.blit(text_surf, (300, 50))
    # pygame.draw.line(screen, 'Orange', (0, 0), (800, 400))
    pygame.draw.rect(screen, 'Gold', score_rect)
    pygame.draw.rect(screen, 'Gold', score_rect, 10)
    screen.blit(score_surf, score_rect)
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    player_rect.left += 1
    screen.blit(player_surf, player_rect)

    #  if player_rect.colliderect(snail_rect):
    #      print('collision')
    # mouse_pos = pygame.mouse.get_pos()  # buscar a posiçao do rato
    # if player_rect.collidepoint(mouse_pos):  # ponto de colisao com algo
    #   print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)
