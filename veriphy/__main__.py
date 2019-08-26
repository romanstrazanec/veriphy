#!/usr/bin/python3
from argparse import ArgumentParser
from hashlib import new as newhash, algorithms_guaranteed
from veriphy._resources import *


# parse arguments
parser = ArgumentParser(prog=PROG, description=DESC)
parser.add_argument(ARG_FILE, help=HELP_FILE)
signature_input_group = parser.add_mutually_exclusive_group()
signature_input_group.add_argument(ARG_I, ARG_INPUT, help=HELP_INPT)
signature_input_group.add_argument(ARG_S, ARG_SIGN, help=HELP_SIGN)
parser.add_argument(ARG_A, help=HELP_FUNC, choices=algorithms_guaranteed)
args = parser.parse_args()

# prompt algorithm
if not args[ARG_A]:
    choice_len = len(algorithms_guaranteed) + 1
    chosen_algorithm = None

    # ask for algorithm
    while not chosen_algorithm:
        # print available algorithms with corresponding numbers beginning with 1
        for i, algorithm in enumerate(algorithms_guaranteed, start=1):
            print(f'{i:02}> {algorithm}')

        v = input(MSG_SEL_ALG)
        if v == '':
            exit(MSG_NO_ALG)

        try:
            v = int(v)
            if 0 < v < choice_len:
                chosen_algorithm = list(algorithms_guaranteed)[v - 1]
        except ValueError:  # type(v) is str
            if v in algorithms_guaranteed:
                chosen_algorithm = v
    setattr(args, 'f', chosen_algorithm)


# prompt signature
if args[ARG_SIGN]:
    signature = args[ARG_SIGN]
elif args[ARG_INPUT]:
    with open(args[ARG_INPUT]) as f:
        signature = f.read().replace('\n', '')
else:
    signature = input(MSG_SIGN)

# verify
with open(args[ARG_FILE], 'rb') as f:
    h = newhash(args[ARG_A])
    h.update(f.read())

    print(MSG_MATCH if h.hexdigest() == signature else MSG_NO_MATCH)
