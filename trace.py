#!/usr/bin/env python3
import traceback
from ipdb import set_trace


def f_eins(eins):
    print("eins", eins)
    traceback.print_stack()


def zwei(eins, zwei):
    f_eins(eins)
    print("eins", eins, zwei)


zwei("yea loser", "lets go")


