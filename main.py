#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 22:05:08 2018

@author: priyanka.v.bhalekar@gmail.com

Main module to parse .math files and perform mathematical operations as instructed.
"""
from engine.math_engine import Arithmetic
from engine.parser import parse


FILE_NAME = 'operations.math'

def main():
    """ Main """
    # Read .math file.
    with open(FILE_NAME, 'r') as file_handle:
        text = file_handle.read()

    # Parse text from the .math file.
    instructions = parse(text)

    # Run set of instructions.
    math_operations = Arithmetic(instructions)
    math_operations.run()


if __name__ == "__main__":
    main()
