import pygame
import random
from backend.settings import *

class Character:
    def __init__(self, x, y, animations):
        self.x = x
        self.y = y
        self.y_velocity = 0
        self.animations = animations
        self.current_animation = "idle"
        self.animation_index = 0
        self.image = self.animations[self.current_animation][self.animation_index]
        self.animation_speed = 0.1
        self.animation_timer = 0
        self.facing_right = True
        self.is_attacking = False
        self.is_dash = False
        self.dash_cooldown = False  # To prevent dash from retriggering
        self.is_jump = False
        self.is_doubleJump = False
        self.hurtbox = pygame.Rect(self.x + PLAYER_HURTBOX_X_OFFSET_RIGHT, self.y + PLAYER_HURTBOX_Y_OFFSET, PLAYER_HURTBOX_WIDTH, PLAYER_HURTBOX_HEIGHT)
        self.attack_hitbox = pygame.Surface((SPRITE_WIDTH // 3, SPRITE_HEIGHT // 9))
        self.current_vel = VEL

    def set_animation(self, animation_name):
        if self.current_animation != animation_name:
            self.current_animation = animation_name
            self.animation_index = 0

    def update(self, delta_time):
        self.animation_timer += delta_time
        if self.animation_timer >= self.animation_speed:
            self.animation_index += 1

            # Check if the animation has reached the end
            if self.animation_index >= len(self.animations[self.current_animation]):
                if self.is_attacking and self.current_animation == "l_attack":
                    # Reset attacking state after attack animation finishes
                    self.is_attacking = False
                elif self.is_dash and self.current_animation == "h_attack":
                    self.is_dash = False
                    self.dash_cooldown = False  # Allow dash to be triggered again

                self.animation_index = 0

            # Update the current image based on the animation and facing direction
            if self.facing_right:
                self.image = self.animations[self.current_animation][self.animation_index]
            else:
                self.image = pygame.transform.flip(self.animations[self.current_animation][self.animation_index], True, False)

            self.animation_timer = 0

            
        # Apply scaling
        self.image = pygame.transform.scale(self.image, (SPRITE_WIDTH, SPRITE_HEIGHT))

    def draw(self, screen):
        keys = pygame.key.get_pressed()
        # Draw hurtbox
        if keys[pygame.K_LSHIFT] and (keys[pygame.K_a] or keys[pygame.K_d]) and not self.is_jump:
            if self.facing_right:
                self.hurtbox.x -= HURTBOX_DASH_OFFSET
            else:
                self.hurtbox.x += HURTBOX_DASH_OFFSET
        
        # Draw character sprite
        screen.blit(self.image, (self.x, self.y))

        # Display attack hitbox during the attack animation
        """
        if self.current_animation == "l_attack" and self.animation_index == 4:
            # Display the hitbox only on a specific frame (e.g., frame 4)
            attack_hitbox_position = (self.x, self.y)
            if self.facing_right:
                attack_hitbox_position = (self.x + SPRITE_WIDTH // 1.5, self.y + SPRITE_HEIGHT // 1.6)  # Adjust for right-facing direction
            else:
                attack_hitbox_position = ((self.x - 5), self.y + SPRITE_HEIGHT // 1.6)   # Adjust for left-facing direction

            screen.blit(self.attack_hitbox, attack_hitbox_position)
        
        if self.current_animation == "h_attack" and self.animation_index == (1 or 2):
            attack_hitbox_position = (self.x, self.y)
            if self.facing_right:
                attack_hitbox_position = (self.x + SPRITE_WIDTH // 1.5, self.y + SPRITE_HEIGHT // 1.6)  # Adjust for right-facing direction
            else:
                attack_hitbox_position = ((self.x - 1), self.y + SPRITE_HEIGHT // 1.6)   # Adjust for left-facing direction

            screen.blit(self.attack_hitbox, attack_hitbox_position)"""











    