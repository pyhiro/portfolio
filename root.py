PREVIOUS_ROOT = []
ALL_GOAL_ROOT = []


def file_read(file_name):
    root_map = []
    with open(file_name, 'r') as f:
        txt = f.readlines()
        for line in txt:
            root_map.append(list(line.rstrip('\n')))
    return root_map


def get_pos(all_map):
    """
    :return: start and goal position
    """
    for column, row in enumerate(all_map):
        if 'S' in row:
            s_idx = (column, row.index('S'))
        if 'G' in row:
            g_idx = (column, row.index('G'))
    return((s_idx, g_idx))


def can_move_to(now_pos, all_map):
    can_move_to_list = []
    if (all_map[now_pos[0]-1][now_pos[1]] in (' ', 'G')) and\
            (now_pos[0]-1, now_pos[1]) not in PREVIOUS_ROOT:
        can_move_to_list.append((now_pos[0]-1, now_pos[1]))
    if (all_map[now_pos[0]+1][now_pos[1]] in (' ', 'G')) and\
            (now_pos[0]+1, now_pos[1]) not in PREVIOUS_ROOT:
        can_move_to_list.append((now_pos[0]+1, now_pos[1]))
    if (all_map[now_pos[0]][now_pos[1]-1] in (' ', 'G')) and\
            (now_pos[0], now_pos[1]-1) not in PREVIOUS_ROOT:
        can_move_to_list.append((now_pos[0], now_pos[1]-1))
    if (all_map[now_pos[0]][now_pos[1]+1] in (' ', 'G')) and\
            (now_pos[0], now_pos[1]+1) not in PREVIOUS_ROOT:
        can_move_to_list.append((now_pos[0], now_pos[1]+1))
    return can_move_to_list


def move_to(now_pos, all_map):
    can_move_to_list = can_move_to(now_pos, all_map)
    if can_move_to_list:
        can_move_to_list_copy = can_move_to_list.copy()
        for future_pos in can_move_to_list_copy:
            if future_pos == GOAL:
                ALL_GOAL_ROOT.append(PREVIOUS_ROOT.copy())
                break
            PREVIOUS_ROOT.append(now_pos)
            move_to(future_pos, all_map)
    else:
        PREVIOUS_ROOT.pop()
        return


if __name__ == '__main__':
    root_map = file_read('root.txt')
    print(root_map)
    start, GOAL = get_pos(root_map)
    move_to(start, root_map)


    for li in ALL_GOAL_ROOT:
        root_map_copy = root_map.copy()
        for l in li:
            root_map_copy[l[0]][l[1]] = '$'
        for root_map_ in root_map_copy:
            print(''.join(root_map_))


