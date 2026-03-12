import os
from flask import Flask, send_file
 
app = Flask(__name__)
 
@app.route('/')
def index():
    base = os.path.dirname(os.path.abspath(__file__))
    return send_file(os.path.join(base, 'index.html'))
 
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
