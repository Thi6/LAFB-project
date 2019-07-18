#!flask/bin/python
from flask import Flask, jsonify, make_response
from random import randint

app = Flask(__name__)

@app.route('/num_gen', methods=['GET'])
def generate_num():
    eightDigitNum = randint(10000000, 99999999)
    return str(eightDigitNum)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=9017)




