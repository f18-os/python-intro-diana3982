#!/usr/bin/env python3

import sys # command line arguments
import re # to tokenize
import os # to call on exe, for, wait, redir, etc
#import exe, fork, wait, redir # code provided


if len(sys.argv) is not 1: #this is a check to make sure user is running program correctly
    print("Correct usage: shell.py")
    exit()

def shell_script(usrin):


while True:
    line = sys.stdin.readlines()
    print("what was read %s" % line)
    for cmd in line:
        print("-------------------------------------")
        cmd.replace("\n", "")
        os.system(cmd)
        #os.system()
        break;
