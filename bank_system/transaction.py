from ecdsa import NIST256p
from ecdsa import SigningKey
import hashlib

class Account(object):

    def __init__(self, mail):
        self.__private_key = SigningKey.generate(curve=NIST256p)
        self.__public_key = self.__private_key.get_verifying_key()
        self.mail = mail

    @property
    def private_key(self):
        return self.__private_key.to_string().hex()

    @property
    def public_key(self):
        return self.__public_key.to_string().hex()


class Transaction(object):

    def __init__(self, private, public, from_address, to_address, value):
        self.private = private
        self.public = public
        self.from_address = from_address
        self.to_addreass = to_address
        self.value = value

    def generate_signature(self):
        transaction = {"from": self.from_address,
                       "to": self.to_addreass,
                       "value": self.value
                       }
        send_obj = hashlib.sha256(str(transaction).encode("utf-8")).digest()
        private_key = SigningKey.from_string(
            bytes().fromhex(self.private), curve=NIST256p
        )
        signature = private_key.sign(send_obj).hex()
        return signature


if __name__ == '__main__':
    accountA = Account("jfaj")
    accountB = Account("fjeafjoi")
    t = Transaction(accountA.private_key, accountA.public_key, "A", "B", 1)
    print(t.generate_signature())
#######################

    tf = blockchain.add_transaction(
        "A", "B", 1, accountA.public_key, t.generate_signature()
    )
    print(tf)
    time.sleep(5)
    print(blockchain.chain)