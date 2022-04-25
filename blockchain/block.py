import hashlib
import datetime
import json
from blockchain.state import State
# from state import State

class Block():
    def __init__(self, num=0, prev_hash=None, prev_state = State()):
        """
        :param prev_hash: <str> Hash of the previous block
        :return: None
        """
        self.num = num
        self.timestamp = datetime.datetime.now()
        self.nonce = 0
        self.state = State(prev_state)
        self.prev_hash = prev_hash
        self.hash = self.find_hash()

    def update_state_add_fund(self, title, description):
        self.state.add_fund(title,description)
        self.update_hash()

    def update_state_add_donation(self, amount, fund_id):
        self.state.add_donation(amount, fund_id)
        self.update_hash()

    def find_hash(self):
        """
        Finds the hash of the current block using timestamp, state, prev_hash and nonce
        :return: <str> hash of the current block
        """
        hash = hashlib.sha256()
        block_string = f"{self.num}{str(self.timestamp)}{self.state}{self.prev_hash}{self.nonce}"
        hash.update(block_string.encode('utf-8'))
        return hash.hexdigest()

    def update_hash(self):
        """
        Updates the hash of the current block
        :return: None
        """
        self.hash = self.find_hash() 

    def dict(self):
        """
        :return: <dict> python dictionary for the current block details
        """
        block_dict = {
            'num' : self.num,
            'timestamp' : str(self.timestamp),
            'state' : self.state.dict(),
            'prev_hash' : self.prev_hash,
            'hash' : self.hash,
            'nonce' : self.nonce
        }
        return block_dict

    def json(self):
        """
        :return: <json> json responce for the current blcok details
        """
        block_json = json.dumps(self.dict(), indent = 4)
        return block_json

    def __str__(self):
        """
        Gets called every time block object is converted to string
        :return: <str> String of the json responce
        """
        return str(self.json())

if __name__ == "__main__":
    def pow(b):
        while b.hash[:2]!="00":
            b.nonce += 1
            b.update_hash()
    def prt(b):
        print("---------------")
        print(b)
        print("-----^^before pow^^--------")
        pow(b)
        print(b)
        print("------^^after pow^^-------")

    b= Block()
    prt(b)
    b.update_state_add_fund('t1','description for t1')
    prt(b)
    b.update_state_add_donation(100, b.state.fund_id_list[0])
    prt(b)
    b.update_state_add_fund('t2','description for t2')
    prt(b)
    b.update_state_add_donation(220, b.state.fund_id_list[0])
    prt(b)