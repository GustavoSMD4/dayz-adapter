from flask import Flask, request, jsonify, render_template
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
        return jsonify(Service.newService().adapter(request.json))
        
    except Exception as e:
        return jsonify(str(e)), 400

if __name__ == "__main__":
    app.run(debug=True)


