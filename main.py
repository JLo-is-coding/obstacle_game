import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
import random

# --- Constants ---
screen_width = 1200
screen_height = 700

# --- Sprite Classes ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 75))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        self.move(pressed_keys)
    
    def move(self, pressed_keys):
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, +5)
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(+5, 0)

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(screen_width +20, screen_width +100),
                random.randint(0, screen_height)
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.move()
        if self.rect.right < 0:
            self.kill()
    
    def move(self):
        self.rect.move_ip(-self.speed, 0)

# --- Main Game Function ---
def main():
    # --- Initialising Pygame ---
    pygame.init()

    # --- Object Initialisation ---
    screen = pygame.display.set_mode([screen_width, screen_height])
    player = Player()
    enemy = Enemy()
    
    # --- Main Game Loop ---
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        enemy.update()

        screen.fill((25, 255, 255))
        screen.blit(player.surf, player.rect)
        screen.blit(enemy.surf, enemy.rect)
        pygame.display.flip()

# --- Call For Main ---
if __name__ == "__main__":
    main()