# -*- coding: cp1251 -*-
import os
import numpy as np

import pprint


def main():
    matching = {}
    with open(rf"{os.getcwd()}\list_for_SecretSanta.txt", "r", encoding="utf-8") as f:
        string = f.readline().strip()

    list_participants_main = string.split(", ")

    for human in list_participants_main:
        list_participants_minor = list_participants_main.copy()
        # only one Santa for each person is allowed
        list_participants_minor = list(
            set(list_participants_minor) - set(matching.values())
        )
        try:
            list_participants_minor.remove(human)
        except ValueError:
            pass
        # human cannot be Santa for himself
        matched_human = np.random.choice(list_participants_minor)
        matching[human] = matched_human
        list_participants_minor.remove(matched_human)

    pprint.pprint(matching, sort_dicts=True)


if __name__ == "__main__":
    main()
