# this code is already deployed on https://szkasm.pythonanywhere.com/
from flask import Flask, request, jsonify
import random

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_random_number():
    max_num = int(request.args.get('max_num', 10))
    random_num = random.randint(1, max_num)
    return jsonify({'random_number': random_num})
