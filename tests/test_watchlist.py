import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_helper import NorenApiPy
import logging 

#supress debug messages for prod/tests
logging.basicConfig(level=logging.DEBUG)

#start of our program
api = NorenApiPy()

#set token
usersession='8fea10ad126ba63f019eb89d2894c182903b8c8e18ecc739570d18e8eb6647f6'
ret = api.set_session(userid= 'FT000069', password = '', usertoken= usersession)

if ret != None:   
    wlnames = api.get_watch_list_names()

    for wl in wlnames['values']:
        print(80*'=')        
        scrips = api.get_watch_list(wlname=wl)
        print(scrips)
        print(80*'=')        

    wltest = wlnames['values'][0]
    ret = api.add_watch_list_scrip(wlname=wltest, instrument='NSE|22')
    wlscrips = api.get_watch_list(wlname=wltest)

    for scrip in wlscrips['values']:
        print(f"{scrip['exch']} - {scrip['token']} {scrip['tsym']}")
    
    print(80*'=')
    ret = api.delete_watch_list_scrip(wlname=wltest, instrument='NSE|22')
    wlscrips = api.get_watch_list(wlname=wltest)

    for scrip in wlscrips['values']:
        print(f"{scrip['exch']} - {scrip['token']} {scrip['tsym']}")
    