#!/usr/bin/env python

from time import sleep

"""
    Print function with flush parameter
    Created by : Emils Bute

    URL : https://www.includehelp.com/python/flush-parameter-in-python-with-print-function.aspx
"""
# output not flushed here
print("Es macos programmet.  ", end='')
print("Lietoju funkciju print.  ", end='')
print("Izmantoju paramentu flush.  ", end='')

sleep(5)
print("Bye!!!")
input("Press <ENTER> to exit.")

