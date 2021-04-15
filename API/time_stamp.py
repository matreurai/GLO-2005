
# ----------------------------------
# Time stamp pour de nouvelle data
# fait par: David Bolduc
# Projet: GLO-2005
# ----------------------------------

import time
from datetime import datetime

def timestampe_now():
    while True:
        # create a timestamp for the present moment:
        currentTime_timestamp = time.time()
        currentTime = datetime.fromtimestamp(currentTime_timestamp).strftime("%Y-%m-%d %H:%M:%S")
        return (str(currentTime))

def timestampe_15min():
    while True:
        currentTime_timestamp = time.time()
        # create a timestamp for 15 minutes into the future:
        nextTime = currentTime_timestamp + 900  # 15min = 900 seconds
        return (str(datetime.fromtimestamp(nextTime).strftime("%Y-%m-%d %H:%M:%S")))
        # time.sleep(900)  # call the api every 15 minutes
# print ('now:', timestampe_now(), 'later:', timestampe_15min())