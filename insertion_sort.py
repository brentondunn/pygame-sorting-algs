import pygame
import random

WIDTH = 1000
TOTAL_COLS = 100
FPS = 400
GAP = WIDTH / TOTAL_COLS
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('Insertion Sort Algorithm Visualizer!')
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
DARK_AQUA = (38, 70, 83)
YELLOW = (233, 196, 106)
DARK_ORANGE = (231, 111, 81)

CURSOR_COLOR = DARK_ORANGE
BACKGROUND_COLOR = DARK_AQUA
COLUMN_COLOR = YELLOW


class Col(object):
    def __init__(self, col_number, height):
        self.col_number = col_number
        self.height = height
        self.color = WHITE
        self.x = GAP * col_number

    def __lt__(self, other):
        return self.height > other.height       # is reversed because height is space from top not height of column

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.height, GAP, WIDTH-self.height))

    def change_color(self, color):
        if color == DARK_AQUA:
            self.color = DARK_AQUA
        elif color == YELLOW:
            self.color = YELLOW
        elif color == DARK_ORANGE:
            self.color = DARK_ORANGE


def draw(win, layout):
    win.fill(BACKGROUND_COLOR)
    for i in range(len(layout)):
        layout[i].draw(win)
    pygame.display.update()


def main():
    run = True
    layout = []
    heights = []
    for i in range(TOTAL_COLS):
        rand_int = random.randint(int(WIDTH * .05), int(WIDTH - WIDTH * .05))       # padding so columns aren't too high
        heights.append(rand_int)
    for i in range(TOTAL_COLS):
        layout.append(Col(i, heights[i]))
    draw(WIN, layout)
    step = 0
    forward = 1
    while run:
        if step == 0:
            backward = forward
            step += 1
        elif step == 1:
            try:
                if layout[backward] < layout[backward - 1] and backward > 0:
                    temp = layout[backward - 1]
                    layout[backward - 1] = layout[backward]
                    layout[backward] = temp
                    backward -= 1
                else:
                    step -= 1
                    forward += 1
            except IndexError:
                pass
            for n in range(len(layout)):
                layout[n].x = n * GAP
        try:
            for k in range(forward):
                layout[k].change_color(COLUMN_COLOR)
            layout[backward].change_color(CURSOR_COLOR)
        except IndexError:
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw(WIN, layout)
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
