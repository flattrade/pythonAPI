import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_helper import NorenApiPy
import logging

#enable dbug to see request and responses
logging.basicConfig(level=logging.DEBUG)

#start of our program
api = NorenApiPy()

#set token
usersession='8fea10ad126ba63f019eb89d2894c182903b8c8e18ecc739570d18e8eb6647f6'
ret = api.set_session(userid= 'FT000069', password = '', usertoken= usersession)

ret = api.get_positions()

p = ret[0]
ret = api.position_product_conversion(p['exch'], p['tsym'], p['netqty'], 'I', p['prd'], 'B', 'DAY')

print(ret)