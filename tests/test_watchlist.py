import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_helper import NorenApiPy
import logging 

#supress debug messages for prod/tests
logging.basicConfig(level=logging.DEBUG)

#start of our program
api = NorenApiPy()

#set token and user id
#paste the token generated using the login flow described 
# in LOGIN FLOW of https://pi.flattrade.in/docs
usersession='token here'
userid = 'user id here'

ret = api.set_session(userid= userid, password = '', usertoken= usersession)

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
    