#!/usr/bin/python
import sys
import subprocess
import time

NUMBER_ARGS = 5

class Gen:

    def main(self, kind, commit, version, build, show_author):
        sections = {}

        command_value = ""
        if kind == "-c" or kind == "--commit":
            command_value = "%s^..HEAD" % commit
            output = subprocess.check_output(["git", "log", "%s^..HEAD" % commit])
        elif kind == "-t" or kind == "--tags":
            item_split_alpha = commit.split(",")[0]
            item_split_bravo = commit.split(",")[1]
            command_value = "%s..%s" % (item_split_alpha, item_split_bravo)

        output = subprocess.check_output(["git", "log", command_value])
        author = ""
        for x in output.splitlines():
            value = x.strip()

            if value.startswith("Author:"):
                author = "(%s)" % value.replace("Author:", "").strip()

            if value.startswith("#"):
                name = value.split(" ")[0]
                content = value.replace(name, "").strip()

                if name not in sections:
                    sections[name] = []

                bucket = sections[name]
                if show_author:
                    bucket.append("%s %s" % (content, author))
                else:
                    bucket.append(content)

                sections[name] = bucket

        print "## %s (%s) - %s" % (version, build, time.strftime("%d-%m-%Y"))
        for something in sections:
            print "### %s" % something.replace("#", "")
            for another in sections[something]:
                print "- %s" % another
            print ""

if __name__ == "__main__":
    number_of_args = len(sys.argv)
    if number_of_args < NUMBER_ARGS:
        arg_string = "argument"
        if number_of_args != 2:
            arg_string = "arguments"
        print "Invalid arguments, %d %s won't cut it" % ((number_of_args - 1), arg_string)
        print "-c   --commit        Use commit"
        print "-t   --tags          Use tags"
        print "-a   --author        Show author on commits"
        print "Example: gen.py -c 06141946 0.0.1 001"
        print "Example: gen.py -t v0.0.1,v0.0.2 0.0.2 002"
    else:
        G = Gen()
        if len(sys.argv) == 6:
            if sys.argv[5] == "-a" or sys.argv[5] == "--author":
                G.main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], True)
        else:
            G.main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], False)
