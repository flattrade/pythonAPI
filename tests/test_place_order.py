import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_helper import NorenApiPy
import logging

#enable dbug to see request and responses
logging.basicConfig(level=logging.DEBUG)

#start of our program
api = NorenApiPy()

#set token and user id
#paste the token generated using the login flow described 
# in LOGIN FLOW of https://pi.flattrade.in/docs
usersession='token here'
userid = 'user id here'

ret = api.set_session(userid= userid, password = '', usertoken= usersession)

ret = api.place_order(buy_or_sell='B', product_type='C',
                        exchange='NSE', tradingsymbol='CANBK-EQ', 
                        quantity=1, discloseqty=0,price_type='SL-LMT', price=200.00, trigger_price=199.50,
                        retention='DAY', remarks='my_order_001')

print(ret)

## check sl modification
orderno = ret['norenordno']

ret = api.modify_order(exchange='NSE', tradingsymbol='CANBK-EQ', orderno=orderno,
                                   newquantity=2, newprice_type='SL-LMT', newprice=201.00, newtrigger_price=200.00)


print(ret)

ret = api.modify_order(exchange='NSE', tradingsymbol='CANBK-EQ', orderno=orderno,
                                   newquantity=2, newprice_type='MKT', newprice=0.00)

print(ret)

ret = api.single_order_history(orderno=orderno)

for ord in ret:
    
    print(f"{ord['qty']} prc: {ord['prc']} trgprc: {ord['trgprc']} {ord['rpt']}")



