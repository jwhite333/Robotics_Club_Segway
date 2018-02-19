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
    spi.close()
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)


# Set up GPIO Pins
GPIO.setmode(GPIO.BOARD)

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

# Map acceleration to angle
def map(value, low1, high1, low2, high2):

    return low2 + (value-low1)*(high2-low2)/(high1-low1)

def main():
    while True:
        a1_x = float(getInput(0))
        a1_y = float(getInput(1))
        a2_x = float(getInput(6))
        a2_y = float(getInput(7))

        x_avg = np.mean([a1_x, a2_x])
        y_avg = np.mean([a1_y, a2_y])
        angle = np.arctan(x_avg / y_avg)

        angle = map(angle, .53, 1.03, -90, 90)

        print("Angle: {}".format(angle))

if __name__ == '__main__':
    main()
