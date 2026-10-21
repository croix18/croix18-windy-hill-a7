#!/usr/bin/env python3
"""The real A7 Unit 3 test (one form) as data for the teacher page (practice kit teacher_gen.py). python3 gen_test.py [--check]"""
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "kit"))
from teacher_gen import main
main(unit_py="../../../build/u3/unit.py", out="test.js")
