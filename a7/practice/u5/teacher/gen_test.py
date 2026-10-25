#!/usr/bin/env python3
"""The real A7 Unit 5 test (Forms A and B) as data for the teacher page (practice kit teacher_gen.py). python3 gen_test.py [--check]
Unit 5 was built before ruling 49: its test is the printed Form A and Form B of a7/build/u5/unit.py (Thu 5 Nov 2026), and the
student page is practice for them (ruling 55)."""
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "kit"))
from teacher_gen import main
main(unit_py="../../../build/u5/unit.py", out="test.js")
