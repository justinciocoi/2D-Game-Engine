import pygame
from backend.settings import *

def split_sprite_into_frames(spritesheet, sprite_width = 128):
    sheet_width = spritesheet.get_width()
    number_of_frames = sheet_width // sprite_width
    frames = []
    for i in range(number_of_frames):
        frame = spritesheet.subsurface(
            pygame.Rect(i * sprite_width, 0, 128, 128)
        )
        frames.append(frame)
    return frames

def load_animation(spritesheets, sprite_width=128):
    animations = {}
    for animation_name, spritesheet in spritesheets.items():
        frames = split_sprite_into_frames(spritesheet, sprite_width)
        animations[animation_name] = frames
    return animations

