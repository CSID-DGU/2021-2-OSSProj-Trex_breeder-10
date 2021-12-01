from src.dino import *
from src.gameMode.arcadeMode import gameplay_hard
from src.gameMode.classicMode import gameplay_easy
from src.gameMode.multiMode import gameplay_multi

dino_type = ['ORIGINAL','RED','ORANGE','YELLOW','GREEN','PURPLE','BLACK','PINK']
type_idx = 0

def call_game(game_mode):
    game_mode_dict = {
        'classic':1,
        'arcade':2,
        'multi':3
    }

    game_mode_number = game_mode_dict[str(game_mode)]

    playerDino = Dino(dino_size[0], dino_size[1], type=dino_type[type_idx])

    if game_mode_number == 1:
        return gameplay_easy(playerDino)
    elif game_mode_number == 2:
        init_stage = 1
        init_life = 15
        init_speed = 4
        init_score = 0
        gameplay_hard(init_stage, init_life, init_speed, init_score, playerDino)
    else:
        gameplay_multi()
