from flask import Flask 
import redis

app = Flask(__name__)
redis_client = redis.Redis(host = 'redis', port= 6379, db=0)

@app.route('/')
def welcome():
    return "Hello, You made it. This is my flask-redis web page!!"



@app.route('/count')
def count():
    count = redis_client.incr('visitor_count')
    return f"This page has been visited this many times :{count}"

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5005)
