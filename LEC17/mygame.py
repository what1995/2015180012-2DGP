import game_framework
import pico2d
import json
from ranking import Ranking
import game_world
#import main_state as start_state
import world_build_state as start_state

PIXEL_PER_METER = 100 / 3
def create_new_ranking():
    with open('ranking_data.json', 'r')as f:
        ranking_data_list = json.load(f)
    for data in ranking_data_list:
        ranking = Ranking(data['number'], data['score'], data['y'])
        game_world.ranking_list(ranking, 1)

pico2d.open_canvas(int(40 * PIXEL_PER_METER), int(30 * PIXEL_PER_METER))
create_new_ranking()
game_framework.run(start_state)
pico2d.close_canvas()