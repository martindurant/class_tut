"""Module doc

This does good stuff
"""

mod_var = True
mod_list = [True]


def is_it():
    return mod_var


def dont_it():
    mod_list[0] = not mod_list[0]
    if mod_var:
        mod_var -= 1
