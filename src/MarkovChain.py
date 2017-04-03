class Markov_Chain:
    def __init__(self, matrix_size, current_state = 0):
        self.probability_matrix = [[0]*matrix_size for x in range(0, matrix_size)]
        self.matrix_size = matrix_size
        self.current_state = current_state
        
    def add_to_probability_matrix(self, matrix):
        # error if matrices dimensions doesnt equal
        for x, y in zip(self.probability_matrix, matrix):
            x[:] = [a + b for a, b in zip(x, y)]
            
    def learn(self, sequence):
        # error if sequence contains number equal or bigger self.matrix_size
        for row in range(0, self.matrix_size):
            for i in range(0, len(sequence)-1):
                if sequence[i] == row:
                    self.probability_matrix[row][sequence[i+1]] += 1
                        
    # Method divide every element in matrix by sum of all it's elements in row.
    def probability_matrix_normalization(self):
        for i in self.probability_matrix:
            s = sum(i)
            if s != 0:
                i[:] = [a / s for a in i]
            
    def print_probability_matrix(self):
        for x in self.probability_matrix:
            print(x)
