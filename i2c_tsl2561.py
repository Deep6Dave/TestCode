#!/usr/bin/env python3

# i2c_tsl2561.py
# 2017-02-22
# Public Domain NO

import time

import pigpio  # http://abyz.co.uk/rpi/pigpio/python.html

BUS = 1

TSL2561_I2C_ADDR = 0x39

RUNTIME = 60.0

pi = pigpio.pi()  # open local Pi

h = pi.i2c_open(BUS, TSL2561_I2C_ADDR)


if h >= 0:  # Connected OK?

   # Initialise TSL2561.
   pi.i2c_write_byte_data(h, 0x00, 0)  # POWER_CTL reset.
   pi.i2c_write_byte_data(h, 0x01, 1)  # Register Timing - Nominal = 402ms.
   time.sleep(0.5)
   read = 0

   start_time = time.time()

   #while (time.time()-start_time) < RUNTIME:
   while read < 5:
        pi.i2c_write_byte_data(h, 0x00, 0)  # POWER_CTL reset.
        pi.i2c_write_byte_data(h, 0x01, 1)  # Register Timing - Nominal = 402ms.
        time.sleep(0.5)

        data = pi.i2c_read_i2c_block_data(h, 0x0C, 2)
        data1 = pi.i2c_read_i2c_block_data(h, 0x0E, 2)
        #ch0 = data[1] * 256 + data[0]
        #ch1 = data1[1] * 256 + data1[0]
        print((data))
        print((data[0]))
        num = int.from_bytes(data[1], byteorder='little', signed=True)
        #num = struct.unpack(">L", data[1])[0]
        print(("num value is ",num))
        #print("Full Spectrum( IR + Visible ) :%d lux" %(data[1] * 256 + data[0])))
        #print("Infrared Value :%d lux" %(data1[1] * 256 + data1[0]))
        #print("Visible Value :%d lux" %(ch0 - ch1))
        read += 1

   pi.i2c_close(h)

pi.stop()

print(read, read / RUNTIME)