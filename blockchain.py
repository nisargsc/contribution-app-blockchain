class Blockchain():
    def __init__(self):
        self.chain = [
            {
                'state' : { 'funds' : [] },
                'nounce' : 0,
                'hash' : "0x0",
                'prev_hash' : "prev_hash"
            },
            {
                'state' : {
                    'funds' : [
                        {
                            'id' : "abc",
                            'title' : "title of the fund",
                            'description' : "description of the fund",
                            'donations' : [
                                {
                                    'amount' : 100
                                }
                            ]
                        },
                    ]
                },
                'nounce' : 123,
                'hash' : "hash",
                'prev_hash' : "prev_hash"
            }
        ]
        self.state = {}
        self.nodes = []
    
    def update_state(self):
        self.state = self.chain[-1]['state']