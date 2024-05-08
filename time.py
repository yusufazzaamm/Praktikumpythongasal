import time

localtime = time.localtime(time.time())
print("Waktu lokal saat ini :", localtime)

import time

localtime = time.asctime( time.localtime(time.time()) )
print("Waktu lokal saat ini :", localtime)

import calendar

cal = calendar.month(2008, 1)
print "Dibawah ini adalah kalender:" #python 2
print cal