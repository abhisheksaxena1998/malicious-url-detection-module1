import urllib.request, sys, re
import xmltodict, json

xml = urllib.request.urlopen('http://data.alexa.com/data?cli=10&dat=s&url={}'.format("https://www.geeksforgeeks.org/hashing-set-2-separate-chaining/")).read()
 
result= xmltodict.parse(xml)
 
data = json.dumps(result).replace("@","")
data_tojson = json.loads(data)
url = data_tojson["ALEXA"]["SD"][1]["POPULARITY"]["URL"]
rank= data_tojson["ALEXA"]["SD"][1]["POPULARITY"]["TEXT"]
 
print("site {site}, rank {rank}".format(site=url,rank=rank))