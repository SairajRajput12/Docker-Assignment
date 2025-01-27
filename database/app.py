from flask import Flask, jsonify,json, request
from flask_cors import CORS
import os 

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


DATA_FILE = os.path.join(os.getcwd(), 'data', 'data', 'users.json')


def read_users():
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def write_users(data):
    print(data)
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)



@app.route('/')
def home():
    return jsonify({"message":"this is the database server !!"})


@app.route('/read_data1', methods=['GET'])
def send_data():
    data = read_users()
    print("this is read function executing")
    return jsonify({"message": "data retrived succesfully !","data":data}),200


@app.route('/write_data1', methods=['POST'])
def write_data():
    data = request.json
    given_data = data.get('updated_data') 
    write_users(given_data)
    return jsonify({"message": "data written succesfully !"}),200


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5001)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
