from miditime.miditime import MIDITime
import numpy as np
import random

def string_to_number(str):
    return int("".join([c for c in str if c.isdigit()]))
            
def parse_midi_file(path):
    with open(path, 'r') as f:
        read_data = f.read()
        f.closed
    read_data = read_data.split('\n')
    matrix_size = len(read_data)
    node = []
    for i in range(matrix_size-1):
        read_data[i] = read_data[i].split(' ')
        # time / node / velocity / beats
        #print(i)
        node.append([string_to_number(read_data[i][0])/1000,
                        string_to_number(read_data[i][3]),
                        string_to_number(read_data[i][4]),
                        string_to_number(read_data[i][2])])
    return node

def create_note(time, pitch, velocity, duration):
    return [time, pitch, velocity, duration]

def save_midi_file(data, name):
    mymidi = MIDITime(200, name)
    midinotes = data
    mymidi.add_track(midinotes)
    mymidi.save_midi()

def update_weight(X, i, j):
    X[i][j] += 1

def probability_of(X, number):
    res = [0] * 127
    for i in range(0, len(X) - 1):
        if X[i] == number:
            res[X[i+1]] += 1
    return res

# X - list
def list_normalization(X):
    s = sum(X)
    if s != 0:
        X[:] = [x / s for x in X]

# X - matrix (2D array)
def matrix_normalization(X):
    for i in X:
        list_normalization(i)

# Y - for example, sequence of notes
def probability_matrix(Y):
    X = []
    for i in range(0, 128):
        X.append(probability_of(Y, i))                
    return X


def index_of_closest(A, x):
    return min(range(len(A)), key=lambda i: abs(A[i]-x))



# X - probability matrix
def next_note(X, current_note):
    rnd = random.uniform(0, max(X[current_note]))
    # olny zeros in row
    # return some closest note
    if (sum(X[current_note]) < 1e-9):
        rnd = random.randint(0, 5)
        return current_note + rnd
    return index_of_closest(X[current_note], rnd)

def sum_lists(A, B):
    return [x + y for x, y in zip(A, B)]

def sum_probability_matrix(A, B):
    result = []
    for x, y in zip(A, B):
        result.append(sum_lists(x, y))
    return result

def return_notes(X):
    result = []
    for i in X:
        result.append(i[1])
    return result

# X - array of paths
def learn(X):
    matrix = [[0] * 128] * 128
    for x in X:
        midi_file = parse_midi_file(x)
        file_prob = probability_matrix(return_notes(midi_file))
        matrix = sum_probability_matrix(matrix, file_prob)
    return matrix

def main():

    P1 = learn([
        #"test1",
        #"test2",
        #"morning_moode",
        #"funeral",
        "moonlight"
    ])
    matrix_normalization(P1)

    #print(P1)
    
    start_point = random.randint(0, 128)
    #start_point = 10
    song = []
    song.append(create_note(0, start_point, 127, 2))

    print(P1)
    
    nextNote = start_point

    for i in range(1, 128):
        nextNote = next_note(P1, int(nextNote))
        x = create_note(i*1, nextNote, 127, 1)
        song.append(x)
   
 #   print(song)
    save_midi_file(song, "lol.mid")


main()

    
