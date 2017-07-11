import hashlib
import hmac
import base64

with open('/home/<user>/Applications/Password/Wordlists/1_million_password_list_top_1000000.txt') as f:
   for line in f:
       print line
       message = bytes('dXNlcj1tb25hJmlkPTExMzQmbmFtZT1Nb25h')
       try:
       	   secret = bytes(line)
       except:
           pass	   
       hash = hmac.new(secret, message, hashlib.sha256).digest()
       #print hash

       # to lowercase hexits
       # hash.hexdigest()
       # to base64
       signature = hash.encode('base64').strip('\n')
       print signature
       print "-------------------------------------------------"

       if 'hhdg0/xpysPiquwdGpH+EgsnfQFSXDo7dNOCrRqMJaU=' in signature:
          break
