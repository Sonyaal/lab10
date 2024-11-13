# Team Memebers: Sonya Alexis and Ethan Palosh

import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#using physical pin 11 to blink an LED
GPIO.setmode(GPIO.BOARD)
chan_list = [11]
GPIO.setup(chan_list, GPIO.OUT)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# by taking readings and printing them out, find
# appropriate threshold levels and set them 
# accordingly. Then, use them to determine
# when it is light or dark, quiet or loud.
lux_treshold=250  # change this value
sound_treshold=650 # change this value


while True: 
  #Following commands control the state of the output
  for i in range(5):
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(11, GPIO.LOW)
    time.sleep(0.5)

  for i in range(50):
    reading = mcp.read_adc(0)
    if reading > lux_treshold:
      print("LIGHT: " + str(reading))
    else:
      print("DARK: " + str(reading))
    time.sleep(0.1)

  for i in range(5):
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(11, GPIO.LOW)
    time.sleep(0.2)

  for i in range(50):
    reading = mcp.read_adc(1)
    if reading > sound_treshold:
      print("LOUD: " + str(reading))
      GPIO.output(11, GPIO.HIGH)
      time.sleep(0.1)
      GPIO.output(11, GPIO.LOW)
    else:
      print("QUIET: " + str(reading))
      time.sleep(0.1)