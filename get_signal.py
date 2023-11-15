import pywifi
import time

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]  # Use the first wireless interface AKA your phone, only needs to be run once

iface.scan()  # Scan for networks
time.sleep(3)  # Wait 3 seconds for the scan to finish
scan_results = iface.scan_results()  # Get scan results

# Create a dictionary to store unique networks based on BSSID
unique_network = {}
for result in scan_results:
    bssid = result.bssid
    ssid = result.ssid
    unique_network[bssid] = result            

# Sort the unique results by RSSI (signal strength) in descending order
sorted_results = sorted(unique_network.values(), key=lambda x: x.signal, reverse=True)

# Get the strongest router, or the first result from sorted_results
strongest_node = sorted_results[0]

# Print the information for the strongest node if it exists, else return "no connection"
s = abs(strongest_node.signal) # Converts negative RSSI values to positive

# Calculate the estimated distance by reverse engineering the Log-Distance Path Model
# https://en.wikipedia.org/wiki/Log-distance_path_loss_model
d = 10 ** ((s - 45) / (10 * 3)) 
d = round(d,2) # Convert the distance to meters and round to 2 decimal places