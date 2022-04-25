from blockchain import Blockchain
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

blockchain = Blockchain()


@app.route('/', methods=['GET'])
def home():
    resp_json = {
        'message': 'API is running!!' 
    }
    return jsonify(resp_json), 200

@app.route('/chain', methods=['GET'])
def chain():
    resp_json = {
        'length' : len(blockchain.chain),
        'chain' : blockchain.chain,
    }

    return jsonify(resp_json), 200

@app.route('/chain/state', methods=['GET'])
def chain_state():
    blockchain.update_state()
    resp_json = {
        'state': blockchain.state 
    }
    return jsonify(resp_json), 200

@app.route('/funds', methods=['GET'])
def funds():
    resp_json = {
        'message': ''
    }

    id = request.args.get('id')
    if id is None:
        resp_json['message'] = "no 'id' in req params"
        return resp_json, 200
    else:
        resp_json['message'] = f'given id: {id}'
        return resp_json, 200

@app.route('/funds/new', methods=['POST'])
def new_funds():
    resp_json = {
        'message': 'init msg'
    }

    values = request.get_json()
    title = values.get('title')
    description = values.get('description')
    if title is None or description is None:
        resp_json['message'] = "Error: req body needs 'title' and 'description' values"
        return resp_json, 400

    if (not isinstance(title, str)) or title.isnumeric() or title=="":
        resp_json['message'] = "Error: title must be a non-numeric non-empty string"
        return resp_json, 400
    if (not isinstance(description, str)) or description.isnumeric():
        resp_json['message'] = "Error: description must be a non-numeric string"
        return resp_json, 400
    
    resp_json = {
        'title' : title,
        'description' : description
    }
    return resp_json, 200

@app.route('/donations', methods=['GET'])
def donations():
    resp_json = {
        'message': ''
    }

    fund_id = request.args.get('fund-id')
    if fund_id is None:
        resp_json['message'] = "Error: no 'fund-id' in req params"
        return resp_json, 400
    else:
        resp_json['message'] = f'given fund-id: {fund_id}'
        return resp_json, 200

@app.route('/donations/new', methods=['POST'])
def new_donations():
    resp_json = {
        'message': ''
    }

    fund_id = request.args.get('fund-id')
    if fund_id is None:
        resp_json['message'] = "Error: no 'fund-id' in req params"
        return resp_json, 400
    else:
        values = request.get_json()
        amount = values.get('amount')
        if amount is None:
            resp_json['message'] = "Error: req body needs 'amount'"
            return resp_json, 400
        else:
            if (not isinstance(amount, (int, float))) or amount <= 0:
                resp_json['message'] = "Error: amount must be a positive number"
                return resp_json, 400
            else:
                resp_json['message'] = f"fund-id: {fund_id} | donation-amount: {amount}"
                return resp_json, 200

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(port=port, debug=True)