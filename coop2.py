# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# TSL2561
# This code is designed to work with the TSL2561_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Light?sku=TSL2561_I2CS#tabs-0-product_tabset-2
#/usr/bin python3

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# TSL2561 address, 0x39(57)
# Select control register, 0x00(00) with command register, 0x80(128)
#		0x03(03)	Power ON mode
bus.write_byte_data(0x39, 0x00 | 0x80, 0x03)
# TSL2561 address, 0x39(57)
# Select timing register, 0x01(01) with command register, 0x80(128)
#		0x02(02)	Nominal integration time = 402ms
bus.write_byte_data(0x39, 0x01 | 0x80, 0x02)

time.sleep(0.5)

# Read data back from 0x0C(12) with command register, 0x80(128), 2 bytes
# ch0 LSB, ch0 MSB
data = bus.read_i2c_block_data(0x39, 0x0C | 0x80, 2)

# Read data back from 0x0E(14) with command register, 0x80(128), 2 bytes
# ch1 LSB, ch1 MSB
data1 = bus.read_i2c_block_data(0x39, 0x0E | 0x80, 2)

# Convert the data
ch0 = data[1] * 256 + data[0]
ch1 = data1[1] * 256 + data1[0]

"""
DHT22 code
"""
import pigpio
import DHT22
import time
##import datetime
##from time import sleep
##import RPi.GPIO as GPIO
##  must run sudo pigpiod from cmd prompt prior to running this script after
##  every restart of PI.
pi = pigpio.pi()  ## Initiate GPIO for pigpio.
dht22 = DHT22.sensor(pi, 17)  ## use the actual GPIO pin name/number
dht22.trigger()  ## forces a reading.  first reading is just junk.
sleepTime = 3   ## must sleep at least 3 second to stop sensor hangs.

def readDHT22():
    dht22.trigger()
    humidity = " %.2f" % (dht22.humidity())
    temp = " %.2f" % (dht22.temperature())
    return (humidity, temp)

def Temp_Tol():
    temperature = int(temperature)
    if temperature + "%" > int(27.00):
        print("\n\n Temperature too High")
    else:
        print(" ")


def Hum_Tol():
    humidity = int(humidity)
    if humidity + "%" > int(40.00):
        print("\n\n Humidity too High")
    else:
        print(" ")


while True:
    
    time.sleep(3)
    readDHT22()
    count = 0
    while True:
        count += 1
        humidity, temperature = readDHT22()


        if count > 3:
            print("Humidity is: " + humidity + "%")
            print("Temperature is: " + temperature + "C")
            Temp_Tol()
            Hum_Tol()
    break





# Output data to screen
print("Full Spectrum(IR + Visible) :%d lux" %ch0)
print("Infrared Value :%d lux" %ch1)
print("Visible Value :%d lux" %(ch0 - ch1))
