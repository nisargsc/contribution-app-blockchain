import hashlib
import datetime
import json
from time import sleep

class Fund:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.donations = []

        self.id = self.find_id()

    def find_id(self):
        """
        Finds the id of the current fund using title and description
        :return: <str> hash of the current fund
        """
        hash = hashlib.sha256()
        block_string = f"{self.title}{self.description}"
        hash.update(block_string.encode('utf-8'))
        return hash.hexdigest()
    
    def add_donation(self, amount):
        donation = {
            'amount' : amount,
            'timestamp' : str(datetime.datetime.now())
        }

        self.donations.append(donation)
        return self.donations

    def dict(self):
        """
        :return: <dict> python dictionary for the current fund details
        """
        fund_dict = {
            'id' : f'{self.id}',
            f'{self.id}' : {
                'title' : self.title,
                'description' : self.description,
                'donations' : self.donations
            }
        }
        return fund_dict

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
    f1 = Fund("t1","d1 is the descritption of the funt f1")

    print(f1,"\n")
    f1.add_donation(100)
    sleep(5)
    f1.add_donation(200)
    sleep(8)
    f1.add_donation(300)
    print(f1,"\n")
    print("---------")
    print(json.dumps(f1.donations, indent = 4))