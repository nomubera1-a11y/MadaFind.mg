from flask import Flask, send_file
import os
 
app = Flask(__name__)
 
@app.route('/')
@app.route('/index.html')
def home():
    return send_file('madafind.html')
 
if __name__ == '__main__':
    app.run()
