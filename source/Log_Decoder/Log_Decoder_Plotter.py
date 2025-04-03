# This file is part of PythonFDR: Free flight data recorder for Microsoft Flight Simulator written entirely in Python
# Copyright (C) 2025  Vilgot Szasz Kero
# PythonFDR comes with ABSOLUTELY NO WARRANTY; for details see COPYRIGHT.txt


import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Configuration for variables
logged_data = [
    "AILERON COMMANDED DEFLECTION",        # parts[1]
    "AILERON TRIM PCT",        # parts[2]
    "AILERON LEFT DEFLECTION PCT",  # parts[3]
    "AILERON RIGHT DEFLECTION PCT", # parts[4]
    "ELEVATOR COMMANDED DEFLECTION",       # parts[5]
    "ELEVATOR TRIM PCT",       # parts[6]
    "ELEVATOR DEFLECTION PCT", # parts[7]
    "JOYSTICK X",   # parts[8]
    "JOYSTICK Y",   # parts[9]
]

# Parse logfile
timestamps = []
data = {var: [] for var in logged_data}

with open('fdr.log') as f:
    for line in f:
        parts = line.strip().split(':')
        dt = datetime.strptime(parts[0], "%H%M%S")
        timestamps.append(dt)
        
        # Map parts[1-7] to corresponding variables
        for i, var in enumerate(logged_data, start=1):
            data[var].append(float(parts[i]))

# Create two separate figures for ailerons and elevators
fig_ailerons, ax_ailerons = plt.subplots(figsize=(14, 7))
fig_elevators, ax_elevators = plt.subplots(figsize=(14, 7))

# Plot ailerons on one graph
aileron_vars = [
    "JOYSTICK X",
    "AILERON COMMANDED DEFLECTION",
    "AILERON TRIM PCT",
    "AILERON LEFT DEFLECTION PCT",
    "AILERON RIGHT DEFLECTION PCT"
]
line_styles = ['-', '-', ':', '--', '--']
colors = ['black', 'blue', 'orange', 'red', 'green']

for var, style, color in zip(aileron_vars, line_styles, colors):
    ax_ailerons.plot(timestamps, data[var], linestyle=style, color=color, label=var)

ax_ailerons.set_title('Aileron Control Surface Positions', fontsize=14)
ax_ailerons.set_xlabel('Timestamp (HH:MM:SS)', fontsize=12)
ax_ailerons.set_ylabel('Deflection Percentage (%)', fontsize=12)
ax_ailerons.legend(loc='upper left')
ax_ailerons.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
plt.setp(ax_ailerons.xaxis.get_majorticklabels(), rotation=45)

# Plot elevators on another graph
elevator_vars = [
    "JOYSTICK Y",
    "ELEVATOR COMMANDED DEFLECTION",
    "ELEVATOR TRIM PCT",
    "ELEVATOR DEFLECTION PCT"
]

for var, style, color in zip(elevator_vars, line_styles, colors):
    ax_elevators.plot(timestamps, data[var], linestyle=style, color=color, label=var)

ax_elevators.set_title('Elevator Control Surface Positions', fontsize=14)
ax_elevators.set_xlabel('Timestamp (HH:MM:SS)', fontsize=12)
ax_elevators.set_ylabel('Deflection Percentage (%)', fontsize=12)
ax_elevators.legend(loc='upper left')
ax_elevators.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
plt.setp(ax_elevators.xaxis.get_majorticklabels(), rotation=45)

# Adjust layout and show both plots
fig_ailerons.tight_layout()
fig_elevators.tight_layout()
plt.show()
