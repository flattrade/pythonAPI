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

ret = api.get_limits()
 
print(ret)

