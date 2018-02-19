import RPi.GPIO as GPIO
import spidev
import numpy as np
from time import sleep
import signal
import sys


# Catch ctrl-c
def sigint_handler(signum, frame):
    print("Shutting down...")
    GPIO.cleanup()
    sys.exit(0)
    spi.close()
    spi.exit(0)
signal.signal(signal.SIGINT, sigint_handler)


# Set up GPIO Pins
GPIO.setmode(GPIO.BOARD) # BOARD
#GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#PIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Setup ADC
spi = spidev.SpiDev()
spi.open(0, 0)

# Get ADC input
def getInput(channel):
    #check validity (should always work)
    if ((channel > 7) or (channel < 0)):
        return -1

    #Preform SPI transaction and store returned bits in 'r'
    r = spi.xfer([1, (8 + channel) << 4, 0])

    #Filter Data Bits from returned bits
    adcIn = ((r[1]&3) << 8) + r[2]
    
    return adcIn

def main():
    while True:
        x_value = float(getInput(0))
        y_value = float(getInput(1))
        print("X: {}".format(x_value))
        print("Y: {}".format(y_value))

if __name__ == '__main__':
    main()
