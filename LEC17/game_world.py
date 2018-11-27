import pickle
import json
# layer 0: Background Objects
# layer 1: Foreground Objects
objects = [[],[]]
rank_list=[]
def ranking_list():
    global rank_list
    with open('ranking_data.json', 'r')as f:
        rank_list = json.load(f)
def ranking_save():
    pass
    with open('ranking_data.json', 'w')as f:
        json.dump(rank_list,f)






def add_object(o, layer):
    objects[layer].append(o)


def add_objects(l, layer):
    objects[layer] += l


def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break


def clear():
    for l in objects:
        l.clear()


def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o


def save():
    with open('game.sav', 'wb') as f:
        pickle.dump(objects, f)
    # fill here


def load():
    global objects
    with open('game.sav','rb') as f:
        objects = pickle.load(f)
    # fill here
