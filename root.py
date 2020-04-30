PREVIOUS_ROOT = []
ALL_GOAL_ROOT = []
EDGE_FLAG = False


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
    global EDGE_FLAG
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
    EDGE_FLAG = True
    return can_move_to_list


def move_to(now_pos, all_map):
    can_move_to_list = can_move_to(now_pos, all_map)
    global EDGE_FLAG
    if can_move_to_list:
        for future_pos in can_move_to_list:
            if future_pos == GOAL:
                PREVIOUS_ROOT.append(now_pos)
                ALL_GOAL_ROOT.append(PREVIOUS_ROOT.copy())
                PREVIOUS_ROOT.pop()
                PREVIOUS_ROOT.pop()
                EDGE_FLAG = False
                return
            PREVIOUS_ROOT.append(now_pos)
            move_to(future_pos, all_map)
            if future_pos == can_move_to_list[-1]:
                EDGE_FLAG = True
            else:
                EDGE_FLAG = False
            if EDGE_FLAG:
                PREVIOUS_ROOT.pop()
                EDGE_FLAG = False
                break
    else:
        PREVIOUS_ROOT.pop()
        EDGE_FLAG = False
        return



if __name__ == '__main__':
    root_map = file_read('root.txt')
    start, GOAL = get_pos(root_map)
    PREVIOUS_ROOT.append(start)
    move_to(start, root_map)

    shortest_root = ALL_GOAL_ROOT[0]
    for check_shortest in ALL_GOAL_ROOT:
        if len(check_shortest) < len(shortest_root):
            shortest_root = check_shortest

    shortest_root.pop(0)
    shortest_root.pop(0)
    for change_pos in shortest_root:
        root_map[change_pos[0]][change_pos[1]] = '$'

    for line in root_map:
        print(''.join(line))



