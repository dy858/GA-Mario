import retro

env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
env.reset()

ram = env.get_ram()

full_screen_tiles = ram[0x0500:0x069F+1]

print(full_screen_tiles.shape)
print(full_screen_tiles)