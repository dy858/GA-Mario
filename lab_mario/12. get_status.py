import retro

env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
env.reset()

ram = env.get_ram()


player_float_state = ram[0x0010]


if player_float_state == 0x03:
    print('mffld')


player_state = ram[0x000E]

if player_state == 0x06 or player_state == 0x0B:
    print('게임오버1')
player_vertical_screen_position = ram[0x00B5]

if player_vertical_screen_position >= 2:
    print('게임오버2')