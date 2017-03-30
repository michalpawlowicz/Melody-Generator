from src.Melody import Note, Melody
from miditime.miditime import MIDITime

# Parser methods

# takes string and create integer from it.
# Example: example123string, return 123
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
        node.append(Note(string_to_number(read_data[i][0]) / 1000,
                     string_to_number(read_data[i][3]),
                     string_to_number(read_data[i][4]),
                     string_to_number(read_data[i][2])))
    return Melody(node)

def save_midi_file(data, name, bpm):
    
    mymidi = MIDITime(bpm, name)
    mymidi.add_track(data) 
    mymidi.save_midi()     
