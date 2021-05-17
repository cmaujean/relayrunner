# relayrunner

Small simple py3 program for activating a GPIO relay for an amount of time. Specific to the RPI Relay Board from Electronics Salon.

This was written so I could run it in cron jobs to manage my aeroponic system lights and water pump.

# Usage

    relayrunner.py [-h] --relay {1,2,3} --seconds SECONDS

    Activate a numbered relay for some amount of time

    optional arguments:
      -h, --help         show this help message and exit
      --relay {1,2,3}    The Relay number to activate
      --seconds SECONDS  Time in seconds for the relay to be "On"

# Notes

Relay numbers are as written on the RPI Relay board.
Requires Python3 and the [RPi.GPIO](https://pypi.org/project/RPi.GPIO/) package
