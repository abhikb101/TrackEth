from flask import Flask, request, render_template

from solc import compile_source

from web3 import Web3, HTTPProvider

from web3.contract import ConciseContract

app = Flask(__name__)

http_provider = HTTPProvider('HTTP://192.168.6.225:7545')
eth_provider = Web3(http_provider).eth
default_account = eth_provider.accounts[0]
transaction_details = {
    'from': default_account,
}

with open('face.sol') as file:
    source_code = file.readlines()

compiled_code = compile_source(''.join(source_code))

contract_name = 'face'

contract_bytecode = compiled_code[f'<stdin>:{contract_name}']['bin']
contract_abi = compiled_code[f'<stdin>:{contract_name}']['abi']
contract_factory = eth_provider.contract(
    abi=contract_abi,
    bytecode=contract_bytecode,
)
contract_constructor = contract_factory.constructor()

transaction_hash = contract_constructor.transact(transaction_details)

transaction_receipt = eth_provider.getTransactionReceipt(transaction_hash)
contract_address = transaction_receipt['contractAddress']

contract_instance = eth_provider.contract(
    abi=contract_abi,
    address=contract_address, 
    #ContractFactoryClass=ConciseContract,
)
#reader = ConciseContract(contract_instance)
#uid=1;
#system_id=1;
#a=reader.addPerson(uid,system_id, transact={'from':default_account, 'gas':1000000})
#print(a)
#system_id=2;
#b=reader.addPerson(uid, system_id)
#personRecord = reader.getPerson(uid)
#print("person", personRecord)

if __name__ == '_main_':
    app.run(debug=True, use_reloader=False)

