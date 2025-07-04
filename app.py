from flask import Flask, Response, make_response, request, jsonify, render_template
# from flask_cors import CORS
from service import Service

app = Flask(__name__)
# CORS(app)

@app.route("/")
def indexHtml():
    return render_template("index.html")

@app.route("/docs")
def docs():
    return render_template("docs.html")

@app.route("/adapter", methods=["POST"])
def adapter():
    try:
        response = make_response(Service.newService().adapter(request.json))
        response.mimetype = "text/plain"
        return response
        
    except Exception as e:
        return jsonify(str(e)), 400
    
@app.route("/generator", methods=["POST"])
def generateTent():
    try:
        response = make_response(Service.newService().generateTent(request.json))
        response.mimetype = "text/plain"
        return response
        
    except Exception as e:
        return jsonify(str(e)), 400
    
@app.route("/files/names")
def getFilesNames():
    try:
        return jsonify(Service.newService().getFilesNames())
        
    except Exception as e:
        return jsonify(str(e)), 400
    
@app.route("/file/get/<name>")
def getFileByName(name):
    try:
        response = make_response(Service.newService().getFileByName(name))
        response.mimetype = "text/plain"
        return response
        
    except Exception as e:
        return jsonify(str(e)), 400
    
@app.route("/file/get/<name>/json")
def getFileByNameJson(name):
    try:
        json = Service.newService().getFileByNameJson(name)
        return Response(json, mimetype='application/json')
    except Exception as e:
        return jsonify(str(e)), 400
    
@app.route("/file/upload", methods=["POST"])
def fileUpload():
    try:
        Service.newService().fileUpload(request.json)
        return jsonify("Saved")
        
    except Exception as e:
        return jsonify(str(e)), 400
    
@app.route("/file/delete", methods=["POST"])
def fileDelete():
    try:
        Service.newService().fileDelete(request.json)
        return jsonify("Deleted")
        
    except Exception as e:
        return jsonify(str(e)), 400

if __name__ == "__main__":
    app.run(debug=True)


