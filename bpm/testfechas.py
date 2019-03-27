from datetime import datetime, date, time, timedelta
import calendar
import time
from urllib.parse import quote
#2018-07-10T00%3A00%3A00Z
formato = "%d-%m-%yT%H:%M:%S%ZZ"
#fecha = (datetime.today()) - (timedelta(days=180))
fecha = date.fromtimestamp(time.time())
#fecha = fecha.fromisoformat(formato) 
print("Se eliminaran instancias previas a: ", fecha)

t = time.time()
print ('t:', t)
print ('fromtimestamp(t):', datetime.date.fromtimestamp(t))