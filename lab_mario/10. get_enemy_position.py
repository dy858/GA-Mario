import retro

env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
env.reset()

ram = env.get_ram()

#자신이 속한 화면의 페이지 번호
enemy_horizon_position = ram[0x006E:0x0072+1]
#자신이 속한 페이지 속 x좌표
enemy_screen_position_x = ram[0x0087:0x008B+1]

enemy_position_y = ram[0x00CF:0x00D3+1]

enemy_position_x = (enemy_horizon_position * 256 + enemy_screen_position_x) % 512

print(enemy_position_x, enemy_position_y)