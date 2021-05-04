#!/usr/bin/python3
def multiple_returns(sentence):
    i = None
    size = len(sentence)
    if size > 0:
        i = sentence[0]
    return size, i
