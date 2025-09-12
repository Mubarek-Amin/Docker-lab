from flask import Flask 
import Redis

app = Flask(__name__)
redis_client = Redis(host = 'redis', port= 6379)

@app.route('/')
def welcome():
    return "Hello, You made it. This is my flask-redis web page!!"



@app.route('/count')
def count():
    count = redis_client.incr('visitor_count')
    return "This page has been visited this many times :{count}"

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
    