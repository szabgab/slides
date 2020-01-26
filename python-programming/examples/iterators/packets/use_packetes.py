import sys
from packets import Packets

if len(sys.argv) < 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

for packet in Packets(sys.argv[1]):
    print(packet)
