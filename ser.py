import serial
import time
import os
import conf as Conf

# configure the serial connections (the parameters differs on the device you are connecting to)
sensors = []
for i in range(7):
  if(os.path.exists('/dev/ttyUSB'+str(i))):
    sensors.append(
      serial.Serial(
        port='/dev/ttyUSB'+str(i),
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
      )
    )

while True:
  data = ''
  for i in range(len(sensors)):
    if sensors[i].inWaiting() > 0:
      # print(int(sensors.read(1).encode('hex'), 16))
      data  += '|sen%d:%d' % (i, (int(sensors[i].read(32)[7].encode('hex'), 16)))
  print(data)
  if len(data) > 0:
    restful_str = "wget -O /tmp/last_upload.log \"" + Conf.Restful_URL + "topic=" + Conf.APP_ID + "&device_id=" + Conf.DEVICE_ID + "&msg=" + data + "\""
    os.system(restful_str)
  time.sleep(1)
