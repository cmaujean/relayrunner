#!/usr/bin/python3

import time
import sys
import argparse
import warnings
import RPi.GPIO as GPIO

PINS = {
  1: 21,
  2: 20,
  3: 26,
}

# Prepare the relays
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

parser = argparse.ArgumentParser(description='Activate a numbered relay for some amount of time')
parser.add_argument('--relay', dest='relay', type=int, choices=[1,2,3], required=True, help="The Relay number to activate")
parser.add_argument('--seconds', dest='seconds', type=int, required=True, help="Time in seconds for the relay to be \"On\"")
parser.format_help()
try:
  args = parser.parse_args()
  pin = int(PINS.get(args.relay, 0))
  # validate the pin choice
  if pin == 0:
    sys.exit(f'ERROR: relay {args.relay} not found in the pins map')

  print(f'Activating relay {args.relay} on pin {pin} for {args.seconds} seconds')  

  # activate the relay
  GPIO.output(pin, GPIO.HIGH)

  # wait the requested amount of time
  time.sleep(args.seconds)

  # deactivate the pin
  GPIO.output(pin, GPIO.LOW)
except KeyboardInterrupt: 
  print("User Canceled Run")

finally:
  # ensure cleanup is run
  warnings.filterwarnings("ignore")
  GPIO.cleanup()
