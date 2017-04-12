#!/usr/bin/env python

# Tests for OversizedPancakeFlipper

__author__ = "Krzysztof Kutt"
__copyright__ = "Copyright 2017, Krzysztof Kutt"


import pytest
from codejam_2017.qualification.pancakeflipper.OversizedPancakeFlipper \
    import flip_pancakes


@pytest.mark.parametrize("pancakes_, flipper_, expected", [
    ("---+-++-", 3, 3),
    ("+++++", 4, 0),
    ("-+-+-", 4, "IMPOSSIBLE")
])
def test_flip_pancakes(pancakes_, flipper_, expected):
    assert flip_pancakes(pancakes_, flipper_) == expected


if __name__ == '__main__':
    pass
