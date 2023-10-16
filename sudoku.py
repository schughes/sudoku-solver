import csv

class Sudoku:
    def __init__(self, file):
        self.rows = self.init_rows(file)
        self.cols = self.init_cols()

    # TODO: validate file is square
    
    def init_rows(self, file):
        rows = []
        with open(file) as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append([None if x == 'x' else int(x) for x in row])
        return rows
    
    def get_row(self, i):
        return self.rows[i]

    def is_row_valid(self,row):
        return True

    def init_cols(self):
        cols = []
        for i in range(len(self.rows)):
            _ = []
            for j in range(len(self.rows[i])):
                _.append(self.rows[j][i])
            cols.append(_)
        return cols

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

        x_bound, y_bound = None, None
        if(x % 3 == 0):
            x_bound = (x, x + 3)
        elif(x % 3 == 1):
            x_bound = (x - 1, x + 2)
        else:
            x_bound = (x - 2, x + 1)
        if(y % 3 == 0):
            y_bound = (y, y + 3)
        elif(y % 3 == 1):
            y_bound = (y - 1, y + 2)
        else:
            y_bound = (y - 2, y + 1)

        vals = [self.get_row(i)[x_bound[0]:x_bound[1]] for i in range(y_bound[0], y_bound[1])]

        return vals

        # print(vals)
            
        # print(x_bound[0], x_bound[1])
        # print(y_bound[0], y_bound[1])
