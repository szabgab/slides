import slow
import os
import hotshot, hotshot.stats

prof = hotshot.Profile("slow.prof")
prof.runcall(slow.main, 1000)
prof.close()
stats = hotshot.stats.load("slow.prof")
stats.strip_dirs()
stats.sort_stats('time', 'calls')
stats.print_stats(20)

os.remove("slow.prof")
