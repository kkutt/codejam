#!/usr/bin/env python

# Google Code Jam 2017. Round 1B
# Problem B. Stable Neigh-bors
#
# * Problem
# You are lucky enough to own N pet unicorns. Each of your unicorns has
# either one or two of the following kinds of hairs in its mane: red hairs,
# yellow hairs, and blue hairs. The color of a mane depends on exactly which
# sorts of colored hairs it contains:
# - A mane with only one color of hair appears to be that color. For example,
#   a mane with only blue hairs is blue.
# - A mane with red and yellow hairs appears orange.
# - A mane with yellow and blue hairs appears green.
# - A mane with red and blue hairs appears violet.
# You have R, O, Y, G, B, and V unicorns with red, orange, yellow, green,
# blue, and violet manes, respectively.
# You have just built a circular stable with N stalls, arranged in a ring
# such that each stall borders two other stalls. You would like to put exactly
# one of your unicorns in each of these stalls. However, unicorns need to feel
# rare and special, so no unicorn can be next to another unicorn that shares at
# least one of the hair colors in its mane. For example, a unicorn with an
# orange mane cannot be next to a unicorn with a violet mane, since both of
# those manes have red hairs. Similarly, a unicorn with a green mane cannot be
# next to a unicorn with a yellow mane, since both of those have yellow hairs.
# Is it possible to place all of your unicorns? If so, provide any one
# arrangement.
#
# * Input
# The first line of the input gives the number of test cases, T. T test cases
# follow. Each consists of one line with seven integers: N, R, O, Y, G, B,
# and V.
#
# * Output
# For each test case, output one line containing Case #x: y, where x is the
# test case number (starting from 1) and y is IMPOSSIBLE if it is not
# possible to place all the unicorns, or a string of N characters
# representing the placements of unicorns in stalls, starting at a point of
# your choice and reading clockwise around the circle. Use R to represent
# each unicorn with a red mane, O to represent each unicorn with an orange
# mane, and so on with Y, G, B, and V. This arrangement must obey the rules
# described in the statement above.
# If multiple arrangements are possible, you may print any of them.
#
# * Limits
# 1 ≤ T ≤ 100.
# 3 ≤ N ≤ 1000.
# R + O + Y + G + B + V = N.
# 0 ≤ Z for each Z in {R, O, Y, G, B, V}.
# Small dataset: O = G = V = 0.
#                (Each unicorn has only one hair color in its mane.)
# Large dataset: No restrictions beyond the general limits.
#                (Each unicorn may have either one or two hair colors in its
#                mane.)
#
# * Sample
# Input             Output
# 4
# 6 2 0 2 0 2 0     Case #1: RYBRBY
# 3 1 0 2 0 0 0     Case #2: IMPOSSIBLE
# 6 2 0 1 1 2 0     Case #3: YBRGRB
# 4 0 0 2 0 0 2     Case #4: YVYV
# Note that the last two sample cases would not appear in the Small dataset.
# For sample case #1, there are many possible answers; for example, another
# is BYBRYR. Note that BYRYRB would not be a valid answer; remember that the
# stalls form a ring, and the first touches the last!
# In sample case #2, there are only three stalls, and each stall is a
# neighbor of the other two, so the two unicorns with yellow manes would
# have to be neighbors, which is not allowed.
# For sample case #3, note that arranging the unicorns in the same color
# pattern as the Google logo (BRYBGR) would not be valid, since a unicorn
# with a blue mane would be a neighbor of a unicorn with a green mane,
# and both of those manes share blue hairs.
# In sample case #4, no two unicorns with yellow manes can be neighbors,
# and no two unicorns with violet manes can be neighbors.

# FIXME: This solution is not working for the large dataset - it hangs
# somewhere while sorting unicorns...

__author__ = "Krzysztof Kutt"
__copyright__ = "Copyright 2017, Krzysztof Kutt"

import sys
import io
import struct


def are_equal(elem1, elem2):
    if elem1 == elem2:
        return True
    if elem1 in ["O", "G", "V"] and elem2 in ["O", "G", "V"]:
        return True
    elems = []
    for elem_ in [elem1, elem2]:
        if elem_ == "O":
            elems.append("R")
            elems.append("Y")
        elif elem_ == "G":
            elems.append("B")
            elems.append("Y")
        elif elem_ == "V":
            elems.append("B")
            elems.append("R")
        else:
            elems.append(elem_)

    elems.sort()
    for i in range(1, len(elems)):
        if elems[i-1] == elems[i]:
            return True
    return False


def sort_unicorns(sequence_in):
    # convert to list to swap letters in place
    sequence_ = []
    for character in sequence_in:
        sequence_.append(character)

    not_sorted = True
    while not_sorted:
        not_sorted = False
        if are_equal(sequence_[0], sequence_[-1]):
            not_sorted = True
            sequence_[1], sequence_[0] = sequence_[0], sequence_[1]
        for i in range(1, len(sequence_)-1):
            if are_equal(sequence_[i-1], sequence_[i]):
                not_sorted = True
                sequence_[i+1], sequence_[i] = sequence_[i], sequence_[i+1]
        if are_equal(sequence_[-2], sequence_[-1]):
            not_sorted = True
            sequence_[-1], sequence_[0] = sequence_[0], sequence_[-1]
    return "".join(sequence_)


def arrange_unicorns(count, unicorns):
    """ Check if arrangement for the set of unicorns is possible (accordingly
    to the specification)
    
    :param count: number of unicorns
    :param unicorns: list of [R, O, Y, G, B, V]
    :return: arrangement or "IMPOSSIBLE" if it is impossible to do this
    """
    R, O, Y, G, B, V = unicorns

    RR = V + R + O
    YY = O + Y + G
    BB = G + B + V
    if RR > count/2 or YY > count/2 or BB > count/2:
        # if there are more that the half of unicorns in the one color,
        # there is no possibility to arrange them
        return "IMPOSSIBLE"

    sequence = "G" * G + "O" * O + "V" * V + "R" * R + "B" * B + "Y" * Y
    sequence = sort_unicorns(sequence)

    return sequence if True else "IMPOSSIBLE"


if __name__ == '__main__':
    # FIXME Comment this line before sending to Google!
    sys.stdin = io.StringIO("".join(open("sample.in", "r").readlines()))

    t = int(input())  # read a line with a single integer
    for case in range(1, t + 1):
        unicorns_ = [int(s) for s in input().split(" ")]
        print("Case #{}: {}".format(case, arrange_unicorns(unicorns_[0],
                                                           unicorns_[1:])))
