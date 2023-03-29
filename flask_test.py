from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('decisionTree.sav', 'rb'))

# create an empty list to store items
items = []


# define a route for getting all items in the list
@app.route('/items', methods=['GET'])
def get_items():
    return {
        'method': request.method,
        'headers': dict(request.headers),
        'data': request.get_data(as_text=True)
    }

@app.route('/predict', methods=['GET'])
def predict():
    result = model.predict([[22,0,0,1,1,0]])[0]
    if result == 0:

        return jsonify({'result': 'successful'})
    
    else:
        return jsonify({'result': 'failure'})



# define a route for adding a new item to the list
@app.route('/items', methods=['POST'])
def add_item():
    item = request.json['item']
    items.append(item)
    return jsonify({'message': 'Item added successfully'})


if __name__ == '__main__':
    app.run(debug=True)
