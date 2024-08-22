import pygame
from backend.settings import *

 # Initialize the animations for each character
player_spritesheets = {
    "idle": pygame.image.load("assets/samurai/Idle.png"),
    "walk": pygame.image.load("assets/samurai/Walk.png"),
    "jump": pygame.image.load("assets/samurai/Jump.png"),
    "run": pygame.image.load("assets/samurai/Run.png"),
    "l_attack": pygame.image.load("assets/samurai/Attack_1.png"),
    "l_attack_2": pygame.image.load("assets/samurai/Attack_2.png"),
    "h_attack": pygame.image.load("assets/samurai/Attack_3.png"),
    "hurt": pygame.image.load("assets/samurai/Hurt.png"),
    "death":  pygame.image.load("assets/samurai/Dead.png"),
}

enemy_spritesheets = {
    "idle": pygame.image.load("assets/shinobi/Idle.png"),
    "walk": pygame.image.load("assets/shinobi/Walk.png"),
    "jump": pygame.image.load("assets/shinobi/Jump.png"),
    "run": pygame.image.load("assets/shinobi/Run.png"),
    "l_attack": pygame.image.load("assets/shinobi/Attack_1.png"),
    "l_attack_2": pygame.image.load("assets/shinobi/Attack_2.png"),
    "h_attack": pygame.image.load("assets/shinobi/Attack_3.png"),
    "hurt": pygame.image.load("assets/shinobi/Hurt.png"),
    "death": pygame.image.load("assets/shinobi/Hurt.png")
}

background = pygame.transform.scale(pygame.image.load("assets/city.webp"), (R_1080P))