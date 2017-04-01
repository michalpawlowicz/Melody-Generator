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
    args = parser.parse_args()
    if (args.bpm != None and int(args.bpm) <= 0):
        raise argparse.ArgumentTypeError("Bpm must be grater then 0")
    return args
    
def main():
    args = __arg_parse()
    md = Melody_Generator(128, 6) # 128 notes in midi
    md.learn(["seeds/morning_moode",
              "seeds/funeral",
              "seeds/moonlight"],
             md.notes_markov_chain)
    md.notes_markov_chain.probability_matrix_normalization()

    md.notes_markov_chain.print_probability_matrix()

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
                   int(args.bpm) if args.bpm != None else 250
    )
