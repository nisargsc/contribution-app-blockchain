import json
from block import Block

class Blockchain():
    def __init__(self):
        self.difficulty = 2
        self.chain = []
        self.state = {}
        self.nodes = []

        self.create_genesis()

    def get_state(self):
        self.state = self.chain[-1]['state']
        return self.state

    def create_genesis(self):
        """
        Creates the genesis block
        :return: None
        """
        if len(self.chain) == 0:
            genesis = Block()
            self.proof_of_work(genesis)
            self.chain.append(genesis.dict())
            self.get_state()
            # print("genesis: ", genesis)

    def mine_block_add_fund(self, title, description):

        print("---------in mine_block before creating new_block-----------")
        chain = self.chain
        print(json.dumps(chain, indent = 4))
        new_block = Block(num=len(self.chain), prev_hash=self.chain[-1]['hash'], funds_dict=self.state['funds'])
        print("---------in mine_block before update state add fund-----------")
        print(json.dumps(chain, indent = 4))
        new_block.update_state_add_fund(title,description)
        self.proof_of_work(new_block)
        print("---------in mine_block after add_fund before append-----------")
        print(json.dumps(chain, indent = 4))
        self.chain = chain
        self.chain.append(new_block.dict())
        print("---------in mine_block after append-----------")
        print(json.dumps(chain, indent = 4))

        self.get_state()

        # print("add fund new block: ", new_block)

    def mine_block_add_donation(self, amount, fund_id):
        chain = self.chain
        new_block = Block(num=len(self.chain), prev_hash=self.chain[-1]['hash'], funds_dict=self.state['funds'])
        new_block.update_state_add_donation(amount, fund_id)
        self.proof_of_work(new_block)
        self.chain = chain
        self.chain.append(new_block.dict())
        self.get_state()
        # print("add fund new block: ", new_block)
    
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
    
    def print_chain(self):
        print(json.dumps(self.chain, indent = 4))

    def dict(self):
        """
        :return: <dict> python dictionary for the current chain details
        """
        chain_dict = {
            'length' : len(self.chain),
            'chain' : self.chain,
            'state' : self.state
        }
        return chain_dict

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

    print("------------Added genesis----------------\n")
    # b.print_chain()


    print("------------Added fund t1----------------\n")
    b.mine_block_add_fund('t1','description for t1')
    # b.print_chain()

    # b.mine_block_add_donation(100, b.state['fund-id-list'][0])
    # b.print_chain()

    # print("------------Added fund t2----------------\n")
    # b.mine_block_add_fund('t2','description for t2')
    # b.print_chain()
    # b.mine_block_add_donation(220, b.state['fund-id-list'][0])
    # b.print_chain()
    # print("------------^^add donation to t1^^----------------")
    # print(json.dumps(b.get_state(), indent = 4))
    # print("---------------^^final state^^------------------------")

# chain = [
#             {
#                 'state' : { 'funds' : [] },
#                 'nounce' : 0,
#                 'hash' : "0x0",
#                 'prev_hash' : "prev_hash"
#             },
#             {
#                 'state' : {
#                     'funds' : {
#                         'abc' : {
#                             'title' : "title of the fund",
#                             'description' : "description of the fund",
#                             'donations' : [
#                                 {
#                                     'amount' : 100
#                                 },
#                                 {
#                                     'amount' : 100
#                                 }
#                             ]
#                         },
#                     }
#                 },
#                 'nounce' : 123,
#                 'hash' : "hash",
#                 'prev_hash' : "prev_hash"
#             }
#         ]