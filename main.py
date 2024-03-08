import pygame as pg
import sys
from simulation import Simulation

pg.init()

GREY = (29, 29, 29)
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750
CELL_SIZE = 25
FPS = 12

window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Game of Life")

clock = pg.time.Clock()
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

# Simulation Loop
while True:
    # Event Handling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            row = pos[1] // CELL_SIZE
            column = pos[0] // CELL_SIZE
            simulation.toggle_cell(row, column)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                simulation.start()
                pg.display.set_caption("Game of Life is running")
            elif event.key == pg.K_SPACE:
                simulation.stop()
                pg.display.set_caption("Game of Life has stopped")
            elif event.key == pg.K_f:
                FPS += 2
            elif event.key == pg.K_s:
                if FPS > 5:
                    FPS -= 2
            elif event.key == pg.K_r:
                simulation.create_random_state()
            elif event.key == pg.K_c:
                simulation.clear()

    # 2. Updating State
    simulation.update()

    # 3. Drawing
    window.fill(GREY)
    simulation.draw(window)

    pg.display.update()
    clock.tick(FPS)