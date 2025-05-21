from flask import Flask, make_response, request, jsonify, render_template
from flask_cors import CORS
from service import Service

app = Flask(__name__)
CORS(app)

@app.route("/")
def indexHtml():
    return render_template("index.html")

@app.route("/adapter", methods=["POST"])
def adapter():
    try:
        response = make_response(Service.newService().adapter(request.json))
        response.mimetype = "text/plain"
        return response
        
    except Exception as e:
        return jsonify(str(e)), 400
    
@app.route("/generator/tent", methods=["POST"])
def generateTent():
    try:
        response = make_response(Service.newService().generateTent(request.json))
        response.mimetype = "text/plain"
        return response
        
    except Exception as e:
        return jsonify(str(e)), 400

if __name__ == "__main__":
    app.run(debug=True)


