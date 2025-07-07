from settings import *
from level import Level
from pytmx.util_pygame import load_pygame
from os.path import join
from support import *

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Super Pirate World')
        self.clock = pygame.time.Clock()
        self.import_assets()

        self.tmx_maps = {0: load_pygame(join('.', 'assets', 'data', 'levels', 'omni.tmx'))}
        self.current_stage = Level(self.tmx_maps[0], self.level_frames)

    def import_assets(self):
        self.level_frames = {
            'flag': import_folder('.', 'assets', 'graphics', 'level', 'flag'),
            'saw': import_folder('.', 'assets', 'graphics', 'enemies', 'saw', 'animation'),
            'floor_spike': import_folder('.', 'assets', 'graphics', 'enemies', 'floor_spikes'),
            'palms': import_sub_folders('.', 'assets', 'graphics', 'level', 'palms'),
            'candle': import_folder('.', 'assets', 'graphics', 'level', 'candle'),
            'window': import_folder('.', 'assets', 'graphics', 'level', 'window'),
            'big_chain': import_folder('.', 'assets', 'graphics', 'level', 'big_chains'),
            'small_chain': import_folder('.', 'assets', 'graphics', 'level', 'small_chains'),
            'candle_light': import_folder('.', 'assets', 'graphics', 'level', 'candle light'),
            'player': import_sub_folders('.', 'assets', 'graphics', 'player'),
            'saw': import_folder('.', 'assets', 'graphics', 'enemies', 'saw', 'animation'),
            'saw_chain': import_image('.', 'assets', 'graphics', 'enemies', 'saw', 'saw_chain'),
            'helicopter': import_folder('.', 'assets', 'graphics', 'level', 'helicopter'),
            'boat': import_folder('.', 'assets', 'graphics', 'objects', 'boat'),
            'spike': import_image('.', 'assets', 'graphics', 'enemies', 'spike_ball', 'Spiked Ball'),
            'spike_chain': import_image('.', 'assets', 'graphics', 'enemies', 'spike_ball', 'spiked_chain'),
            'tooth': import_folder('.', 'assets', 'graphics', 'enemies', 'tooth', 'run'),
            'shell': import_sub_folders('.', 'assets', 'graphics', 'enemies', 'shell'),
            'pearl': import_image('.', 'assets', 'graphics', 'enemies', 'bullets', 'pearl'),
        }

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.current_stage.run(dt)
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()