Version = "0.0.1"

APP_ID = "APP_GPS"
DEVICE = "LinkIt_Smart_7688"
DEVICE_ID = "DEVICE_ID1234"
DEVICE_IP = ''

Interval_LCD = 5

Reboot_Time = 86400			# interval to reboot (seconds); 0 for no-rebooti

Restful_URL = "https://data.lass-net.org/Upload/MAPS.php?"
# Restful_URL = "https://rootn.rocks/airbox?"
Restful_interval = 300			# 300 seconds

SecureKey = "NoKey"

FS_SD = "/mnt/mmcblk0p1"

#################################
# don't make any changes in the following codes

import uuid
import re
import os
from multiprocessing import Queue

float_re_pattern = re.compile("^-?\d+\.\d+$")                                                                                               
num_re_pattern = re.compile("^-?\d+\.\d+$|^-?\d+$")

#mac = str(':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])).upper()
# mac = open('/sys/class/net/eth0/address').readline().upper().strip()
# DEVICE_ID = mac.replace(':','')                                                                           

# f = os.popen('ifconfig eth0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1')
# DEVICE_IP=f.read()
# if(DEVICE_IP == ''):
#         f = os.popen('ifconfig apcli0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1')
#         DEVICE_IP=f.read()    


fields ={       "Tmp"   :       "s_t0",           
                "RH"    :       "s_h0",           
                "PM1.0" :       "s_d2",           
                "PM2.5" :       "s_d0",           
                "PM10"  :       "s_d1",              
                "Lux"   :       "s_l0",              
                "CO2"   :       "s_g8e",              
		"TVOC"	:	"s_gg",
		"lat"	:	"gps_lat",
		"lon"	:	"gps_lon",
		"sat_num"	:	"gps_num",
        }                                           
values = {      "app"           :       APP_ID,      
                "device_id"     :       DEVICE_ID,                  
                "device"        :       DEVICE,                     
                "ver_format"    :       3,                        
                "fmt_opt"       :       0,             
                "FAKE_GPS"      :       0,                        
                "gps_fix"       :       1,                        
                "gps_num"       :       100,                      
                "date"          :       "1900-01-01",                        
                "time"          :       "00:00:00",                          
        }                       
