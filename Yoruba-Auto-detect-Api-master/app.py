from flask import Flask, request, jsonify, render_template
from AutoCorrect import SpellChecker
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialize SpellChecker
parser = SpellChecker("dictionary.txt")

# Define a route for the root URL
@app.route("/")
def index():
    return render_template("index.html")

# Define the API route
@app.route("/api", methods=["POST"])
def spell_check():
    if request.method == "POST":
        request_data = request.get_json(force=True)
        print("FORM DATA RECEIVED", request_data)
        json_to_dict_data = request_data['search_word']
        result_dict = parser.check(json_to_dict_data)
        return jsonify(result_dict), 200

if __name__ == '__main__':
    app.run(debug=True)

