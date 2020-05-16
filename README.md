# getData.py
### Récupération de la "input data" d'une transaction Ethereum grâce à l'api.

 

> **Prérequis :**
  [Python3](https://www.python.org/) ; [pip](https://pypi.org/project/pip/) ; [ethereum-input-decoder](https://github.com/tintinweb/ethereum-input-decoder) ; [une clé API sur Etherscan.io](https://etherscan.io/apis) <br>

Sous linux Ubuntu et python3:

1°) `apt-get update` <br>
2°) `apt-get install python3-pip` <br>
3°) `python3 -m pip install ethereum-input-decoder` <br>
4°) `git clone https://github.com/damballah/getData.git` <br> 
5°) `cd getData` <br>
6°) `python3 getData.py + reseau + transaction + api_key` <br>

Exemple: 

    python3 getData.py ropsten 0x3c2edfb2e0a... 23ARRW4K8I7G...
ou sur Windows...  

    python getData.py ropsten 0x3c2edfb2e0a... 23ARRW4K8I7G...

(n° de transaction et api_key complètes bien sur)

##### Liste des réseaux à mettre en paramètre n°1:
ropsten <br>
kovan <br>
rinkeby <br>
goerli <br>
main <br>

Le résultat affiché tient sur quelques lignes

**Enjoy ;)**
