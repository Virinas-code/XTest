#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
XTest Output.

Output for XTest.
"""
from xtest.colors import GREEN, YELLOW, RED, RESET, BOLD, RESET_COLOR


def sprint(string):
    """Title formater."""
    string = (" " + string + " ").center(20)
    print(string.center(40, "*"))


def test(description):
    """Print test description."""
    print("[      ]", description, end="\r", flush=True)


def test_done(description):
    """Print done test description."""
    print("[  " + GREEN + "OK" + RESET + "  ]", description)


def test_partial(description):
    """Print errored test description."""
    print("[ " + YELLOW + "PART" + RESET + " ]", description)


def test_error(description):
    """Print partial test description."""
    print("[  " + RED + "NO" + RESET + "  ]", description)


def error(description):
    """Print error."""
    print(BOLD + RED + "ERROR" + RESET_COLOR + ":" + RESET, description)


def warning(description):
    """Print warning."""
    print(BOLD + YELLOW + "WARNING" + RESET_COLOR + ":" + RESET, description)
