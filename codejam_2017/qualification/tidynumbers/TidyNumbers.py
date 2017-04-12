#!/usr/bin/env python

# Google Code Jam 2017. Qualification Round
# Problem B. Tidy Numbers
#
# * Problem
# Tatiana likes to keep things tidy. Her toys are sorted from smallest to
# largest, her pencils are sorted from shortest to longest and her computers
# from oldest to newest.
# One day, when practicing her counting skills, she noticed that some
# integers, when written in base 10 with no leading zeroes, have their digits
# sorted in non-decreasing order. Some examples of this are 8, 123, 555, and
# 224488. She decided to call these numbers tidy. Numbers that do not have
# this property, like 20, 321, 495 and 999990, are not tidy.
# She just finished counting all positive integers in ascending order from
# 1 to N. What was the last tidy number she counted?
#
# * Input
# The first line of the input gives the number of test cases, T. T lines
# follow. Each line describes a test case with a single integer N, the last
# number counted by Tatiana.
# * Output
# For each test case, output one line containing Case #x: y, where x is the
# test case number (starting from 1) and y is the last tidy number counted by
# Tatiana.
#
# * Limits
# 1 ≤ T ≤ 100.
# Small dataset: 1 ≤ N ≤ 1000.
# Large dataset: 1 ≤ N ≤ 1018.
#
# * Sample
# Input               Output
# 4
# 132                 Case #1: 129
# 1000                Case #2: 999
# 7                   Case #3: 7
# 111111111111111110  Case #4: 99999999999999999
# Note that the last sample case would not appear in the Small dataset.

__author__ = "Krzysztof Kutt"
__copyright__ = "Copyright 2017, Krzysztof Kutt"

import sys
import io


def find_tidy_number(number):
    changes = True  # if something was changed during this iteration
    while changes:
        changes = False
        inconsistency_index = -1
        # find the first inconsistency:
        for i in range(1, len(number)):
            if int(number[i - 1]) > int(number[i]):
                changes = True
                inconsistency_index = i
                break
        if inconsistency_index != -1:
            # prepare new string with changes from inconsistency index
            new_number = number[0:i-1]
            # change the digit before the inconsistency to one less
            new_number += chr(ord(number[i - 1]) - 1)
            # and all further digits to 9
            new_number += ('9' * (len(number)-inconsistency_index))
            number = new_number
    # convert to int to remove zeros at the beginning
    return int(number)


if __name__ == '__main__':
    # FIXME Comment this line before sending to Google!
    sys.stdin = io.StringIO("".join(open("sample.in", "r").readlines()))

    t = int(input())  # read a line with a single integer
    for case in range(1, t + 1):
        print("Case #{}: {}".format(case, find_tidy_number(input())))
