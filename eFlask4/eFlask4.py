# coding=utf-8
#import settings
from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/item/<id>/')
def item(id):
    return 'Item:{}'.format(id)
if __name__=='__main__':
    #app.run(host='0.0.0.0', port=9000)
    app.run(host='127.0.0.1', port=9000)
    #app.config.from_object(settings)
    #app.debug = True
