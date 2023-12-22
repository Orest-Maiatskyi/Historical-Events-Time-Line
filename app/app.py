from flask import Flask, render_template, request

from api import get_events
from app.conf import API_KEY

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')


@app.route('/get_historical_events', methods=['GET'])
def get_historical_events():

    text = None if len(request.args.get('text').replace(' ', '')) == 0 else request.args.get('text')
    year = None if len(request.args.get('year').replace(' ', '')) == 0 else request.args.get('year')
    month = None if len(request.args.get('month').replace(' ', '')) == 0 else request.args.get('month')
    day = None if len(request.args.get('day').replace(' ', '')) == 0 else request.args.get('day')
    offset = None if len(request.args.get('offset').replace(' ', '')) == 0 else request.args.get('offset')

    if text is None and year is None and month is None and day is None:
        return {'text': 'Bad Request'}, 400

    return get_events(API_KEY, text, year, month, day, offset), 200
