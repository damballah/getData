import urllib.request
import json
import sys
import os
import platform

plt=platform.system()

#arguments = len(sys.argv) - 1

api_key=sys.argv[3]
reseau=sys.argv[1]
tx=sys.argv[2]


#ropsten
#kovan
#rinkeby
#goerli
#main

if reseau=="ropsten":
	part1="https://api-ropsten.etherscan.io/api?module=proxy&action=eth_getTransactionByHash&txhash="
elif reseau=="kovan":
	part1="https://api-kovan.etherscan.io/api?module=proxy&action=eth_getTransactionByHash&txhash="
elif reseau=="rinkeby":
	part1="https://api-kinkeby.etherscan.io/api?module=proxy&action=eth_getTransactionByHash&txhash="
elif reseau=="goerli":
	part1="https://api-goerli.etherscan.io/api?module=proxy&action=eth_getTransactionByHash&txhash="
elif reseau=="main":
	part1="https://api.etherscan.io/api?module=proxy&action=eth_getTransactionByHash&txhash="
else:
	print("Erreur dans le choix du réseau")

url = part1 + tx + "&apikey=" + api_key

#print("")
#print(url)
#print("")

resp = urllib.request.urlopen(url)

data1 = resp.read().decode()
data2 = json.loads(data1)
laData=data2['result']['input']

if plt=="Windows":
	cmdConstruct="python -m ethereum_input_decoder -t " + laData
	os.system(cmdConstruct)
elif plt=="Linux":
	cmdConstruct="python3 -m ethereum_input_decoder -t " + laData
	os.system(cmdConstruct)
else:

print("")






	





