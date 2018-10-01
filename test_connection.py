import httplib
import socket

# define some variables
test_con_url = "www.google.com" # For connection testing
test_con_resouce = "/intl/en/policies/privacy/" # may change in future
test_con = httplib.HTTPConnection(test_con_url) # create a connection


try:
    test_con.request("GET", test_con_resouce) # do a GET request
    response = test_con.getresponse() # get the response from the GET request
except httplib.ResponseNotReady as e:
    print "Improper connection state"
except socket.gaierror as e:
    print "Not connected"
else:
    print "Connected"

test_con.close()
