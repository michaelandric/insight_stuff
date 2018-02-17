#!/usr/bin/env python3

import pytest
from listSorting import getOutputString

def test_strings():
    assert getOutputString("20 cat bi?rd 12 do@g") == "12 bird cat 20 dog"
    assert getOutputString("20 bat bi?rd 12 do@g") == "12 bat bird 20 dog"
    assert getOutputString("-60 10") == "-60 10"
    assert getOutputString("10 -60") == "-60 10"
    assert getOutputString("1-0 -60") == "-60 10"
    assert getOutputString("1-0 -60 c!a!t") == "-60 10 cat"
    assert getOutputString("-999999 999 0 -999 999999") == "-999999 -999 0 999 999999"
    assert getOutputString("") == ""



