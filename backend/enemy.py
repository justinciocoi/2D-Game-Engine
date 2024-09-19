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
        self.buffer_distance = 50  # Buffer distance before stopping
        self.reaction_delay = 1  # Delay in seconds
        self.time_since_last_action = 0
        self.target_direction = 0  # 0 means idle, -1 means move left, 1 means move right
        self.is_attacking = False
        self.attack_cooldown = 1 # Cooldown between attacks in seconds
        self.time_since_last_attack = 0
        self.attack_frame_duration = 30  # Number of frames the attack lasts
        self.attack_frame_counter = 0  # Counter to track frames during the attack
       

    def define_logic(self, delta_time):
        # Increment timers
        self.time_since_last_action += delta_time
        self.time_since_last_attack += delta_time
        
        # Recalculate distance to player every frame
        player_x = self.player.hurtbox.x  # Ensure this value is updating every frame
        distance_to_player = abs(self.x - player_x)

        # Debugging print statements to monitor state
        print(f"Player Position: {player_x}, Enemy Position: {self.x}")
        print(f"Distance to player: {distance_to_player}, Buffer Distance: {self.buffer_distance}")
        print(f"Is Attacking: {self.is_attacking}, Time Since Last Attack: {self.time_since_last_attack}")
        print(f"Current Direction: {self.target_direction}")
        # Reevaluate after the reaction delay
        if self.time_since_last_action >= self.reaction_delay:
            # Within buffer distance, either attack or idle
            if distance_to_player <= self.buffer_distance:
                # Stop moving if within buffer distance
                self.target_direction = 0
                if not self.is_attacking and self.time_since_last_attack >= self.attack_cooldown:
                    print("Initiating Attack")
                    self.is_attacking = True
                    self.set_animation("l_attack")
                    self.time_since_last_attack = 0  # Reset the cooldown timer
                    self.attack_frame_counter = 0  # Reset the frame counter
            else:
                # Move towards the player
                if player_x < self.x:
                    self.target_direction = -1  # Move left
                    self.set_animation("walk")
                elif player_x > self.x:
                    self.target_direction = 1  # Move right
                    self.set_animation("walk")

            # Reset the action timer
            self.time_since_last_action = 0

        # If attacking, stop moving and re-evaluate after attack completes
        if self.is_attacking:
            self.target_direction = 0  # Stop moving while attacking
            self.attack_frame_counter += 1  # Count frames during the attack

            # Check if the attack animation is complete
            if self.attack_frame_counter >= self.attack_frame_duration:
                print("Attack Completed")
                self.is_attacking = False  # Finish attacking
    def update(self, delta_time):
   
        # Implement the decision-making logic
        self.define_logic(delta_time)

        # Apply continuous movement based on the decided direction
        if self.target_direction == -1:
            self.facing_right = False
            self.x -= VEL * 0.7 # Move left
        elif self.target_direction == 1:
            self.facing_right = True
            self.x += VEL * 0.7  # Move right

        # Handle animations and update
        super().update(delta_time)
