
"""
Best source ever
"""

import sys

with open(sys.argv[1], 'w') as f:
    f.write("Hi, I'm a file generated by %s.\n" % sys.executable)
