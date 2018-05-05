# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# TSL2561
# This code is designed to work with the TSL2561_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Light?sku=TSL2561_I2CS#tabs-0-product_tabset-2
#!/usr/bin/env python3
import smbus
import time
#from dhtxx import DHT22

#import Adafruit_DHT as dht

# Get I2C bus
bus = smbus.SMBus(1)

# TSL2561 address, 0x39(57)from dhtxx import DHT11, DHT22
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


"""
def read_results_without_exceptions():
    # Adjust pin (BCM) for your needs !
    dht22 = dht.DHT22(17)

    while True:
        # Retries 'max_tries' from DHT11 to get a valid result
        r = dht22.get_result(max_tries=10)  # 'max_tries' defaults to 5
        if r:
            print(r)
        else:
            print('Failed to get result !')
        time.sleep(5)


def read_results_with_exceptions():
    # Adjust pin (BCM) for your needs !
    dht22 = dht.read_retry(dht.DHT22,17)
    i = 0
    while i <= 5:
        i = i + 1
  +      try:
            s = dht22.sensor(pi,17,27)
            s.trigger()
            reading=dht.read_retry(dht.DHT22,17)
            print((0.8 * (reading[0]) + 32.0))
            print(('{:3.2f}'.format(reading[1]/1.)))
        except Exception as e:
            print(e)
        time.sleep(5)
        s.cancel()

"""


# Output data to screen
full = ch0 + ch1
print("Full Spectrum( IR + Visible ) :%d lux" % full)
print("Infrared Value :%d lux" % ch1)
print("Visible Value :%d lux" % (ch0 - ch1))

# read_results_with_exceptions()
