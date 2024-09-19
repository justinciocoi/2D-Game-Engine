import pygame
from backend.settings import *
from backend.character import *

class Player(Character):
    def __init__(self, x, y, animations):
        super().__init__(x, y, animations)
        self.is_grounded = True  # Indicates if the player is on the ground
        self.health = 100
        self.attack_power = 5
        self.current_grav = GRAV
        

    def handle_input(self):
        keys = pygame.key.get_pressed()

        # Adjust velocity based on the state
        if self.is_attacking and not self.is_jump:
            self.current_vel = VEL // 2  # Move slower when attacking
        elif self.is_dash:
            self.current_vel = VEL * 4  # Move faster when dashing
            if self.is_jump and not keys[pygame.K_k]:
                self.current_vel = VEL
        else:
            self.current_vel = VEL
        if keys[pygame.K_LSHIFT] and not self.is_attacking and not self.is_dash:
            self.current_vel = VEL * 2

        # Handle horizontal movement
        if keys[pygame.K_a] and self.x >= 0:
            self.x -= self.current_vel
            self.hurtbox.x -= self.current_vel
            if not self.is_attacking and not self.is_dash and self.is_grounded:
                self.set_animation("run" if keys[pygame.K_LSHIFT] else "walk")
            self.facing_right = False
        elif keys[pygame.K_d] and self.x <= SCREEN_WIDTH - SPRITE_WIDTH:
            self.x += self.current_vel
            self.hurtbox.x += self.current_vel
            if not self.is_attacking and not self.is_dash and self.is_grounded:
                self.set_animation("run" if keys[pygame.K_LSHIFT] else "walk")
            self.facing_right = True
        elif not self.is_attacking and not self.is_dash and self.is_grounded:
            self.set_animation("idle")

        # Handle attack input
        if keys[pygame.K_j] and not self.is_attacking and not self.is_dash:
            self.is_attacking = True
            self.set_animation("l_attack")

        if keys[pygame.K_s]:
            self.current_grav = GRAV * 2
        else:
            self.current_grav = GRAV

    def handle_event(self, event):
        # Event handler for player class
        if event.type == pygame.KEYDOWN:
            # DASH INPUT
            if event.key == pygame.K_k and not self.is_dash and not self.dash_cooldown and not self.is_attacking:                
                self.is_dash = True
                self.dash_cooldown = True  # Prevent dash from retriggering until reset
                self.set_animation("h_attack")
                clock = pygame.time.Clock()
                keys = pygame.key.get_pressed()
                if not keys[pygame.K_a] and not keys[pygame.K_d]:
                    pass 
                
            #  JUMP INPUT
            if event.key == pygame.K_SPACE and not self.is_attacking:
                if self.is_grounded:
                # Initial jump
                    self.is_grounded = False
                    self.is_jump = True
                    self.y_velocity = -JUMP_FORCE
                    self.set_animation("jump")
                
                elif not self.is_doubleJump:
                    # Double jump
                    self.is_doubleJump = True
                    self.y_velocity = -JUMP_FORCE
                    self.set_animation("jump")

    def update(self, delta_time):
        self.handle_input()

        # Apply gravity if not on the ground
        if not self.is_grounded:
            self.y += self.y_velocity
            self.y_velocity += self.current_grav

            # Check if the player has hit the ground
            if self.y >= SCREEN_HEIGHT - (SPRITE_HEIGHT + GROUND_OFFSET):
                # Reset player to grounded state (maybe introduce state variable and function to do all of this)
                self.y = SCREEN_HEIGHT - (SPRITE_HEIGHT + GROUND_OFFSET)
                self.y_velocity = 0
                self.is_grounded = True
                self.is_jump = False
                self.is_doubleJump = False
                self.is_attacking = False
                self.is_dash = False  # Reset dash state
                self.dash_cooldown = False  # Allow dash to be triggered again

                # Reset VEL to default
                self.current_vel = VEL

                # Reset animation to idle when landing
                self.set_animation("idle")

        # Handle animations and update
        super().update(delta_time)
