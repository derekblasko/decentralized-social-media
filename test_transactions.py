from wallet import wallet
from blockchain_utils import blockchain_utils
import requests

if __name__ == "__main__":
    bob = wallet()
    alice = wallet()
    exchange = wallet()
    
    transaction = exchange.create_transaction(alice.public_key_string(), 10, "EXCHANGE")
    
    url = "http://localhost:5000/transaction"
    
    package = {"transaction": blockchain_utils.encode(transaction)}
    
    request = requests.post(url, json=package)
    print(request.text)
    
