class Reversi:
    Length = 6
    NotPut = 0
    Black = 1
    White = 2

    def __init__(self):
        self.l = [0] * self.Length
        self.boad = []
        for _ in range(self.Length):
            self.boad.append(list(self.l))
        self.boad[int(self.Length/2)-1][int(self.Length/2)-1] = self.boad[int(self.Length/2)][int(self.Length/2)] = self.Black
        self.boad[int(self.Length/2)-1][int(self.Length/2)] = self.boad[int(self.Length/2)][int(self.Length/2)-1] = self.White
        self.b_turn = True
        self.w_turn = False
        self.tmp_l = []
        self.l = {}
        self.ll = []
        self.b_flag = True
        self.w_flag = True
        self.w_count = 0
        self.b_count = 0

    def full_board_or_not(self):
        for i, in_list in enumerate(self.boad):
            if 0 in in_list:
                break
            if i == 7 and (0 not in in_list):
                return False
        return True

    def print_revers_stone(self):
        self.l = {}
        self.ll = []
        if self.b_turn:
            self.b_flag = True
            for i, in_list in enumerate(self.boad):
                for ii, state in enumerate(in_list):
                    if self.boad[i][ii] == self.NotPut:
                        self.b_can_put(i, ii)
                        if self.tmp_l:
                            self.l[(i, ii)] = list(self.tmp_l)
            t = []
            for v in self.l.values():
                t.extend(v)
            t = set(t)
            if self.l.keys():
                for ttt in self.l:
                    self.ll.append(ttt)
                print(self.ll)
            else:
                self.b_flag = False

        if self.w_turn:
            self.w_flag = True
            for i, in_list in enumerate(self.boad):
                for ii, state in enumerate(in_list):
                    if self.boad[i][ii] == self.NotPut:
                        self.w_can_put(i, ii)
                        if self.tmp_l:
                            self.l[(i, ii)] = list(self.tmp_l)
            t = []
            for v in self.l.values():
                t.extend(v)
            t = set(t)
            if self.l.keys():
                for ttt in self.l:
                    self.ll.append(ttt)
                print(self.ll)
            else:
                self.w_flag = False

    def w_can_put(self, i, ii):
        self.tmp_l = []
        try:
            if self.boad[i-1][ii] == self.Black:
                t = 2
                while i-t >= 0 and self.boad[i-t][ii] == self.Black:
                    t += 1
                if i - t >= 0 and self.boad[i-t][ii] == self.White:
                    self.tmp_l.append((i-t, ii))
        except IndexError:
            pass

        try:
            if self.boad[i+1][ii] == self.Black:
                t = 2
                while i+t < self.Length and self.boad[i+t][ii] == self.Black:
                    t += 1
                if i + t < self.Length and self.boad[i+t][ii] == self.White:
                    self.tmp_l.append((i+t, ii))
        except IndexError:
            pass

        try:
            if self.boad[i][ii + 1] == self.Black:
                t = 2
                while ii+t < self.Length and self.boad[i][ii+t] == self.Black:
                    t += 1
                if ii + t < self.Length and self.boad[i][ii+t] == self.White:
                    self.tmp_l.append((i, ii+t))
        except IndexError:
            pass

        try:
            if self.boad[i][ii-1] == self.Black:
                t = 2
                while ii-t >= 0 and self.boad[i][ii-t] == self.Black:
                    t += 1
                if ii - t >= 0 and self.boad[i][ii-t] == self.White:
                    self.tmp_l.append((i, ii-t))
        except IndexError:
            pass

        try:
            if self.boad[i - 1][ii - 1] == self.Black:
                t = 2
                while i - t >= 0 and ii - 1 >= 0 and self.boad[i - t][ii - t] == self.Black:
                    t += 1
                if i - t >= 0 and ii - t >= 0 and self.boad[i - t][ii - t] == self.White:
                    self.tmp_l.append((i - t, ii - t))
        except IndexError:
            pass

        try:
            if self.boad[i - 1][ii + 1] == self.Black:
                t = 2
                while i - t >= 0 and ii + 1 < self.Length and self.boad[i - t][ii + t] == self.Black:
                    t += 1
                if i - t >= 0 and ii + t < self.Length and self.boad[i - t][ii + t] == self.White:
                    self.tmp_l.append((i - t, ii + t))
        except IndexError:
            pass

        try:
            if self.boad[i + 1][ii - 1] == self.Black:
                t = 2
                while i + t < self.Length and ii - 1 >= 0 and self.boad[i + t][ii - t] == self.Black:
                    t += 1
                if i + t < self.Length and ii - 1 >= 0 and self.boad[i + t][ii - t] == self.White:
                    self.tmp_l.append((i + t, ii - t))
        except IndexError:
            pass

        try:
            if self.boad[i + 1][ii + 1] == self.Black:
                t = 2
                while i + t < self.Length and ii + 1 < self.Length and self.boad[i + t][ii + t] == self.Black:
                    t += 1
                if i + t < self.Length and ii + 1 < self.Length and self.boad[i + t][ii + t] == self.White:
                    self.tmp_l.append((i + t, ii + t))
        except IndexError:
            pass

    def b_can_put(self, i, ii):
        self.tmp_l = []
        try:
            if self.boad[i - 1][ii] == self.White:
                t = 2
                while i - t >= 0 and self.boad[i - t][ii] == self.White:
                    t += 1
                if i - t >= 0 and self.boad[i - t][ii] == self.Black:
                    self.tmp_l.append((i - t, ii))
        except IndexError:
            pass

        try:
            if self.boad[i + 1][ii] == self.White:
                t = 2
                while i + t < self.Length and self.boad[i + t][ii] == self.White:
                    t += 1
                if i + t < self.Length and self.boad[i + t][ii] == self.Black:
                    self.tmp_l.append((i + t, ii))
        except IndexError:
            pass

        try:
            if self.boad[i][ii + 1] == self.White:
                t = 2
                while ii + t < self.Length and self.boad[i][ii + t] == self.White:
                    t += 1
                if ii + t < self.Length and self.boad[i][ii + t] == self.Black:
                    self.tmp_l.append((i, ii + t))
        except IndexError:
            pass

        try:
            if self.boad[i][ii - 1] == self.White:
                t = 2
                while ii - t >= 0 and self.boad[i][ii - t] == self.White:
                    t += 1
                if ii - t >= 0 and self.boad[i][ii-t] == self.Black:
                    self.tmp_l.append((i, ii - t))
        except IndexError:
            pass

        try:
            if self.boad[i-1][ii-1] == self.White:
                t = 2
                while i - t >= 0 and ii -1 >= 0 and self.boad[i-t][ii-t] == self.White:
                    t += 1
                if i - t >= 0 and ii -t >= 0 and self.boad[i-t][ii-t] == self.Black:
                    self.tmp_l.append((i-t, ii-t))
        except IndexError:
            pass

        try:
            if self.boad[i-1][ii+1] == self.White:
                t = 2
                while i - t >= 0 and ii + 1 < self.Length and self.boad[i-t][ii+t] == self.White:
                    t += 1
                if i - t >= 0 and ii + t < self.Length and self.boad[i-t][ii+t] == self.Black:
                    self.tmp_l.append((i-t, ii+t))
        except IndexError:
            pass

        try:
            if self.boad[i + 1][ii - 1] == self.White:
                t = 2
                while i + t < self.Length and ii - 1 >= 0 and self.boad[i + t][ii - t] == self.White:
                    t += 1
                if i + t < self.Length and ii - 1 >= 0 and self.boad[i + t][ii - t] == self.Black:
                    self.tmp_l.append((i+t, ii-t))
        except IndexError:
            pass

        try:
            if self.boad[i + 1][ii + 1] == self.White:
                t = 2
                while i + t < self.Length and ii + 1 < self.Length and self.boad[i + t][ii + t] == self.White:
                    t += 1
                if i + t < self.Length and ii + 1 < self.Length and self.boad[i + t][ii + t] == self.Black:
                    self.tmp_l.append((i+t, ii+t))
        except IndexError:
            pass

    def reverse_stone_to_w(self, i, ii):
        self.w_can_put(i, ii)
        for t in self.tmp_l:
            x, y = t
            n = 0
            if i == x and y > ii:
                for _ in range(y-ii):
                    self.boad[i][ii+n] = self.White
                    n += 1
            elif i == x and y < ii:
                for _ in range(ii-y):
                    self.boad[i][ii-n] = self.White
                    n += 1
            elif i > x and y == ii:
                for _ in range(i-x):
                    self.boad[i-n][ii] = self.White
                    n += 1
            elif i < x and y == ii:
                for _ in range(x-i):
                    self.boad[i+n][ii] = self.White
                    n += 1
            elif i > x and y > ii:
                for _ in range(y-ii):
                    self.boad[i-n][ii+n] = self.White
                    n += 1
            elif i < x and y > ii:
                for _ in range(y-ii):
                    self.boad[i+n][ii+n] = self.White
                    n += 1
            elif i > x and y < ii:
                for _ in range(ii-y):
                    self.boad[i-n][ii-n] = self.White
                    n += 1
            elif i < x and y < ii:
                for _ in range(ii-y):
                    self.boad[i+n][ii-n] = self.White
                    n += 1

    def reverse_stone_to_b(self, i, ii):
        self.b_can_put(i, ii)
        for t in self.tmp_l:
            x, y = t
            n = 0
            if i == x and y > ii:
                for _ in range(y-ii):
                    self.boad[i][ii+n] = self.Black
                    n += 1
            elif i == x and y < ii:
                for _ in range(ii-y):
                    self.boad[i][ii-n] = self.Black
                    n += 1
            elif i > x and y == ii:
                for _ in range(i-x):
                    self.boad[i-n][ii] = self.Black
                    n += 1
            elif i < x and y == ii:
                for _ in range(x-i):
                    self.boad[i+n][ii] = self.Black
                    n += 1
            elif i > x and y > ii:
                for _ in range(y-ii):
                    self.boad[i-n][ii+n] = self.Black
                    n += 1
            elif i < x and y > ii:
                for _ in range(y-ii):
                    self.boad[i+n][ii+n] = self.Black
                    n += 1
            elif i > x and y < ii:
                for _ in range(ii-y):
                    self.boad[i-n][ii-n] = self.Black
                    n += 1
            elif i < x and y < ii:
                for _ in range(ii-y):
                    self.boad[i+n][ii-n] = self.Black
                    n += 1

    def print_board(self):
        for in_row in self.boad:
            print("")
            for i in in_row:
                if i == 0:
                    print("△", end="")
                if i == 1:
                    print("◯", end="")
                if i == 2:
                    print("✕", end="")
        print("")

    def judge(self):

        for in_row in self.boad:
            for i in in_row:
                if i == self.White:
                    self.w_count += 1
                if i == self.Black:
                    self.b_count += 1
        if self.w_count == self.b_count:
            print(str(self.w_count) + " : " + str(self.b_count) + "で引き分け")

        elif self.b_count > self.w_count:
            print(str(self.w_count) + ":" + str(self.b_count) + "で◯のかち")

        elif self.b_count < self.w_count:
            print(str(self.w_count) + ":" + str(self.b_count) + "で✕のかち")

if __name__ == "__main__":
    import time
    game = Reversi()
    while game.full_board_or_not():
        time.sleep(0.5)
        game.print_board()
        time.sleep(0.5)
        game.print_revers_stone()
        if game.b_flag:

            num = int(input("input idx of list! where　◯ put:"))
            t = game.ll[num]
            game.reverse_stone_to_b(*t)
        game.b_turn = False
        game.w_turn = True

        time.sleep(0.5)
        game.print_board()
        time.sleep(0.5)
        game.print_revers_stone()
        if game.w_flag:
            num = int(input("input idx of list! where ✕ put:"))
            t = game.ll[num]
            game.reverse_stone_to_w(*t)
        game.b_turn = True
        game.w_turn = False

        if game.w_flag == False and game.b_flag == False:
            break
    game.judge()