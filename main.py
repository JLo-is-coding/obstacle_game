import pygame

def main():
    pygame.init()

    screen_width = 1200
    screen_height = 700
    screen = pygame.display.set_mode([screen_width, screen_height])
    surf = pygame.Surface((50, 50))
    surf.fill((0, 0, 0))
    surf_center = (
        (screen_width-surf.get_width())/2, 
        (screen_height-surf.get_height())/2
        )

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((25, 255, 255))
        screen.blit(surf, surf_center)
        pygame.display.flip()

if __name__ == "__main__":
    main()