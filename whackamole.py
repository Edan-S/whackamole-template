import pygame
import random





def main():
    count = 0
    def is_click(x, y):
        if event.type == pygame.MOUSEBUTTONDOWN:
            a, b = event.pos
            j = a//32
            k = b//32
            j *= 32
            k *= 32
            if (j, k) == (x, y):
                return True
            return False

    def change_position():
        x = random.randrange(0, 641)//32
        y = random.randrange(0, 513)//32
        x *= 32
        y *= 32
        positions = [x, y]
        return positions

    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")

            for i in range(1, 20):
                x = 32 * i
                pygame.draw.line(screen, "black", (x, 0), (x, 512), 2)

            for i in range(1, 16):
                y = 32 * i
                pygame.draw.line(screen, "black", (0, y), (640, y), 2)

            if count == 0:
                list = [0,0]

            screen.blit(mole_image, mole_image.get_rect(topleft=(list[0], list[1])))



            if is_click(list[0],list[1]) == True:
                list = change_position()
                count += 1




            pygame.display.flip()
            clock.tick(60)



    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
