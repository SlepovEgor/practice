import pygame

width_in_block = 200
height_in_block = 90

block_width = 8
block_height = 8


black = (0,0,0)
silver = (192,192,192)
life_map = [[{'x': x, 'y': y, 'fill': None} for x in range(width_in_block)] for y in range(height_in_block)]
life_map[5][5]['fill'] = True
life_map[5][6]['fill'] = True
life_map[6][5]['fill'] = True
life_map[6][4]['fill'] = True
life_map[7][5]['fill'] = True

life_map[45][125]['fill'] = True
life_map[45][126]['fill'] = True
life_map[46][125]['fill'] = True
life_map[46][124]['fill'] = True
life_map[47][125]['fill'] = True

life_map[85][25]['fill'] = True
life_map[85][26]['fill'] = True
life_map[86][25]['fill'] = True
life_map[86][24]['fill'] = True
life_map[87][25]['fill'] = True


pygame.init()
clock = pygame.time.Clock()

main_screen = pygame.display.set_mode((width_in_block * block_width, height_in_block * block_height))

gen = 0

while 1:
    print('Generation: ', gen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    #life
    to_do = []
    for _list in life_map:
        for single_block in _list:
            life_counter = 0
            for y_step in range(-1, 2):
                for x_step in range(-1, 2):
                    if y_step != 0 or x_step != 0:
                        x_check = single_block['x'] + x_step
                        y_check = single_block['y'] + y_step

                        if x_check < 0:
                            x_check = width_in_block - 1
                        elif x_check == width_in_block:
                            x_check = 0

                        if y_check < 0:
                            y_check = height_in_block - 1
                        elif y_check == height_in_block:
                            y_check = 0

                        if life_map[y_check][x_check]['fill']:
                            life_counter += 1
            if single_block['fill']:
                if life_counter < 2 or life_counter > 3:
                    to_do.append((single_block['y'], single_block['x'], None))
            else:
                if life_counter == 3:
                    to_do.append((single_block['y'], single_block['x'], True))

    for item in to_do:
        life_map[item[0]][item[1]]['fill'] = item[2]

    gen+=1

    #draw
    main_screen.fill((1, 1, 1))

    for _list in life_map:
        for single_block in _list:
            if single_block['fill']:
                #pygame.draw.rect(main_screen, silver, [single_block['x'] * block_width, single_block['y'] * block_height, block_width, block_height])
                pygame.draw.circle(main_screen, silver, [int(single_block['x'] * block_width + block_width / 2), int(single_block['y'] * block_height + block_height / 2)], int(block_width / 2))

    pygame.display.update()
    clock.tick(30)