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

screen_width = 1200
screen_height = 700

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 75))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

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

def main():
    pygame.init()

    screen = pygame.display.set_mode([screen_width, screen_height])
    player = Player()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pressed_keys = pygame.key.get_pressed()
        player.move(pressed_keys)

        screen.fill((25, 255, 255))
        screen.blit(player.surf, player.rect)
        pygame.display.flip()

if __name__ == "__main__":
    main()