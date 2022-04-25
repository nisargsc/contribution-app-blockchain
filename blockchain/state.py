import json
import copy
from blockchain.funds import Fund
# from funds import Fund

class State():
    def __init__(self, prev_state = None):

        if prev_state is None:
            self.funds_dict = {}
            self.funds = {}
            self.fund_id_list = []
        else:
            self.funds_dict = copy.deepcopy(prev_state.funds_dict)
            self.funds = copy.deepcopy(prev_state.funds)
            self.fund_id_list = copy.deepcopy(prev_state.fund_id_list)

    def add_fund(self, title, description):
        f = Fund(title, description)
        f_dict = f.dict()

        if f_dict['id'] not in self.funds.keys():
            self.funds[f_dict['id']] = f

        if f_dict['id'] not in self.funds_dict.keys():
            self.funds_dict[f_dict['id']] = f_dict[f_dict['id']]
        
        self.update_fund_id_list()
    
    def add_donation(self, amount, fund_id):
        f = self.funds[fund_id]
        f.add_donation(amount)
        self.funds[fund_id] = f
        self.funds_dict[fund_id] = f.dict()[fund_id]
        self.update_fund_id_list()
    
    def update_fund_id_list(self):
        # print('in fund list')
        for key in list(self.funds_dict.keys()):
            if key not in self.fund_id_list:
                # print(f'appending {key}')
                self.fund_id_list.append(key)


    def dict(self):
        """
        :return: <dict> python dictionary for the current fund details
        """
        state_dict = {
            'fund_id_list' : self.fund_id_list,
            'funds' : self.funds_dict
        }
        return state_dict

    def json(self):
        """
        :return: <json> json responce for the current fund details
        """
        fund_json = json.dumps(self.dict(), indent = 4)
        return fund_json

    def __str__(self):
        """
        Gets called every time fund object is converted to string
        :return: <str> String of the json responce
        """
        return str(self.json())

if __name__ == "__main__":
    s = State()
