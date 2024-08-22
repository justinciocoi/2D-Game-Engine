import pygame
from backend.utils import load_animation
from backend.settings import *
from backend.character import *
from backend.player import *
from backend.enemy import *
from backend.assetImports import *
from backend.collision import *

def draw_screen(screen, entities, delta_time, platform):
    screen.blit(background, (0,0))
    for entity in entities:
        entity.update(delta_time)
        entity.draw(screen)
    pygame.draw.rect(screen, PLATFORM_COLOR, platform)
    pygame.display.update()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player_animations = load_animation(player_spritesheets)
    enemy_animations = load_animation(enemy_spritesheets)
    platform = pygame.Rect(0, SCREEN_HEIGHT - GROUND_OFFSET, SCREEN_WIDTH,  GROUND_OFFSET)

    # Animation loop example
    clock = pygame.time.Clock()
    current_animation = "idle"
    animation_index = 0
    running = True

    player = Player(100,SCREEN_HEIGHT - (SPRITE_HEIGHT + GROUND_OFFSET),player_animations)
    enemy = Enemy(800,SCREEN_HEIGHT - (SPRITE_HEIGHT + GROUND_OFFSET), enemy_animations, player)
    entities = [player, enemy]

    while running:
        delta_time = clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            player.handle_event(event)
        

        draw_screen(screen, entities, delta_time, platform)

    pygame.quit()

if __name__ == "__main__":
    main()