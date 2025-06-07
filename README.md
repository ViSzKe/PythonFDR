# PythonFDR v1.1.1

**Copyright (C) 2025  Vilgot Szasz Kero
PythonFDR comes with ABSOLUTELY NO WARRANTY; for details see COPYRIGHT.txt**

## Introduction

This is a free, open-source flight data recorder for Microsoft Flight Simulator written entirely in Python. It uses pysimconnect to fetch data from the simulator, and pygame to read joystick input.

*This is a personal project*, so it is obviously very limited compared to paid services.

## Supported simulators (tested on):

* Microsoft Flight Simulator 2020, 2024

## Usage

A Python environment and all the requirements are included in the package.
Simply run `RUN_PYTHONFDR.bat` or `RUN_LOG_DECODER_PLOTTER.bat`

## Recorded data:

By default, data is fetched and saved with one second intervals. The log is stored in `fdr.log` in project root. The previous logs are deleted every time you run the program.

"AILERON POSITION", # Percent aileron input left/right.
"AILERON TRIM PCT", # The trim position of the ailerons. Zero is fully retracted.
"AILERON LEFT DEFLECTION PCT", # Percent deflection for the left aileron.
"AILERON RIGHT DEFLECTION PCT", # Percent deflection for the right aileron.

"ELEVATOR POSITION", # Percent elevator input deflection.
"ELEVATOR TRIM PCT", # Percent elevator trim.
"ELEVATOR DEFLECTION PCT", # Percent deflection.

## Reviewing the log

The included `Log_Decoder_Plotter` will plot the data on a graph. If you want to use your own tool, the log entry format is below:

### Log entry format:
```
[HHMMSS]:[AILERON POSITION(simvar)]:[AILERON TRIM PCT(simvar)]:[AILERON LEFT DEFLECTION PCT(simvar)]:[AILERON RIGHT DEFLECTION PCT(simvar)]:[ELEVATOR POSITION(simvar)]:[ELEVATOR TRIM PCT(simvar)]:[ELEVATOR DEFLECTION PCT(simvar)]:[JOYSTICK X(input)]:[JOYSTICK Y(input)]
```