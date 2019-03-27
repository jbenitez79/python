
import requests
from requests import Request, Session
import urllib3
import json
urllib3.disable_warnings()
from pprint import pprint
from datetime import datetime, date, time, timedelta

#host= 'https://bpmtest.gscorp.ad'
host= 'https://abpmspr-01.gscorp.ad:9444'
uri= '/rest/bpm/wle/v1/systems'
url= host + uri
print ('url '+ url)
s = requests.Session()
s.auth = cred
r = s.get( url , verify=False)
if r.status_code == 200:    
    # Busqueda de instancias Terminadas
    # Seteo de fecha para realizar la busqueda
    formato = "%Y-%m-%dT%H:%M:%S%ZZ"
    fecha = (datetime.today()) - (timedelta(days=60))        
    f = open('instance_deleted_'+(fecha.strftime("%Y%m%dT%H%M%S")), 'w')
    fecha = fecha.strftime(formato)  
    print("Se eliminaran instancias previas a: " + fecha)
    f.write("Se eliminaran instancias previas a: " + fecha + '\n')    
    #print ('url '+ url)
    f.write('URL '+ url + '\n')
    endLoop = True
    while endLoop:
        uri = '/rest/bpm/wle/v1/processes/search?modifiedBefore='+fecha+'&statusFilter=Terminated&limit=100'
        url = host + uri
        r = s.get( url , verify=False)
        #print (r.headers['content-type'])
        resp = r.json()        
        pprint ('Instancias a borrar ' + str(resp['data']['overview']['Terminated']))
        if ((resp['data']['overview']['Terminated']) == 0):
            print ('Fin de loop')
            endLoop = False
        result = (resp['data']['processes'])
        #pprint(result)
        for key in result:
            piid = key['piid']
            #print(piid)
            uri = '/rest/bpm/wle/v1/process/' + piid + '?action=delete&parts=none'
            url = host + uri
            print ('url '+ url)
            r = s.delete( url , verify=False )
            if r.status_code == 200:
                #pprint('Se elimino la instancia '+piid)
                f.write('Se elimino la instancia '+piid + '\n')
            else:
                pprint('Error al eliminar la instancia '+piid)
                pprint(r)
                f.write('Error al eliminar la instancia '+piid + '\n')
                f.write(r + '\n')
else:
    pprint('Error en el llamado')
    pprint (r)
    pprint (host + uri)