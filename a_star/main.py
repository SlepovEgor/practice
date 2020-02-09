def find_a_path(start, finish, field):
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



    way = None
    current = None
    finish_in_to_check = False
    checked = []
    to_check = []
    alg_field = field

    for y in range(len(alg_field)):
        for x in range(len(alg_field)):
            cell = field[x][y]
            if cell:
                cell.update({'evr': abs(cell['x'] - finish['x']) + abs(cell['y'] - finish['y'])})

    to_check.extend(check_neighboors(start))
    checked.append(start)

    while to_check and not finish_in_to_check:
        to_check.sort(key=lambda item: item['evr'])
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

    return way

# field = {x: {y: {'id': str(x)+str(y),
#                  'x': x,
#                  'y': y,
#                  'passability': True} for y in range(10)} for x in range(10)}
# start = field[0][9]
# finish = field[6][2]
#
# print(*find_a_path(start, finish, field), sep='\n')