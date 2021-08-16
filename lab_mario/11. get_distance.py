import retro

env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
env.reset()

ram = env.get_ram()

#플레이어가 속한 화면 페이지 번호
player_horizon_position = ram[0x006D]
#페이지 속 플레이어 x 좌표
player_screen_position_x = ram[0x0086]

distance = 256 * player_horizon_position + player_screen_position_x

print(distance)
