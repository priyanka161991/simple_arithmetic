#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 22:50:05 2018

@author: priyanka.v.bhalekar@gmail.com

Perform math operations as instructed.
"""
from functools import reduce


class Arithmetic():
    """Class to perform arithmetic operations"""

    # Class variable - list of keywords
    keywords = ['ADD', 'MUL', 'DIV', 'SUB', 'STORE']

    def __init__(self, instructions):
        """Initialize instance variables.

        Arguments:
            instructions (list): List of arithmetic instructions to run.
        """
        self.instructions = instructions
        self.variables = {}
        self.results = {}
        self.out_variables = {}

    def _input(self, instruction):
        """Ask user to input valid integer values. Save these values
        in variables instance variable.

        Arguments:
            instruction (str): Single IN instruction.

        Raises:
            ValueError in case user inputs wrong values.
        """
        while True:
            try:
                value = int(input("Please enter integer value: "))
            except ValueError:
                print("Invalid input.")
                continue
            else:
                _, variable_name = instruction.split(' ')
                self.variables[variable_name] = value
                break

    def _output(self, instruction):
        """Save out variables in out_variables.

        Arguments:
            instruction (str): Single OUT instruction.
        """
        _, variable_name = instruction.split(' ')
        self.out_variables[variable_name] = self.results.get(
            variable_name,
            'compute'
        )

    def _show(self, instruction):
        """Display result on console.

        Arguments:
            instruction (str): Single STORE instruction.
        """
        _, variable_name = instruction.split(' ')

        output = '{} = {}'.format(variable_name, self.results.get(variable_name))

        print(output)

    def _compute(self, operation, values, result):
        """Compute result.

        Arguments:
            operation (str): Operation to be performed of the form 'ADD' or 'SUB'.
            values (list): List of values to perform operation on.
            result (str): Variable name to STORE result.

        Raises:
            ZeroDivisionError - if try to divide number by 0.
            NotImplementedError - If try to perform operation other than 'ADD', 'SUB,
               'MUL' or 'DIV'
        """
        if operation == 'ADD':
            self.results[result] = sum(values)
        elif operation == 'MUL':
            self.results[result] = reduce(lambda x, y: x*y, values)
        elif operation == 'DIV':
            try:
                self.results[result] = values[0] / values[1]
            except ZeroDivisionError:
                self.results[result] = 'Error ZeroDivisionError'
                # Re-raise ZeroDivisionError
                raise
        elif operation == 'SUB':
            self.results[result] = values[0] - values[1]
        else:
            # Raise NotImplementedError as only ADD, SUB, MUL and DIV are supported.
            raise NotImplementedError('This operation is not currently supported.')

    def run(self):
        """Run set instructions one by one."""
        for instruction in self.instructions:
            if instruction.startswith('IN'): # Run IN instruction
                self._input(instruction)
            elif instruction.startswith('OUT'):
                pass
            elif instruction.startswith('SHOW'): # Run SHOW instruction
                self._show(instruction)
            else: # Run arithmetic instruction.

                # Separate arithmetic operation and STORE instruction.
                operation, result = instruction.split('STORE')

                # Look of $var in operation
                variables = [var.strip('$') for var in operation.split(' ') if var.startswith('$')]
                # Find values of all the $var
                values = [self.variables.get(variable) for variable in variables]

                # Separate arithmetic operation from $var
                operation = operation.split(' ')[0]

                # Result variable
                result = result.split(' ')[1]

                # Do arithmetic
                self._compute(operation, values, result)
