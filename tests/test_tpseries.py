import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_helper import NorenApiPy
import logging
import datetime
import timeit

#supress debug messages for prod/tests
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)


#start of our program
api = NorenApiPy()

#set token and user id
#paste the token generated using the login flow described 
# in LOGIN FLOW of https://pi.flattrade.in/docs
usersession='token here'
userid = 'user id here'

ret = api.set_session(userid= userid, password = '', usertoken= usersession)

if ret != None:   
    lastBusDay = datetime.datetime.today()
    lastBusDay = lastBusDay.replace(hour=0, minute=0, second=0, microsecond=0)

    if datetime.date.weekday(lastBusDay) == 5:      #if it's Saturday
     lastBusDay = lastBusDay - datetime.timedelta(days = 1) #then make it Friday
    elif datetime.date.weekday(lastBusDay) == 6:      #if it's Sunday
     lastBusDay = lastBusDay - datetime.timedelta(days = 2); #then make it Friday

    print(lastBusDay.timestamp())
    #lastBusDay = 1639098000

    starttime = timeit.default_timer()
    print("The start time is :",starttime)
    #get one day's data

    #ret = api.get_time_price_series(exchange='NSE', token='22', starttime=lastBusDay.timestamp())
    ret = api.get_time_price_series(exchange='NSE', token='2885')
    print("The time difference is :", timeit.default_timer() - starttime)

    if ret != None:
        print(len(ret))
        print(ret[0])
        print(ret[-1])