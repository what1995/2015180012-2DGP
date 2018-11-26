from pico2d import *
import random
import math
import main_state
import game_framework

from pico2d import *


class Ranking:
    font = None
    def __init__(self,  score,y):
        self.score=score
        self.y=y
        if Ranking.font is None:
            Ranking.font = load_font('ENCR10B.TTF', 32)


    def __getstate__(self):
        state = {'score':self.score}
        return state
        # fill here
        pass


    def __setstate__(self, state):
        # fill here
        self.__init__()
        self.__dict__.update(state)
        pass



    def update(self):
        self.score=main_state.score

        pass



    def draw(self):

        Ranking.font.draw(440, self.y,'(%4d)' % self.score, (255, 255, 0))

    def handle_event(self, event):
        pass

