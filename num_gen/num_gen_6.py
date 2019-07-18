#!flask/bin/python
from flask import Flask, jsonify, make_response
from random import randint
import string

app = Flask(__name__)

@app.route('/num_gen', methods=['GET'])
def generate_num():
    sixDigitNum = randint(100000, 999999)
    return str(sixDigitNum)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=9017)




