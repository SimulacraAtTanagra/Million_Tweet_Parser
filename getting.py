from requests import *
import sodapy
import math

def func(page_size,pages,token):
    api_url = 'data.cityofnewyork.us'
    client = sodapy.Socrata(api_url,token)
    database = "nc67-uf89"
    total = client.get(database,select='COUNT(*)')

    if pages <0:
        pages= math.ceil(int(total[0]['COUNT'])/page_size)
    for i in range(pages):
        print('/n/n/n',client.get(database,limit=page_size,offset=i*page_size),timeout=60)

if __name__==("__main__"):
    func()
