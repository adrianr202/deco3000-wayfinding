# Required libraries: 
#   pywifi
#   comtype
#   math
#   matplotlib
#   numpy

import pywifi
import time
from pywifi import const
from math import log10
import matplotlib.pyplot as plt
import numpy as np

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]  # Use the first wireless interface (you can select a different one if needed)
name = iface.name()  # Get the interface name

#i = 0

#Iterates the code over a 60 second period
#while i != 30:
    #i += 1

iface.scan()  # Scan for networks
time.sleep(2)  # Wait a bit for the scan to finish
scan_results = iface.scan_results()  # Get scan results
# Create a dictionary to store unique networks based on BSSID
unique_networks = {}
for result in scan_results:
    bssid = result.bssid
    ssid = result.ssid
    if bssid not in unique_networks and ssid == "UniSydney": # Only add the network if it is not already in the dictionary and if it is UniSydney
        unique_networks[bssid] = result
# Sort the unique results by RSSI (signal strength) in descending order
sorted_results = sorted(unique_networks.values(), key=lambda x: x.signal, reverse=True)
# Free-Space Path Loss adapted avarage constant for home WiFI routers and following units
# Taken from: https://gist.github.com/cryptolok/516471ce35a9851197b204853c6de080
FSPL = 27.55 
# Print the information for the nth strongest networks
for network in sorted_results:
    f = network.freq / 1000
    s = abs(network.signal) # Converts negative RSSI values to positive
    d = 10 ** ((s - 45) / (10 * 3)) # Calculate the estimated distance
    d = round(d,2) # Convert the distance to centimeters and round to 2 decimal places
    #print(f"SSID: {network.ssid}")
    print(f"BSSID (MAC Address): {network.bssid}")
    print(f"RSSI (Signal Strength): {s} dBm")
    #print(f"Frequency: {f} Mhz")
    print(f"Estimated Distance: {d}m")
    print("----------------------------------")