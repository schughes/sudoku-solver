import csv

class Sudoku:
    def __init__(self, file):
        self.rows, self.mutable_rows = self.init_rows(file)
        self.cols, self.mutable_cols = self.init_cols()
        self.size = len(self.rows)

    # def solve(self):
    #     # recursive backtrack call
    #     def _solve(self, x, y, n):
    #         # check if it's in a mutable spot
    #         if self.mutable_rows[y][x]:
    #             self.rows[y][x] = n
    #             if(self.is_valid()):
    #                 if(x < self.size - 1):
    #                     _solve(self, x + 1, y, n)
    #                 elif(y < self.size - 1):
    #                     _solve(self, 0, y + 1, n)
    #                 else:
    #                     print('DONE')
                
    #             else:
    #                 if n >= 9: # if the number is 9, you have to back up
    #                     n = self.rows[y][x] + 1
    #                     self.rows[y][x] = None
    #                     _solve(self, x - 1, y, n)
    #                 else: # if it's not valid, try incrementing the value
    #                     self.rows[y][x] = None
    #                     _solve(self, x, y, n + 1)
                    
    #         else:
    #             if(x < self.size - 1):
    #                 _solve(self, x + 1, y, n)
    #             elif(y < self.size - 1):
    #                 _solve(self, 0, y + 1, n)
    #             else:
    #                 print('DONE DONE')

    #     _solve(self, 0, 0, 1)
    #     return True

    def solve(self):
        def move_pos(x,y):
            if x < 8:
                x += 1
            elif y < 8:
                x = 0
                y += 1
            else:
                x += 1
                y += 1
            return x, y

        def _solve(self, x, y, n):
            if(x > len(self.rows) - 1 or y > len(self.rows) - 1):
                return self

            if self.mutable_rows[y][x]:
                self.rows[y][x] = n
                
            x, y = move_pos(x,y)
            return _solve(self, x, y, n)

            
        _solve(self, 0, 0, 1)

    def is_valid(self):
        for row in self.rows:
            if not self.is_row_valid(row):
                return False
        for col in self.cols:
            if not self.is_col_valid(col):
                return False
        return True
    
    def init_rows(self, file):
        rows, mutable = [], []
        with open(file) as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append([None if x == 'x' else int(x) for x in row])
                mutable.append([True if x == 'x' else False for x in row])

        return rows, mutable
    
    def get_row(self, i):
        return self.rows[i]

    def is_row_valid(self, row):
        _ = []
        for x in row:
            if x != None:
                _.append(x)
        # _ = [x if x != None for x in row]
        print(_, set(row))

    def init_cols(self):
        cols, mutable= [], []
        for i in range(len(self.rows)):
            _, __ = [], []
            for j in range(len(self.rows[i])):
                _.append(self.rows[j][i])
                __.append(self.mutable_rows[j][i])
            cols.append(_)
            mutable.append(__)
        return cols, mutable

    def get_col(self, i):
        return self.cols[i]
    
    def is_col_valid(self, col):
        return True

    # x = column numnber
    # y = row number
    def get_square(self, x, y):
        '''
        if start new box -> pos, pos + 2
        if in middle of box -> pos - 1, pos + 1
        if end of box -> pos - 2, pos

        get rows in y bound
        index rows using x bound

        # bound(inclusive, exclusive)
        '''
        def get_bound(n):
            bound = None
            match n % 3:
                case 0:
                    bound = (n, n + 3)
                case 1:
                    bound = (n - 1, n + 2)
                case 2:
                    bound = (n - 2, n + 1)
            return bound


        x_bound, y_bound = get_bound(x), get_bound(y)

        vals = [self.get_row(i)[x_bound[0]:x_bound[1]] for i in range(y_bound[0], y_bound[1])]

        # print(vals)
        return vals
