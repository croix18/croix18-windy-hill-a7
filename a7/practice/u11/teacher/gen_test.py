#!/usr/bin/env python3
"""The A7 Unit 11 test as data for the teacher page (practice kit teacher_gen.py). python3 gen_test.py [--check]
Ruling 49 (22 Oct 2026): the test is a random set of the practice page, so the paper here is the test's blueprint — the
practice test of a7/build/u11/unit.py — and its forms (Tests A and B, the make-ups) are sets of the page."""
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "kit"))
from teacher_gen import main
main(unit_py="../../../build/u11/unit.py", out="test.js")
