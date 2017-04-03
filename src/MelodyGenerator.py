from src.FileHandler import parse_midi_file, save_midi_file
from src.Generator import Melody_Generator
from src.Melody import Note
from src.Melody import Melody
import argparse
import os
import random

def __arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("output", help="Output file name")
    parser.add_argument("--bpm", help="Beats per minute")
    parser.add_argument("--seed", help="Some string")
    args = parser.parse_args()
    if (args.bpm != None and int(args.bpm) <= 0):
        raise argparse.ArgumentTypeError("Bpm must be grater then 0")
    return args

def __hash_code(A):
    return sum([ord(x)*i % 128 for x,i in zip(A, range(1, len(A)))])%128

def main():
    args = __arg_parse()

    md = Melody_Generator(128, 6) # 128 notes in midi
    md.learn(["seeds/1", "seeds/2", "seeds/3", "seeds/4", "seeds/5", "seeds/6", "seeds/7", "seeds/8", "seeds/9", "seeds/morning_moode",
              "seeds/funeral",
              "seeds/moonlight"],
             md.notes_markov_chain)
    md.notes_markov_chain.probability_matrix_normalization()

    md.notes_markov_chain.print_probability_matrix()

    if args.seed is not None:
        starting_point = __hash_code(args.seed)
        if md.check_row_if_zero(starting_point, md.notes_markov_chain) == -1:
            starting_point = Melody_Generator.random_starting_point(md.notes_markov_chain)
    else:
        starting_point = Melody_Generator.random_starting_point(md.notes_markov_chain)

    md.notes_markov_chain.current_note = starting_point

    song_list = []
    song_list.append(Note(0, starting_point, 127, 2))

    next_note = starting_point
    for i in range(1, 128):
        next_note = md.return_next_note()
        song_list.append(Note(i, next_note, 127, random.randint(1, 10)))
                 
    melody = Melody(song_list)

    if not os.path.exists("output"):
        os.makedirs("output")

    save_midi_file(melody.return_midi_array(),
                   "output/" + args.output,
                   int(args.bpm) if args.bpm is not None else 260
    )
