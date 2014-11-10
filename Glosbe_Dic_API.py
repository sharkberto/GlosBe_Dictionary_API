
# coding: utf-8

# In[16]:


import urllib2
import json
from HTMLParser import HTMLParser

def unescape_entities(value, parser=HTMLParser()):
    return parser.unescape(value)

def process(ob):
    if isinstance(ob, list):
        return [process(v) for v in ob]
    elif isinstance(ob, dict):
        return {k: process(v) for k, v in ob.items()}
    elif isinstance(ob, str):
        return unescape_entities(ob)
    return ob

url = ' http://glosbe.com/gapi/translate?from=tur&dest=eng&format=json&phrase=ocak&pretty=true'
#
#https://glosbe.com/gapi/
#{function-name}[?[{function-parameter1}
# e.g. translate?from
# ={value}[&{function-parameter2}
# e.g. =eng&dest
# ={value}[&{function-parameter3}={value}...]]]]
# =eng



req = urllib2.Request(url)
response = urllib2.urlopen(req)
data = response.read().decode('utf-8') 

theJSON = json.loads(data)
theJSON = process(theJSON)
print(theJSON)


# In[ ]:



