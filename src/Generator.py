import random
from src.MarkovChain import Markov_Chain
from src.FileHandler import parse_midi_file
class Melody_Generator:
    def __init__(self, notes_range, duration_range, start_note = 0, start_duration = 0):
        self.notes_markov_chain = Markov_Chain(notes_range, start_note)
        self.duration_markov_chain = Markov_Chain(duration_range, start_duration)
        
    def index_of_closest_element_in_list(self, list, x):
        return min(range(len(list)), key=lambda i: abs(list[i] - x))
    
    def return_next_note(self):
        random_number = random.uniform(
            0, 
            max(self.notes_markov_chain.probability_matrix[self.notes_markov_chain.current_note])
        )
        index_of_closest = self.index_of_closest_element_in_list(
            self.notes_markov_chain.probability_matrix[self.notes_markov_chain.current_note], 
            random_number
        )
        while (sum(self.notes_markov_chain.probability_matrix[index_of_closest]) == 0):
            random_number = random.uniform(0, max(self.notes_markov_chain.probability_matrix[self.notes_markov_chain.current_note]))
            index_of_closest = self.index_of_closest_element_in_list(
                self.notes_markov_chain.probability_matrix[self.notes_markov_chain.current_note], 
                random_number
            )
        return index_of_closest
        
    @staticmethod
    def learn(paths_list, markov_chain: Markov_Chain):
        for p in paths_list:
            print("Otwieram: " + p)
            song = parse_midi_file(p)
            markov_chain.learn(song.pitch)
            
        
    @staticmethod
    def random_starting_point(markov_chain: Markov_Chain):
        # randomint(a, b) generate random number from interval a <= x <= b
        starting_point = random.randint(0, markov_chain.matrix_size - 1)
        while(sum(markov_chain.probability_matrix[starting_point]) == 0):
            starting_point = random.randint(0, markov_chain.matrix_size - 1)
        return starting_point

    @staticmethod
    def check_row_if_zero(number, markov_chain: Markov_Chain):
        if sum(markov_chain.probability_matrix[number]) == 0:
            return -1
        return 1