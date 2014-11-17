
# coding: utf-8

# In[20]:

#Ask user for list
#Open list from file
#Create a url_list
#For each word on each line in list
#Create a url and add it to the url_list
#For each url in url_list, make request, get response
#Decode and process
#Store as JSON object and extract desired key/value pairs
#...
import csv

file = raw_input("Filename: ") #Spanishtestwords.csv or sample1.csv

with open(file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print row[0]


# In[21]:

#User enters preference. Assume he wants dictionary.
lang1 = raw_input("Source language: ")
lang2 = raw_input("Return language: ")
phrase = raw_input("Word: ")
#lang1 = "eng"
#lang2 = "eng"
#phrase = "bone"
url = str

def glosbeurl(lang1, lang2, phrase):#phrase should be an optional arg if reading from file only
    #url = "http://glosbe.com/gapi/translate?from=" + %s + "&dest=" + %s + "&format=json&phrase=" + %s + "&pretty=true"
    url = "http://glosbe.com/gapi/translate?from=%s&dest=%s&format=json&phrase=%s&pretty=true" % (lang1, lang2, phrase)
          #https://glosbe.com/gapi/
        #{function-name}[?[{function-parameter1}
        # e.g. translate?from
        # ={value}[&{function-parameter2}
        # e.g. =eng&dest
        # ={value}[&{function-parameter3}={value}...]]]]
        # =eng
    return url


#GET URLS FOR EACH WORD IN LIST
with open(file, 'r') as f:
    reader = csv.reader(f)
    for row in reader: #pass row to glosbeurl
        print glosbeurl(lang1, lang2, row[0])
        

#glosbeurl(lang1, lang2, phrase)
    


# In[22]:

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
    


#GET URLS FOR EACH WORD IN LIST
with open(file, 'rb') as f:
    reader = csv.reader(f)
    for row in reader: #pass row to glosbeurl
        print glosbeurl(lang1, lang2, row[0])
        req = urllib2.Request(glosbeurl(lang1, lang2, row[0]))
        response = urllib2.urlopen(req)
        data = response.read().decode('utf-8')
        theJSON = process(data)
        theJSON = json.loads(theJSON) #returns JSON as python data dict
        print theJSON

#json.dumps(theJSON, sort_keys=True, indent=4, separators=(',',':',)) #returns unicode JSON. Use as needed.



# In[ ]:

#EDIT TO LOOP THROUGH AND FIND KEY VALUE PAIRS IN A PYTHON DICT FORMAT

specific_key = 'tuc'
print type(theJSON)

found = False
for key,value in theJSON.iteritems():
           if key.startswith(specific_key): 
            found = True
            print key, value
            
            #Converting the JSON to Python and recursively searching is by far the easiest:

def get_all(theJSON, key):
    if type(theJSON) == str:
        theJSON = json.loads(theJSON)
    if type(theJSON) is dict:
        for jsonkey in theJSON:
            if type(theJSON[jsonkey]) in (list, dict):
                get_all(theJSON[jsonkey], key)
            elif jsonkey == key: 
                print theJSON[jsonkey]
    elif type(theJSON) is list:
        for item in theJSON:
            if type(item) in (list, dict):
                get_all(item, key)

                #http://stackoverflow.com/questions/14048948/how-can-i-use-python-finding-particular-json-value-by-key
            
get_all(theJSON,'text')

#["phrase"]["result"]["meanings"]["text"]


# In[89]:

#output the dictionary entries to file
with open('Gosbe_dic.txt', 'w') as outfile:
    json.dump(theJSON, outfile, sort_keys = True, indent = 4, ensure_ascii=False)


# In[ ]:



