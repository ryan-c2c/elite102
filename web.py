from flask import Flask, render_template, request, redirect, url_for
import logic


<<<<<<< HEAD
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
=======
def main():
    app = Flask(__name__)

    @app.route('/', methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            username = request.form["username"]
            initial_amount = request.form["initial_amnt"]
            logic.create_account(username, initial_amount)
        return render_template("index.html")

    @app.route('/deposit', methods=["POST"])
    def deposit():
        if request.method == "POST":
            username = request.form["username"]
            amount = request.form["amount"]
            logic.deposit(username, amount)

        return redirect(url_for('home'))

    @app.route('/withdraw', methods=["POST"])
    def withdraw():
        if request.method == "POST":
            username = request.form["username"]
            amount = request.form["amount"]
            logic.withdraw(username, amount)

        return redirect(url_for('home'))

    @app.route('/delete', methods=["POST"])
    def delete():
        logic.delete()

        return redirect(url_for('home'))

    app.run(host='0.0.0.0', debug=True)


if __name__ == "__main__":
    main()
>>>>>>> 4b2ce59 (Finished and changed my logic and html, all now connect fluidly all together)
