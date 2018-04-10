#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 22:10:30 2018

@author: priyanka.v.bhalekar@gmail.com

Parse '.math' file.
"""


# START and END of each code block
BLOCKS = {
    'variables': ['VARS:', 'START:'],
    'statements': ['START:', 'END:']
}

def parse(text):
    """Parse text from .math file.

    Read blocks and prepare a list of instructions.

    Arguments:
        text (str): Text from .math file.

    Returns:
        Parsed text - List of all arithmetic instructions.
    """
    parsed_text = []

    # Parse VAR: block.
    variables = _parse_block(text, *BLOCKS.get('variables'))
    parsed_text.extend(variables)

    # Parse statement block.
    statements = _parse_block(text, *BLOCKS.get('statements'))

    parsed_text.extend(statements)

    return parsed_text

def _parse_block(text, start_text, end_text):
    """Parse block.

    Arguments:
        text (str): Text from .math file.
        start_text (str): Block start.
        end_text (str): Block end.

    Returns:
        List of instructions from single block.
    """
    # Find START and END index of block.
    start_index = text.find(start_text) + len(start_text)
    end_index = text.find(end_text)

    # Extract block from text.
    block = text[start_index : end_index]

    # Prepare a list of instruction.
    block = block.split('\n')

    # Remove spaces around instructions.
    block = [stmt.strip(' ') for stmt in block]

    # Remove empty lines.
    block = [stmt for stmt in block if stmt != '']

    return block
