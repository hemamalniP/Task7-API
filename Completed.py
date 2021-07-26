from flask import Flask, request,jsonify
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    name = request.args.get('name')
    age = request.args.get('age')
    place= request.args.get('place')
    	
    return '''
    		<h1> name: {}</h1>
    		<h1> age: {}</h1>
    		<h1> place: {}'''.format(name,age,place)
    		
app.run()


