from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Example for post'

@app.route('/post', methods=["POST"])
def testpost():
     input_json = request.get_python(force=True) 
     dictToReturn = {'text':input_python['text']}
     return python(dictToReturn)

app.run()
