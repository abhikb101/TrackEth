from flask import Flask, request, render_template
from solc import compile_source
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract

app = Flask(__name__)

http_provider = HTTPProvider('http://192.168.6.225:7545')
eth_provider = Web3(http_provider).eth
default_account = eth_provider.accounts[0]
transaction_details = {
    'from': default_account,
}
with open('face.sol') as file:
    source_code = file.readlines()

contract_name = 'face'    
compiled_code = compile_source(''.join(source_code))
contract_abi = compiled_code[f'<stdin>:{contract_name}']['abi']

contract_instance= eth_provider.contract(
    abi=contract_abi,
    address='0xca68c3d6E693987E4Bca2aBab97F6c25598DE7b3'
    #ContractFactoryClass=ConciseContract,
    )
reader = ConciseContract(contract_instance)
def set(uid,system_id):
    reader.addPerson(uid,system_id, transact={'from':default_account, 'gas':1000000})
def get(uid):    
    personRecord = reader.getPerson(int(uid))
    return personRecord


if __name__ == '_main_':
    app.run(debug=True, use_reloader=False)
