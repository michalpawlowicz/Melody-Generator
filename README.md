# Melody-Generator

[![build](https://img.shields.io/travis/rust-lang/rust.svg)](https://github.com/michalpawlowicz/Melody-Generator)

## Overview
This is implementation of Markov Chain that generates noncomplicated melody in MIDI format, based on some exemplary input.

## What is Markov Chain?
Marcov chain is mathematical system which provides as with probability of transition for one state to another. It can be characterize as memoryless proces because the next state depends only on current state and not on events which leads us to that state. Read more: [Wikipedia](https://en.wikipedia.org/wiki/Markov_chain)

## Usage

> Git clone
```
git clone https://github.com/michalpawlowicz/Melody-Generator.git
```
> or download and unpack the zip file. 
```
cd Melody-Generator
```
> Running
```
python run.py output_file_name [optional arguments]
```
> Run ```python run.py -h ``` for more help.

## Requirements
* Python 3.6
* [miditime](https://github.com/cirlabs/miditime)
