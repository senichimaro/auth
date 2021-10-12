#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Import Python Package
import jwt
import base64


# In[13]:


# Init our Data
payload = {'park':'madison square'}
algo = 'HS256' #HMAC-SHA 256
secret = 'learning'


# In[21]:


# Encode a JWT
encoded_jwt = jwt.encode(payload, secret, algorithm=algo)
print(encoded_jwt)


# In[ ]:


# Decode a JWT
# decoded_jwt = jwt.decode(encoded_jwt, secret, verify=True)
decoded_jwt = jwt.decode('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXJrIjoiY2VudHJhbCBwYXJrIn0.H7sytXDEHK1fOyOYkII5aFfzEZqGIro0Erw_84jZuGc', secret, verify=True)
print(decoded_jwt)


# In[17]:


# Decode with Simple Base64 Encoding
decoded_base64 = base64.b64decode(str(encoded_jwt).split(".")[1]+"==")
print(decoded_base64)

