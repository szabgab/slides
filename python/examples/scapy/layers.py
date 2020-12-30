import scapy.all as scapy
import scapy.layers as layers
print(scapy.LayersList().layers()) # []

import scapy.config as config
print(config.LayersList().layers()) # []

print(dir(layers))