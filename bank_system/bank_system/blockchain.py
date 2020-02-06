import hashlib
import logging
import time


from ecdsa import NIST256p
from ecdsa import VerifyingKey

logging.basicConfig(level=logging.DEBUG)

class BlockChain(object):

    CONSECUTIVE_NUM = 2

    def __init__(self):
        self.transactions = []
        self.chain = []
        self.create_block(0, {})

    def create_block(self, nonce, hash):
        block = {
            "nonce": nonce,
            "hash": hash,
            "time": time.time(),
            "transactions": self.transactions.copy()
        }
        self.chain.append(block)
        self.transactions = []
        return block

    def add_transaction(self, sender, recipient, value,
                        sender_public_key=None, signature=None):
        transaction = {
            "from": sender,
            "to": recipient,
            "value": value
        }
        if self.verify_signature(sender_public_key, signature, transaction):
            self.transactions.append(transaction)
            return True
        return False

    def verify_signature(self, public_key, signature, transaction):
        obj = hashlib.sha256(str(transaction).encode("utf-8")).digest()
        sign_to_byte = bytes().fromhex(signature)
        verifying_key = VerifyingKey.from_string(
            bytes().fromhex(public_key), curve=NIST256p
        )
        verified_key = verifying_key.verify(sign_to_byte, obj)
        return verified_key


    def find_nonce(self):
        hash = hashlib.sha256(str(self.chain[-1]).encode()).hexdigest()
        transactions = self.transactions
        nonce = 0
        time.sleep(10)
        while True:
            find_block = [hash, transactions, nonce]
            if hashlib.sha256(str(find_block).encode()).hexdigest()[:self.CONSECUTIVE_NUM] \
                == "0" * self.CONSECUTIVE_NUM:
                break
            nonce += 1
        return nonce

    def mining(self):
        while True:
            nonce = self.find_nonce()
            previous_hash = hashlib.sha256(str(self.chain[-1]).encode()).hexdigest()
            self.create_block(nonce, previous_hash)
            print("********************************************")
            print(self.chain)
            print("============================================")


    def total_value(self, email_address):
        total = 0
        for d in self.chain:
            for transaction in d["transactions"]:
                if transaction["from"] == email_address:
                    total -= transaction["value"]
                if transaction["to"] == email_address:
                    total += transaction["value"]
        return total

