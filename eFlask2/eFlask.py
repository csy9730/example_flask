from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'welcome !!! This is the home page'
if __name__=='__main__':    
	app.run()
