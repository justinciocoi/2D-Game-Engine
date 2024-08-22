import pygame
import random
from backend.settings import *
from backend.character import *


class Enemy(Character):
    def __init__(self, x, y, animations, player):
        super().__init__(x, y, animations)
        self.health = 20
        self.attack_power = 5
        self.player = player  # Reference to the player object
        self.player_hurtbox = player
        self.buffer_distance = 100  # Buffer distance before stopping
        self.reaction_delay = 1  # Delay in seconds
        self.time_since_last_action = 0
        self.target_direction = 0  # 0 means idle, -1 means move left, 1 means move right

    def define_logic(self, delta_time):
        # Increment the timer for delayed decision-making
        self.time_since_last_action += delta_time

        # Update movement direction only after the reaction delay
        if self.time_since_last_action >= self.reaction_delay:
            # Get the player's position
            player_x = self.player.hurtbox.x
            distance_to_player = abs(self.x - player_x)

            # Determine the target direction based on player's position
            if distance_to_player > self.buffer_distance:
                if player_x < self.x:
                    self.target_direction = -1  # Move left
                    self.set_animation("walk")
                elif player_x > self.x:
                    self.target_direction = 1  # Move right
                    self.set_animation("walk")
            else:
                # Within the buffer distance, go idle or attack
                self.target_direction = 0  # Stop moving
                if not self.is_attacking:
                    self.is_attacking = True
                    self.set_animation("l_attack")

            # Reset the timer for the next decision-making interval
            self.time_since_last_action = 0

    def update(self, delta_time):
        # Implement the decision-making logic
        self.define_logic(delta_time)

        # Apply continuous movement based on the decided direction
        if self.target_direction == -1:
            self.facing_right = False
            self.x -= VEL  # Move left
        elif self.target_direction == 1:
            self.facing_right = True
            self.x += VEL  # Move right

        # Handle animations and update
        super().update(delta_time)
