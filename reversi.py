white = 0
black = 1


class ReversiBoard():

    def __init__(self):
        #8x8のボードを作成
        self.board = []
        for _ in range(8):
            self.board.append([None]*8)

        self.board[3][3] = white
        self.board[3][4] = black
        self.board[4][3] = black
        self.board[4][4] = white

    def put_stone(self, x, y, player):
        """
        :param x, y: 置く石の座標
        :param player: white or black
        :return: True or False

        ・置こうとするところに石が置かれていないこと
        ・石を置くと獲得できる相手の石があること
        以上の条件を満たした場合、ボードを更新しTrueを返す
        """

        if self.board[y][x] is not None:
            return False

        #can_flipの中身は、ひっくり返るx,y座標のリスト
        can_flip = self.list_flippable_disks(x, y, player)
        if can_flip == []:
            return False

        #上の条件を満たした場合、以下のメソッドで更新
        self.board[y][x] = player

        for x, y in can_flip:
            self.board[y][x] = player

        return True

    def list_flippable_disks(self, x, y, player):
        """ひっくり返せるます目の座標を返す
        return: can_flip
        """
        try:
            can_flip = []
            for i in [-1, 1]:
                    #横の判定

                    if (self.board[y + i][x] != player and
                        self.board[y + i][x] is not None):
                        temp_flip = []
                        for i2 in range(8):
                            tmp_y = y + i2

                            if tmp_y >= 8:
                                break
                            if (self.board[tmp_y][x] != player and
                                self.board[tmp_y][x] is not None):
                                temp_flip.append((x, tmp_y))
                            if self.board[tmp_y][x] == player:
                                for x, tmp_y in temp_flip:
                                    can_flip.append((x, tmp_y))
                                    temp_flip = []
                                break
                        temp_flip = []
                        for i2 in range(8):
                            tmp_y = y - i2

                            if tmp_y < 0:
                                break
                            if (self.board[tmp_y][x] != player and
                                    self.board[tmp_y][x] is not None):
                                temp_flip.append((x, tmp_y))
                            if self.board[tmp_y][x] == player:
                                for x, tmp_y in temp_flip:
                                    can_flip.append((x, tmp_y))
                                    temp_flip = []
                                break
                    #縦の判定
                    if (self.board[y][x + i] != player and
                        self.board[y][x + i] is not None):
                        temp_flip = []
                        for i2 in range(8):
                            tmp_x = x + i2
                            if tmp_x >= 8:
                                break
                            if (self.board[y][tmp_x] != player and
                                self.board[y][tmp_x] is not None):
                                temp_flip.append((tmp_x, y))
                            if self.board[y][tmp_x] == player:
                                for tmp_x, y in temp_flip:
                                    can_flip.append((tmp_x, y))
                                    temp_flip = []
                                break

                        temp_flip = []
                        for i2 in range(8):
                            tmp_x = x - i2
                            if tmp_x < 0:
                                break
                            if (self.board[y][tmp_x] != player and
                                    self.board[y][tmp_x] is not None):
                                temp_flip.append((tmp_x, y))
                            if self.board[y][tmp_x] == player:
                                for tmp_x, y in temp_flip:
                                    can_flip.append((tmp_x, y))
                                    temp_flip = []
                                break
                    #斜めの判定

                    for i2 in [-1, 1]:
                        if (self.board[y + i][x + i2] != player and
                            self.board[y + i][x + i2] is not None):
                            temp_flip = []
                            for i3 in range(8):
                                tmp_x = x + i3
                                tmp_y = y + i3
                                if (tmp_x < 0 or tmp_x >=8 or
                                        tmp_y <0 or tmp_y >=8):
                                    break
                                if (self.board[tmp_y][tmp_x] != player and
                                    self.board[tmp_y][tmp_x] is not None):
                                    temp_flip.append((tmp_x, tmp_y))
                                if self.board[tmp_y][tmp_x] == player:
                                    for tmp_x, tmp_y in temp_flip:
                                        can_flip.append((tmp_x, tmp_y))
                                    temp_flip = []
                                    break

                            for i3 in range(8):
                                tmp_x = x - i3
                                tmp_y = y + i3
                                if (tmp_x < 0 or tmp_x >= 8 or
                                        tmp_y < 0 or tmp_y >= 8):
                                    break
                                if (self.board[tmp_y][tmp_x] != player and
                                        self.board[tmp_y][tmp_x] is not None):
                                    temp_flip.append((tmp_x, tmp_y))
                                if self.board[tmp_y][tmp_x] == player:
                                    for tmp_x, tmp_y in temp_flip:
                                        can_flip.append((tmp_x, tmp_y))
                                    temp_flip = []
                                    break

                            for i3 in range(8):
                                tmp_x = x + i3
                                tmp_y = y - i3
                                if (tmp_x < 0 or tmp_x >= 8 or
                                        tmp_y < 0 or tmp_y >= 8):
                                    break
                                if (self.board[tmp_y][tmp_x] != player and
                                        self.board[tmp_y][tmp_x] is not None):
                                    temp_flip.append((tmp_x, tmp_y))
                                if self.board[tmp_y][tmp_x] == player:
                                    for tmp_x, tmp_y in temp_flip:
                                        can_flip.append((tmp_x, tmp_y))
                                    temp_flip = []
                                    break

                            for i3 in range(8):
                                tmp_x = x - i3
                                tmp_y = y - i3
                                if (tmp_x < 0 or tmp_x >= 8 or
                                        tmp_y < 0 or tmp_y >= 8):
                                    break
                                if (self.board[tmp_y][tmp_x] != player and
                                        self.board[tmp_y][tmp_x] is not None):
                                    temp_flip.append((tmp_x, tmp_y))
                                if self.board[tmp_y][tmp_x] == player:
                                    for tmp_x, tmp_y in temp_flip:
                                        can_flip.append((tmp_x, tmp_y))
                                    temp_flip = []
                                    break
        except IndexError:
            pass
        return can_flip

    def show_board(self):
        #ボードを表示
        print("##" * 20)
        for i in self.board:
            for cell in i:
                if cell == white:
                    print("W", end="")
                elif cell == black:
                    print("B", end="")
                else:
                    print("*", end="")
            print("\n", end="")


    def list_possible_cells(self, player):

        possible = []
        for x in range(8):
            for y in range(8):
                if self.board[y][x] is not None:
                    continue
                if self.list_flippable_disks(x, y, player) == []:
                    continue
                else:
                    possible.append((x, y))
        return possible

#######################################################

if __name__ == "__main__":
    board = ReversiBoard()
    board.show_board()
    board.put_stone(3, 2, black)
    board.show_board()
    board.put_stone(2, 4, white)
    board.show_board()
    board.put_stone(3, 1, white)
    board.show_board()
