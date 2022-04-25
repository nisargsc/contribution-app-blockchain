import json
from blockchain.block import Block
# from block import Block

class Blockchain():
    def __init__(self):
        self.difficulty = 2
        self.chain = []
        self.state = None
        self.nodes = []
        self.create_genesis()

    def get_state(self):
        self.state = self.chain[-1].state
        return self.state

    def create_genesis(self):
        if len(self.chain) == 0:
            genesis = Block()
            self.proof_of_work(genesis)
            self.chain.append(genesis)
            self.get_state()
        
    def mine_block_add_fund(self, title, description):
        new_block = Block(num=len(self.chain), prev_hash=self.chain[-1].hash, prev_state = self.state)
        new_block.update_state_add_fund(title,description)
        self.proof_of_work(new_block)
        self.chain.append(new_block)
        self.get_state()

    def mine_block_add_donation(self, amount, fund_id):
        new_block = Block(num=len(self.chain), prev_hash=self.chain[-1].hash, prev_state = self.state)
        new_block.update_state_add_donation(amount, fund_id)
        self.proof_of_work(new_block)
        self.chain.append(new_block)
        self.get_state()
        
    def proof_of_work(self, block:Block):
        """
        Updates the nonce and the hash of the block according to the proof of work algoritm
        :param block: <Block>
        :return: None
        """
        while self.valid_proof(block.find_hash()) is False:
            block.nonce += 1
        block.update_hash()

    def valid_proof(self, hash):
        """
        Validates the proof according to the proof of work algoritm
        :param hash: <hash> Hash generated for proof of work algoritm
        :return: <bool> True if guess_hash has its fist 'self.difficulty' digits as '0'.
        """
        return hash[:self.difficulty]=="0" * self.difficulty
    
    def dict(self):
        """
        :return: <dict> python dictionary for the current chain details
        """
        chain = self.dict_chain()
        
        chain_dict = {
            'length' : len(chain),
            'chain' : chain,
            'state' : self.state.dict()
        }
        return chain_dict

    def dict_chain(self):
        chain_dict = []
        for block in self.chain:
            chain_dict.append(block.dict())

        return chain_dict

    def print_chain(self):
        print(json.dumps(self.dict_chain(), indent = 4))

    def json(self):
        """
        :return: <json> json responce for the current chain details
        """
        chain_json = json.dumps(self.dict(), indent = 4)
        return chain_json

    def __str__(self):
        """
        Gets called every time fund object is converted to string
        :return: <str> String of the json responce
        """
        return str(self.json())

if __name__ == "__main__":
    b = Blockchain()

    b.mine_block_add_fund('t1','description for t1')
    print("-----add_fund------")
    b.print_chain()
    b.mine_block_add_donation(100, b.state.fund_id_list[0])
    print("-----add_donation 100------")
    b.print_chain()
    b.mine_block_add_donation(200, b.state.fund_id_list[0])
    print("-----add_donation 200------")
    b.print_chain()
    b.mine_block_add_donation(200, b.state.fund_id_list[0])
    print("-----add_donation 300------")
    b.print_chain()
