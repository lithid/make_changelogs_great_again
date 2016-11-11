#!/usr/bin/env python2
import sys
import subprocess

NUMBER_ARGS = 2

class Gen:

    def main(self, commit):
        sections = {}
        output = subprocess.check_output(["git", "log", "%s^..HEAD" % commit])
        output = output.splitlines()
        for x in output:
            value = x.strip()
            if value.startswith("#"):
                name = value.split(" ")[0]
                content = value.replace(name, "").strip()

                if name not in sections:
                    sections[name] = []

                bucket = sections[name]
                bucket.append(content)
                sections[name] = bucket

        print "Changelog:\n"
        for something in sections:
            print "### %s" % something.replace("#", "")
            for another in sections[something]:
                print "- %s" % another
            print ""

if __name__ == "__main__":
    if len(sys.argv) != NUMBER_ARGS:
        print "Invalid arguments, needed 1"
    else:
        G = Gen()
        G.main(sys.argv[1])
