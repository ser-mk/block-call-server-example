from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

filename = "hist-log-prenet.log"

try:
    with open(filename, 'r') as f:  # Open the file in read mode
        lines = f.readlines()  # Read all lines into a list
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    raise "fff"

times = defaultdict(list)
for line in lines:
    parts = line.split(' | ')
    if len(parts) >= 3:
        time_str = parts[2]
        if '/fastcgo' in parts[4]:
            times['fastcgo'].append(float(time_str[:-2]) * 1e+3 if time_str.endswith('ms') else float(time_str[:-2]))
        elif '/cgo' in parts[4]:
            times['cgo'].append(float(time_str[:-2]) * 1e+3 if time_str.endswith('ms') else float(time_str[:-2]) )


for key, value in times.items():
    plt.hist(value, bins=14, alpha=0.5, label=key, range=(0, 8000)
    )


plt.xlabel('Time (us)')
plt.ylabel('Frequency')
plt.title('Histogram of Response Times')
plt.legend()
plt.show()