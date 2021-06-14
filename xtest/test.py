#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
XTest Test.

Test functions for XTest.
"""
import xtest.output as out

class Test:
    def __init__(self, target, description=None, *, syntax=False):
        if type(target) not in (list, tuple):
            target = [target]
        if not description:
            lst = []
            for targ in target:
                lst.append(targ.__name__)
            description = "Testing " + ", ".join(lst)
        self.target = target
        self.description = description
        self.syntax = syntax
        self.results = [len(target), 0, 0]    # Total, passed, failed
        self.warnings = list()
    
    def run_std(self):
        for test in self.target:
            try:
                test()
                self.results[1] += 1
            except Exception as e:
                self.results[2] += 1
                self.warnings.append((test.__name__, type(e).__name__ + ": " + str(e)))
    
    def print_warnings(self):
        for warning in self.warnings:
            out.warning("Test \"" + warning[0] + "\" failed : " + warning[1])


def make_test(test):
    out.test(test.description)
    test.run_std()
    if test.results[0] != test.results[1]:
        if test.results[1] == 0:
            out.test_error(test.description)
            out.error("Test \"" + test.description + "\" failed")
            return False
        else:
            out.test_partial(test.description)
            test.print_warnings()
    else:
        out.test_done(test.description)
    return True


def make_tests(*args):
    tests = args
    for test in tests:
        if not make_test(test) and test.syntax:
            out.error("Syntaxic test failed")
            break