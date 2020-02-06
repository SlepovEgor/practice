import pygame
import random

pygame.init()
clock = pygame.time.Clock()

sc = pygame.display.set_mode((900, 900))

snake_speed = 20

DOWN = 0
UP = 1
RIGHT = 2
LEFT = 3

direction = DOWN

width = 20

start_x = 100
start_y = 100

snake_length = 3

fruit_map = []
fruit_cooldown = 35

snake = []
for part in range(0,snake_length):
    part_dict = {}
    part_dict.update({'id':part})
    part_dict.update({'x':start_x - part * snake_length})
    part_dict.update({'y':start_y})
    part_dict.update({'prev_x':start_x - part * snake_length})
    part_dict.update({'prev_y':start_y})
    if part != 0:
        part_dict.update({'parent': snake[part - 1]})
    snake.append(part_dict)

for row in range(0, int(900 / 20)):
    row_list = []
    for column in range(0, int(900 / 20)):
        row_list.append(0)
    fruit_map.append(row_list)

while 1:
    moved = False
    fruit_cooldown -= 1
    for part in snake:
        if not moved:
            if part.get('id') == 0:
                if direction == DOWN:
                    part.update({'y':part.get('y') + snake_speed})
                elif direction == UP:
                    part.update({'y': part.get('y') - snake_speed})
                elif direction == RIGHT:
                    part.update({'x':part.get('x') + snake_speed})
                elif direction == LEFT:
                    part.update({'x': part.get('x') - snake_speed})

                moved = True

        if part.get('id') != 0:
            part.update({'x': part.get('parent').get('prev_x')})
            part.update({'y': part.get('parent').get('prev_y')})
            part.get('parent').update({'prev_x': part.get('parent').get('x')})
            part.get('parent').update({'prev_y': part.get('parent').get('y')})

    head_check_x = int(snake[0].get('x') / 20)
    head_check_y = int(snake[0].get('y') / 20)
    try:
        if fruit_map[head_check_y][head_check_x] == 1:
            fruit_map[head_check_y][head_check_x] = 0
            snake_length += 1
            part = {}
            part.update({'x': snake[len(snake)-1].get('x')})
            part.update({'y': snake[len(snake)-1].get('y')})
            part.update({'prev_x': snake[len(snake)-1].get('prev_x')})
            part.update({'prev_y': snake[len(snake)-1].get('prev_y')})
            part.update({'id':snake_length})
            part.update({'parent':snake[len(snake) - 1]})
            snake.append(part)
    except:
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = UP
            elif event.key == pygame.K_DOWN:
                direction = DOWN
            elif event.key == pygame.K_RIGHT:
                direction = RIGHT
            elif event.key == pygame.K_LEFT:
                direction = LEFT
            pass

    sc.fill((1,1,1))

    if fruit_cooldown <= 0:
        fruit_cooldown = 35
        fruit_x = random.randint(0, int(900 / 20))
        fruit_y = random.randint(0, int(900 / 20))
        try:
            fruit_map[fruit_y - 1][fruit_x - 1] = 1
        except:
            print(fruit_x)
            print(fruit_y)
            assert False


    for part in snake:
        pygame.draw.rect(sc, (127,127,127), [part.get('x'), part.get('y'), width, width])
        pygame.draw.rect(sc, (243,27,187), [part.get('x') + 3, part.get('y') + 3, width - 6, width - 6])

    for row in range(0, int(900 / 20)):
        for column in range(0, int(900 / 20)):
            if fruit_map[row][column] == 1:
                pygame.draw.rect(sc, (200,1,100), [column * 20, row * 20, width, width])

    pygame.display.update()
    clock.tick(15)