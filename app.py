from blockchain import Blockchain
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
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
    chain = blockchain.dict_chain()
    resp_json = {
        'length' : len(chain),
        'chain' : chain,
    }

    return jsonify(resp_json), 200

@app.route('/chain/state', methods=['GET'])
def chain_state():
    state = blockchain.get_state()
    resp_json = {
        'state': state.dict()
    }
    return jsonify(resp_json), 200

@app.route('/funds', methods=['GET'])
def funds():
    state = blockchain.get_state()

    id = request.args.get('id')
    if id is None:
        resp_json = state.dict()
        return jsonify(resp_json), 200
    else:
        fund = state.funds[id]
        resp_json = {
            'fund' :{
                'title' : fund.title,
                'description' : fund.description,
                'donations' : fund.donations
            }
        }
        return jsonify(resp_json), 200

@app.route('/funds/new', methods=['POST'])
def new_funds():
    resp_json = {
        'message': ''
    }

    values = request.get_json()
    title = values.get('title')
    description = values.get('description')
    if title is None or description is None:
        resp_json['message'] = "Error: req body needs 'title' and 'description' values"
        return jsonify(resp_json), 400

    if (not isinstance(title, str)) or title.isnumeric() or title=="":
        resp_json['message'] = "Error: title must be a non-numeric non-empty string"
        return jsonify(resp_json), 400
    if (not isinstance(description, str)) or description.isnumeric():
        resp_json['message'] = "Error: description must be a non-numeric string"
        return jsonify(resp_json), 400
    
    blockchain.mine_block_add_fund(title,description)
    state = blockchain.get_state()

    resp_json = {
        'message' : 'new block mined, fund added, and state updated',
        'state' : state.dict()
    }
    return jsonify(resp_json), 200

@app.route('/donations', methods=['GET'])
def donations():
    state = blockchain.get_state()

    resp_json = {
        'message': ''
    }

    fund_id = request.args.get('fund_id')
    if fund_id is None:
        resp_json['message'] = "Error: no 'fund_id' in req params"
        return jsonify(resp_json), 400
    else:
        fund = state.funds[fund_id]
        resp_json = {
            'donations' : fund.donations
        }
        return jsonify(resp_json), 200

@app.route('/donations/new', methods=['POST'])
def new_donations():
    resp_json = {
        'message': ''
    }

    fund_id = request.args.get('fund_id')
    if fund_id is None:
        resp_json['message'] = "Error: no 'fund_id' in req params"
        return jsonify(resp_json), 400
    else:
        values = request.get_json()
        amount = values.get('amount')
        if amount is None:
            resp_json['message'] = "Error: req body needs 'amount'"
            return jsonify(resp_json), 400
        else:
            if (not isinstance(amount, (int, float))) or amount <= 0:
                resp_json['message'] = "Error: amount must be a positive number"
                return jsonify(resp_json), 400
            else:
                blockchain.mine_block_add_donation(amount, fund_id)
                state = blockchain.get_state()
                fund = state.funds[fund_id]

                resp_json = {
                    'message' : f'new block mined, new donation added to fund {fund_id}',
                    'donations' : fund.donations
                }
                return jsonify(resp_json), 200

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(port=port, debug=True)