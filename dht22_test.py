# usr/bin python3

import pigpio
import time
pi = pigpio.pi()
import DHT22
## s = DHT22.sensor(pi, 17) #works with out led blinking
s = DHT22.sensor(pi, 17, 27)  # works and blinks led
s.trigger()
fo = open("/home/pi/temp_log.txt", "w")

count = 0
while (count < 30000):
    time.sleep(60)
    s.trigger()
    localtime = time.asctime( time.localtime(time.time()) )
    #print("Time : {0}".format(localtime))
    fo.writelines("Time : {0}".format(localtime));
    fo.writelines('     Humidity : {0:3.2f}'.format(s.humidity() / 1.));
    #print('Humidity : {:3.2f}'.format(s.humidity() / 1.))
    #print('Temp : {:3.2f}'.format((s.temperature() * 1.8) +32))
    fo.writelines('     Temp : {0:3.2f}\n'.format((s.temperature() * 1.8) +32));

    count = count + 1
fo.close()
s.cancel()
pi.stop()
