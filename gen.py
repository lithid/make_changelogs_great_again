#!/usr/bin/env python2
import sys
import subprocess

NUMBER_ARGS = 2

class Gen:

    def main(self, commit):
        output = subprocess.check_output(["git", "log", "%s^..HEAD" % commit])
        output = output.splitlines()
        for x in output:
            x = x.strip()
            if x.startswith("#"):
                print x

if __name__ == "__main__":
    if len(sys.argv) != NUMBER_ARGS:
        print "Invalid arguments, needed 1"
    else:
        G = Gen()
        G.main(sys.argv[1])
