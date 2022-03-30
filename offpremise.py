import requests
import json
import sys
import urllib3 
import ipaddress
from os.path import exists
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#offPremise

seed = sys.argv[1]
arr = {}
#gcp
try:
	gcpsc = open("db/gcpsc.json")
	res = json.load(gcpsc)
	gcpsc.close()
except FileNotFoundError:
	r = requests.get(url="https://www.gstatic.com/ipranges/cloud.json",timeout=90, verify=False)
	res = r.json()

	with open('db/gcpsc.json', 'w') as f:
	    json.dump(res, f)

for i in range(len(res["prefixes"])):
	newkey1 = res["prefixes"][i]["service"].replace(" ","-")+"-"+res["prefixes"][i]["scope"]
	try:
		value1 = res["prefixes"][i]["ipv4Prefix"]
	except KeyError:
		continue
	arr[value1] = newkey1

#aws
try:
	awssc = open("db/awssc.json")
	res = json.load(awssc)
	awssc.close()
except FileNotFoundError:
	r = requests.get(url="https://ip-ranges.amazonaws.com/ip-ranges.json",timeout=90, verify=False)
	res = r.json()

	with open('db/awssc.json', 'w') as f:
	    json.dump(res, f)

for i in range(len(res["prefixes"])):
	newkey1 = res["prefixes"][i]["service"].replace(" ","-")
	newkey1 = newkey1 + "-"+res["prefixes"][i]["region"]
	try:
		value1 = res["prefixes"][i]["ip_prefix"]
	except KeyError:
		continue
	arr[value1] = newkey1

#azure
try:
	azrsc = open("db/azrsc.json")
	res = json.load(azrsc)
	azrsc.close()
except FileNotFoundError:
	r = requests.get(url="https://download.microsoft.com/download/7/1/D/71D86715-5596-4529-9B13-DA13A5DE5B63/ServiceTags_Public_20220321.json",timeout=90, verify=False)
	res = r.json()

	with open('db/azrsc.json', 'w') as f:
	    json.dump(res, f)

for i in range(len(res["values"])):
	newkey1 = res["values"][i]["properties"]["platform"].replace(" ","-")+"-"+res["values"][i]["id"]

	for j in range(len(res["values"][i]["properties"]["addressPrefixes"])):
		try:
			value1 = res["values"][i]["properties"]["addressPrefixes"][j]
		except KeyError:
			continue
		arr[value1] = newkey1

#alicloud		
try:
	alisc = open("db/alisc.json")
	res = json.load(alisc)
	alisc.close()
except FileNotFoundError:
	print("ali cloud IP list not found, please download from https://github.com/hanhanhanz/Offpremise or generate yourself with format [IP/SUBNET:CLOUDSERVICE]")
	exit()

for i in range(len(res["asn"]["prefixes"])):
	if "ALICLOUD" in res["asn"]["prefixes"][i]["id"]: 
		newkey1 = res["asn"]["prefixes"][i]["id"].replace(" ","-")
		
		
		try:
			value1 = res["asn"]["prefixes"][i]["netblock"]
		except KeyError:
			continue
		arr[value1] = newkey1

#digitalOcean
try:
	docsc = open("db/docsc.json")
	res = json.load(docsc)
	docsc.close()
except FileNotFoundError:
	print("Digital Ocean IP list not found, please download from https://github.com/hanhanhanz/Offpremise or generate yourself with format [IP/SUBNET:CLOUDSERVICE]")
	exit()

for i in range(len(res["asn"]["prefixes"])):
	
	newkey1 = res["asn"]["prefixes"][i]["id"].replace(" ","-")
	
	
	try:
		value1 = res["asn"]["prefixes"][i]["netblock"]
	except KeyError:
		continue
	arr[value1] = newkey1

#print(arr)
#print(len(arr))

#linode
try:
	linsc = open("db/linsc.json")
	res = json.load(linsc)
	linsc.close()
except FileNotFoundError:
	print("Linode cloud IP list not found, please download from https://github.com/hanhanhanz/Offpremise or generate yourself with format [IP/SUBNET:CLOUDSERVICE]")
	exit()

for i in range(len(res["asn"]["prefixes"])):
	
	newkey1 = res["asn"]["prefixes"][i]["id"].replace(" ","-")
	
	
	try:
		value1 = res["asn"]["prefixes"][i]["netblock"]
	except KeyError:
		continue
	arr[value1] = newkey1

#print(arr)
#print(len(arr))

#vulntr
try:
	vulsc = open("db/vulsc.json")
	res = json.load(vulsc)
	vulsc.close()
except FileNotFoundError:
	print("Vultr cloud IP list not found, please download from https://github.com/hanhanhanz/Offpremise or generate yourself with format [IP/SUBNET:CLOUDSERVICE]")
	exit()

for i in range(len(res["asn"]["prefixes"])):
	if res["asn"]["prefixes"][i]["domain"] != None:
		if "vultr.com" in res["asn"]["prefixes"][i]["domain"]: 
			newkey1 = "vultr-"+ res["asn"]["prefixes"][i]["country"]
			
			
			try:
				value1 = res["asn"]["prefixes"][i]["netblock"]
			except KeyError:
				continue
			arr[value1] = newkey1

#print(arr)
#print(len(arr))


#sucuri
try:
	sucsc = open("db/sucsc.json")
	res = json.load(sucsc)
	sucsc.close()
except FileNotFoundError:
	print("Sucuri cloud IP list not found, please download from https://github.com/hanhanhanz/Offpremise or generate yourself with format [IP/SUBNET:CLOUDSERVICE]")
	exit()

for i in range(len(res["asn"]["prefixes"])):
	
	newkey1 = "sucuri-"+res["asn"]["prefixes"][i]["id"].replace(" ","-")
	
	
	try:
		value1 = res["asn"]["prefixes"][i]["netblock"]
	except KeyError:
		continue
	arr[value1] = newkey1

#print(arr)
#print(len(arr))

#cloudflare
file_exists = exists("db/cflsc.txt")
if not file_exists:
	r = requests.get(url="https://www.cloudflare.com/ips-v4",timeout=90, verify=False)

	with open('db/cflsc.txt', 'w') as f:
		f.write(r.text)

jsonobj = {"asn":[]}	
with open('db/cflsc.txt') as f:
	lines = [line.rstrip('\n') for line in f]
	for i in lines:

		jsonobj["asn"].append({i:"cloudflare"})
		arr[i] = "cloudflare"

#print(arr)
#print(len(arr))

#imperva
try:
	impsc = open("db/impsc.json")
	res = json.load(impsc)
	impsc.close()
except FileNotFoundError:
	r = requests.post("https://my.imperva.com/api/integration/v1/ips", data={'resp_format': 'json'})
	res = r.json()

	with open('impsc.json', 'w') as f:
		json.dump(res, f)

for i in range(len(res["ipRanges"])):
	newkey1 = "imperva"
	value1 = res["ipRanges"][i]
	arr[value1] = newkey1
#print(arr)
#print(len(arr))


for i in arr:
	if ipaddress.ip_address(seed) in ipaddress.ip_network(i):
		print(arr[i])
		break
		