import serial
import time
import os
import conf as Conf

sensors = []
count = 0
while True:
  if count % 10 == 0:
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

  data = ''
  for i in range(len(sensors)):
    if(os.path.exists('/dev/ttyUSB'+str(i))):
      if sensors[i].inWaiting() > 0:
        data  += '|sen%d:%d' % (i, (int(sensors[i].read(32)[7].encode('hex'), 16)))
  print(data)
  if len(data) > 0:
    restful_str = "wget -O /tmp/last_upload.log \"" + Conf.Restful_URL + "topic=" + Conf.APP_ID + "&device_id=" + Conf.DEVICE_ID + "&msg=" + data + "\""
    os.system(restful_str)
  time.sleep(1)
  count += 1