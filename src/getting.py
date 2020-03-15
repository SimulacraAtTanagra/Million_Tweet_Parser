from requests import *
import sodapy
import math

def func(page_size,pages,token,database_id):
    print("Functiong working, boss!")
    api_url = 'data.cityofnewyork.us'
    client = sodapy.Socrata(api_url,token)
    database = database_id
    total = client.get(database,select='COUNT(*)')

    if pages <0:
        pages= math.ceil(int(total[0]['COUNT'])/page_size)
        return(client.get(database,limit=total[0]['COUNT']))
    listobj=[]
    for i in range(pages):
        listobj.append(client.get(database,limit=page_size,offset=i*page_size))
    return(listobj)

if __name__==("__main__"):
    func()
