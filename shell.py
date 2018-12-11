#!/usr/bin/env python3

import sys # command line arguments
import re # to tokenize
import os # to call on exe, for, wait, redir, etc
#import exe, fork, wait, redir # code provided


if len(sys.argv) is not 1: #this is a check to make sure user is running program correctly
    print("Correct usage: shell.py")
    exit()


while True:
    for cmd in sys.stdin:
        
        line = sys.stdin.readlines()
        print("what was read %s" % line)
        print("-------------------------------------")
        cmd.replace("\n", "")
        os.system(line)
        #os.system()
        break;
