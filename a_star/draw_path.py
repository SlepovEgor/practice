import pygame
import a_star.main
pygame.init()
clock = pygame.time.Clock()

main_screen = pygame.display.set_mode((1000, 650))

field = {x: {y: {'id': str(x)+str(y),
                 'x': x,
                 'y': y,
                 'passability': True} for y in range(13)} for x in range(20)}
start = field[0][0]
finish = field[9][9]
to_draw = False
step_by_step = False
start_step_by_step = False

field[3][0]['passability'] = False
field[3][1]['passability'] = False
field[3][2]['passability'] = False
field[3][3]['passability'] = False
field[3][4]['passability'] = False
field[3][6]['passability'] = False
field[3][7]['passability'] = False
field[3][9]['passability'] = False
field[7][0]['passability'] = False
field[7][1]['passability'] = False
field[7][2]['passability'] = False
field[7][4]['passability'] = False
field[7][5]['passability'] = False
field[7][6]['passability'] = False
field[7][7]['passability'] = False
field[7][8]['passability'] = False
field[7][9]['passability'] = False

width = 50

way = None
current = None
finish_in_to_check = False
checked = []
to_check = []
alg_field = field

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                way = a_star.main.find_a_path(start, finish, field)
                print(*way,sep='\n')
                to_draw = True
            if event.key == pygame.K_DOWN:
                step_by_step = True
                print('STARTING STEP BY STEP')



    if step_by_step:
        def check_neighboors(point):
            output = []

            steps = (-1, 1)
            for step in steps:
                cell = alg_field.get(point['x'] + step, {}).get(point['y'])
                if cell:
                    if cell['passability']:
                        if not cell.get('parent', False):
                            cell.update({'parent': point})
                        output.append(cell)
                cell = alg_field.get(point['x'], {}).get(point['y'] + step)
                if cell:
                    if cell['passability']:
                        if not cell.get('parent', False):
                            cell.update({'parent': point})
                        output.append(cell)
            return output

        if not start_step_by_step:
            for y in range(13):
                for x in range(20):
                    cell = field[x][y]
                    if cell:
                        cell.update({'evr': abs(cell['x'] - finish['x']) + abs(cell['y'] - finish['y'])})

            to_check.extend(check_neighboors(start))
            checked.append(start)
            start_step_by_step = True

        if to_check and not finish_in_to_check:
            #to_check.sort(key=lambda item: item['evr'])
            current = to_check.pop(0)

            if current == finish:
                finish_in_to_check = True
            else:
                points = check_neighboors(current)
                for point in points:
                    if point not in checked and point not in to_check:
                        to_check.append(point)
                checked.append(current)

        if finish_in_to_check:
            way = [finish]
            while current.get('parent'):
                way.append(current.get('parent'))
                wait = current.get('parent')
                current.pop('parent')
                current = wait
                step_by_step = False
            to_draw = True

    #draw
    main_screen.fill((1, 1, 1))

    for y in range(13):
        for x in range(20):
            if field[x][y]['passability']:
                pygame.draw.rect(main_screen, (200, 200, 200),
                                 [x * width,
                                  y * width,
                                  width,
                                  width])
            else:
                pygame.draw.rect(main_screen, (50, 50, 50),
                                 [x * width,
                                  y * width,
                                  width,
                                  width])
    if to_check:
        for cell in to_check:
            pygame.draw.rect(main_screen, (0, 64, 255),
                             [cell['x'] * width,
                              cell['y'] * width,
                              width,
                              width])
    if checked:
        for cell in checked:
            pygame.draw.rect(main_screen, (11, 102, 35),
                             [cell['x'] * width,
                              cell['y'] * width,
                              width,
                              width])
    if start and finish:
        pygame.draw.rect(main_screen, (255, 165, 0),
                         [start['x'] * width,
                          start['y'] * width,
                          width,
                          width])

        pygame.draw.rect(main_screen, (128,0,0),
                         [finish['x'] * width,
                          finish['y'] * width,
                          width,
                          width])
    if to_draw:
        if way:
            for cell in way:
                pygame.draw.rect(main_screen, (123, 123, 123),
                                 [cell['x'] * width + int(width/4),
                                  cell['y'] * width + int(width/4),
                                  int(width/2),
                                  int(width/2)])
    pygame.display.update()
    clock.tick(5)