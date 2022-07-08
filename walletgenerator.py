from web3 import Web3
import time
import os

rpc = 'https://rpcapi.fantom.network/'

w3 = Web3(Web3.HTTPProvider(rpc))
f = open('./wallets.txt', 'a', encoding="utf-8")
string = input('String to be generated: ')
walletsCounter = 0
start_time = time.time()
while True:
  acc = w3.eth.account.create()
  walletsCounter+=1
  print("\rSearchig... %s wallets genereated"%(walletsCounter), end='')
  if string in acc.address:
    genTime = time.time() - start_time
    print(f'Wallet generated: {acc.address} key stored in wallets.txt, generated in {genTime} seconds')
    f.write(f'{acc.address}\n')
    f.write(f'key {w3.toHex(acc.key)}\n')
    os.system(f"notify-send 'Wallet gerada: {acc.address}'")
    break
