from flask import Flask, render_template, request, redirect, url_for
import logic


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        password = request.form["password"]
        username = request.form["username"]
        print(username, password)
    return render_template("index.html")
    
    
if __name__ == "__main__":
    app.run(debug=True)