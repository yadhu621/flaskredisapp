from flask import Flask
from flask_redis import FlaskRedis

app = Flask(__name__)
app.config['REDIS_URL'] = 'redis://redis:6379/0'

r = FlaskRedis(app)

def get_hits():
  return r.incr('a')

@app.route('/')
def hello():
  hits = get_hits()
  return "Hello from Flask! I got hit {} times".format(hits)
