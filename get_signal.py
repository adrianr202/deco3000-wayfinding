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
import statistics

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]  # Use the first wireless interface (you can select a different one if needed)
name = iface.name()  # Get the interface name

data_time = []
data_distance = []

i = 0
while i != 20:
    i += 1

    iface.scan()  # Scan for networks
    time.sleep(4)  # Wait a bit for the scan to finish
    scan_results = iface.scan_results()  # Get scan results
    # Create a dictionary to store unique networks based on BSSID
    unique_networks = {}
    for result in scan_results:
        bssid = result.bssid
        ssid = result.ssid
        if bssid not in unique_networks and ssid == "Vince's Phone": # Only add the network if it is not already in the dictionary and if it is UniSydney
            unique_networks[bssid] = result
    # Sort the unique results by RSSI (signal strength) in descending order
    sorted_results = sorted(unique_networks.values(), key=lambda x: x.signal, reverse=True)

    # Print the information for the nth strongest networks
    for network in sorted_results:
        f = network.freq / 1000 # Convert frequency from MHz to GHz
        s = abs(network.signal) # Converts negative RSSI values to positive

        # Calculate the estimated distance by using Log-Distance Path Model
        # https://en.wikipedia.org/wiki/Log-distance_path_loss_model
        d = 10 ** ((s - 45) / (10 * 3)) 
        d = round(d,2) # Convert the distance to centimeters and round to 2 decimal places

        data_time.append(s)
        data_distance.append(d)
        # Print the information for the network
        print(f"SSID: {network.ssid}")
        print(f"BSSID (MAC Address): {network.bssid}")
        print(f"RSSI (Signal Strength): {s} dBm")
        print(f"Estimated Distance: {d}m")
        print("----------------------------------")

ax = plt.gca()
ax.set_xlim(0, 10)  # Set minimum and maximum X-axis values
ax.set_ylim(0, 2)
plt.axhline(y = 1, color = 'r', linestyle = '-') 
plt.axhline(y = statistics.mean(data_distance), color = 'b', linestyle = '-') 
plt.scatter(data_time, data_distance)
plt.xlabel("Iterations")
plt.ylabel("Distance (m)")
plt.show() 