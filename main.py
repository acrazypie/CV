from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/data", methods=["GET"])
def get_data():
    data = {
        "name": "Elisa Genesio",
        "role": "AR/VR Developer",
        "skills": ["Python", "Unity", "AR/VR Development"],
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
