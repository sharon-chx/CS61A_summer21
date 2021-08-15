import re


def roman_numerals(text):
    """
    Finds any string of letters that could be a Roman numeral
    (made up of the letters I, V, X, L, C, D, M).

    >>> roman_numerals("Sir Richard IIV, can you tell Richard VI that Richard IV is on the phone?")
    ['IIV', 'VI', 'IV']
    >>> roman_numerals("My TODOs: I. Groceries II. Learn how to count in Roman IV. Profit")
    ['I', 'II', 'IV']
    >>> roman_numerals("I. Act 1 II. Act 2 III. Act 3 IV. Act 4 V. Act 5")
    ['I', 'II', 'III', 'IV', 'V']
    >>> roman_numerals("Let's play Civ VII")
    ['VII']
    >>> roman_numerals("i love vi so much more than emacs.")
    []
    >>> roman_numerals("she loves ALL editors equally.")
    []
    """
    pattern = r"\b([IVXLCDM]+)\b"
    return re.findall(pattern, text)


import re


def calculator_ops(calc_str):
    """
    Finds expressions from the Calculator language that have two
    numeric operands and returns the expression without the parentheses.

    >>> calculator_ops("(* 2 4)")
    ['* 2 4']
    >>> calculator_ops("(+ (* 3 (+ (* 2 4) (+ 3 5))) (+ (- 10 7) 6))")
    ['* 2 4', '+ 3 5', '- 10 7']
    >>> calculator_ops("(* 2)")
    []
    """
    pattern = r"[-/+\/*] [0-9]* [0-9]*\b"   #used / for + and * since they are regular expression itself
    return re.findall(pattern, calc_str)
