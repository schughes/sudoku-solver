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

        print(vals)
        return vals
