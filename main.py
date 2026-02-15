import pygame

def main():
    pygame.init()

    screen_width = 1200
    screen_height = 700
    screen = pygame.display.set_mode([screen_width, screen_height])

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (0, 0, 255), (screen_width/2, screen_height/2), 75)
        pygame.display.flip()

if __name__ == "__main__":
    main()