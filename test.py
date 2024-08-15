from flask import Flask, jsonify, request

app = Flask(__name__)
stores = [
    {
        'name': 'book 1',
        'items': [
            {
                'name': 'english book',
                'price': 100,
                'description': 'contains english grammar'
            }
        ]
    },
    {
        'name': 'book 2',
        'items': [
            {
                'name': 'hindi book',
                'price': 100,
                'description': 'contains hindi grammar'
            }
        ]
    },
    {
        'name': 'book 3',
        'items': [
            {
                'name': 'maths book',
                'price': 100,
                'description': 'contains maths problems'
            }
        ]
    },
    {
        'name': 'book 4',
        'items': [
            {
                'name': 'science book',
                'price': 100,
                'description': 'contains science experiments'
            }
        ]
    }
]


@app.route('/')
def home():
    return "Hello Api Interface"


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store_name(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify(store)
    return jsonify({'message': 'store not found'})


@app.route('/store')
def get_all_store_name():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if(store['name'] == name):
            new_item = {
                'name': request_data['name'],
                'price': request_data['price'],
                'description': request_data['description']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})


@app.route('/store/<string:name>/item')
def get_store_item(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify(store['items'])
    return jsonify({'message': 'store not found'})


app.run(port=5000)