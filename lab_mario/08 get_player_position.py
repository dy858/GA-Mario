import retro

env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
env.reset()

ram = env.get_ram()

#현재 화면 속 플레이어  좌표 (x, y)
player_position_x = ram[0x03AD]
player_position_y = ram[0x03B8]


#타일 좌표로 변환
player_tile_position_x = (player_position_x + 8) // 16
player_tile_position_y = (player_position_y + 8) // 16 - 1

print(player_tile_position_x)
print(player_tile_position_y)


print(player_position_x)
print(player_position_y)