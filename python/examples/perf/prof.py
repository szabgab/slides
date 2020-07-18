import count_characters as count
import cProfile
import sys

cProfile.run('chars, counter = count.count_in(sys.argv[1:])')
