import json
from block import Block

class Blockchain():
    def __init__(self):
        self.chain = []
        self.state = {}
        self.nodes = []

    def get_state(self):
        self.state = self.chain[-1]['state']
        return self.state
    
    def dict(self):
        """
        :return: <dict> python dictionary for the current chain details
        """
        chain_dict = {
            'length' : len(self.chain),
            'chain' : self.chain,
            'state' : self.state.dict()
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

    print(b)

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