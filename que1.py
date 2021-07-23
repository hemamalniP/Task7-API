from flask import Flask, request
app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def index():
    new_data={
    name_str = str(request.json['name'])
    age_str = str(request.json['age'])
    place_str= str(request.json['place'])
    }
    return str(new_data)

if __name__ == "__main__":
	app.run(debug=True)



