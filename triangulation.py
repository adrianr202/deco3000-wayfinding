import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
import numpy as np
import matplotlib
import math

# Font change to Arial cause it looks better
matplotlib.rcParams['font.family'] = 'Arial'

# Map image, for overlay on graph (1421 x 1295 px)
image = mpimg.imread('wilko_level2.png')

# Estimated measurement of Wilkinson building via Google Earth, in meters
x_real = 68.88
y_real = 58.90

# Mapping image size to graph coordinates values (x = 142, y = 130)
xmin = 0
xmax = 142
ymin = 0
ymax = 130

# scaling factor between real measurements and coordinate values
x_scaling_factor = x_real / xmax
y_scaling_factor = y_real / ymax

# [71, 93] is coordinate of Starting Location
x_start = 71
y_start = 93
plt.scatter(x_start, y_start,
            marker='o',
            color='blue',
            label='Start')

# [20, 77] is coordinate of Target Location
x_target = 20
y_target = 77
plt.scatter(x_target, y_target,
            marker='o',
            color='red',
            label='Target')

# Plot the routers for triangulation

router_1 = { 
    'bssid': '48:91:d5:f6:ca:2d:', 
    'x': 29, 
    'y': 79.5,
}

router_2 = {
    'bssid': '6c:d6:e3:00:20:ad:',
    'x': 37.5,
    'y': 65.5,
}

router_3 = {
    'bssid': '6c:d6:e3:01:c3:2d:',
    'x': 24,
    'y': 46,
}

router_list = [router_1, router_2, router_3]

# For every router, annotate the BSSID (MAC Address)
for router in router_list:
    x = router.get('x')
    y = router.get('y')
    bssid = router.get('bssid')

    plt.scatter(x, y,
            color='green',
            )
    
    #distance on the graph with Euclidean distance formula: distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    d_model_target = math.sqrt((x_target - x)**2 + (y_target - y)**2) # Distance in Units
    d_real_target = d_model_target * x_scaling_factor # Distance in Meters
    d_real_target = round(d_real_target, 2) 
    #estimated distance and angle between router and target location
    plt.annotate('', (x, y), (x_target, y_target), arrowprops=dict(arrowstyle='<->', lw=1, color='black'))
    plt.annotate(f'{d_real_target}m', ((x + x_target)/2, (y + y_target)/2), 
                 ha='center', 
                 va='bottom', 
                 fontsize=6)

    #estimated distance and angle between router and starting location
    d_model_start = math.sqrt((x_start - x)**2 + (y_start - y)**2) # Distance in Units
    d_real_start = d_model_start * x_scaling_factor # Distance in Meters
    d_real_start = round(d_real_start, 2) 
    plt.annotate('', (x, y), (x_start, y_start), arrowprops=dict(arrowstyle='<->', lw=1, color='black'))
    plt.annotate(f'{d_real_start}m', ((x + x_start)/2, (y + y_start)/2), 
                 ha='center', 
                 va='bottom', 
                 fontsize=6)
    plt.annotate(bssid, (x, y), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=6, color='green')



# Grid Options
plt.grid(which='both', linestyle='-', linewidth='0.15', color='gray')
plt.minorticks_on()

# Plotting the image, alpha = transparency
plt.imshow(image, extent=[xmin, xmax, ymin, ymax], alpha=0.5)

plt.legend(loc='lower right')
plt.show()

# Your array of numbers
#y = [56, 59, 60, 64, 64, 66, 68, 69, 70, 70, 72, 72, 75, 76, 77, 77, 79, 79, 80, 81, 82, 83, 83, 84, 84, 84, 87]
#x = [2.33, 2.93, 3.16, 4.3, 4.3, 5.01, 5.84, 6.31, 6.81, 6.81, 7.94, 7.94, 10.0, 10.8, 11.66, 11.66, 13.59, 13.59, 14.68, 15.85, 17.11, 18.48, 18.48, 19.95, 19.95, 19.95, 25.12]

# Create a scatter plotc
#plt.scatter(x, y, marker='o', color='blue')
#
# Set the labels for the axes
#plt.xlabel('Est. Distance (m)')
#plt.ylabel('Signal Strength (Dbm)')
#
# Display the plot
# plt.show()
