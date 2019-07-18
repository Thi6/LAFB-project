#!flask/bin/python
from flask import Flask, jsonify, make_response
from random import randint

app = Flask(__name__)

@app.route('/text_gen', methods=['GET'])
def rand_three_string ():
 my_string = "abcdefghijklmnopqrstuvwxyz"
 index1 = randint(0,25)
 index2 = randint(0,25)
 index3 = randint(0,25)
 letter1 = my_string[index1]
 letter2 = my_string[index2]
 letter3 = my_string[index3]
 return (letter1 + letter2 + letter3)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=9018)




