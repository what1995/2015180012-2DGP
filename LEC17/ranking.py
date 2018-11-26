from pico2d import *
import random
import math
import boy
import game_framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
from pico2d import *
import world_build_state
import main_state

import world_build_state
import main_state


class Ranking:
    font = None
    def __init__(self, number, score, y):
        self.number = number
        self.score = score
        self.y=y
        if Ranking.font is None:
            Ranking.font = load_font('ENCR10B.TTF', 32)


    def __getstate__(self):
        state = {'number':self.number,'score':self.score, 'y':self.y}
        return state
        # fill here
        pass


    def __setstate__(self, state):
        # fill here
        self.__init__()
        self.__dict__.update(state)
        pass



    def update(self):
        pass



    def draw(self):

        Ranking.font.draw(400,self.y, self.number, (255, 255, 0))
        Ranking.font.draw(440, self.y,'(%4d)' %  self.score, (255, 255, 0))

    def handle_event(self, event):
        pass

