# This file is part of PythonFDR: Free flight data recorder for Microsoft Flight Simulator written entirely in Python
# Copyright (C) 2025  Vilgot Szasz Kero
# PythonFDR comes with ABSOLUTELY NO WARRANTY; for details see COPYRIGHT.txt


from simconnect import SimConnect
sc = SimConnect()

import os
from datetime import datetime, timezone
from time import sleep

import pygame
os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1" # Allows joystick detection when the program is not in focus
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

log_entry_counter = 0


simvars_pct = [
    "AILERON POSITION", # Percent aileron input left/right.
    "AILERON TRIM PCT", # The trim position of the ailerons. Zero is fully retracted.
    "AILERON LEFT DEFLECTION PCT", # Percent deflection for the left aileron.
    "AILERON RIGHT DEFLECTION PCT", # Percent deflection for the right aileron.

    "ELEVATOR POSITION", # Percent elevator input deflection.
    "ELEVATOR TRIM PCT", # Percent elevator trim.
    "ELEVATOR DEFLECTION PCT", # Percent deflection.
]


def license_notice():
    version = "v1.1.0" # version

    print("PythonFDR " + version + "  Copyright (C) 2025  Vilgot Szasz Kero")
    print("PythonFDR comes with ABSOLUTELY NO WARRANTY; for details see COPYRIGHT.txt.")
    print("This is free software, and you are welcome to redistribute it")
    print("under certain conditions; see COPYRIGHT.txt for details.")
    print("")


def record_simvars_pct():
    utc_now = datetime.now(timezone.utc)
    utc_time_str = utc_now.strftime("%H%M%S")
    
    log_entry = str(utc_time_str)
    for var in simvars_pct:
        log_entry = (log_entry + ":" + str(sc.get_simdata(var)))
        log_entry = log_entry.replace("ChangeDict({'" + var + "': ", "")
        log_entry = log_entry.replace("})", "")
        log_entry = log_entry.replace("ChangeDict()", "")

    print("")
    print("PythonFDR.record_simvars_pct: LOG ENTRY SUCCESSFUL " + utc_time_str)
    print("")

    return (log_entry)


def log_joystick_position():
    joystick.init()
    pygame.event.pump()
    joystick_x = joystick.get_axis(0)
    joystick_y = joystick.get_axis(1)
    return (str(joystick_x) + ":" + str(joystick_y))


def write_to_log(log_entry):
    with open("fdr.log", "a") as logfile:
        global log_entry_counter
        if log_entry_counter >0:
            logfile.write("\n")
        logfile.write(log_entry)
        log_entry_counter += 1


# Remove previous log file
try:
    os.remove("fdr.log")
except FileNotFoundError:
    pass

license_notice()

# Main loop
while True:
    log_entry = record_simvars_pct()
    log_entry = log_entry + ":" + log_joystick_position()
    write_to_log(log_entry)
    print("PythonFDR: LOG ENTRY WRITTEN TO FILE")
    print("")
    sleep(1)