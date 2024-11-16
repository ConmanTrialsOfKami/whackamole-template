import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:

        molex = 0
        moley = 0
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos
                    molerect = pygame.Rect(molex, moley, 32, 32)

                    if molerect.collidepoint(mousex, mousey):
                        molex = random.randrange(20) * 32
                        moley = random.randrange(16) * 32


            screen.fill("light green")
            for x in range(0, 641, 32):
                pygame.draw.line(screen, "black", (x, 0), (x, 512))

            for y in range(0, 513, 32):
                pygame.draw.line(screen, "black", (0, y), (640, y))
            screen.blit(mole_image, mole_image.get_rect(topleft=(molex, moley)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
