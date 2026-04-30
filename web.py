from flask import Flask, render_template, request, redirect, url_for
import logic


def main():
    app = Flask(__name__)

    @app.route('/', methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            username = request.form["username"]
            initial_amount = request.form["initial_amnt"]
            logic.create_account(username, initial_amount)
        accounts = logic.get_accounts()
        return render_template("index.html", accounts=accounts)

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
