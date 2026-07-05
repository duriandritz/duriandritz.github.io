import os
# added a date/time library
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    pf = db.execute(
        "SELECT * FROM inventory WHERE user_id = ?", session["user_id"]
    )
    cc = db.execute(
        "SELECT * FROM users WHERE id = ?", session["user_id"]
    )
    cash = cc[0]["cash"]
    if not pf:
        pf = [{"stock": "None",
            "units": "None",
            "price": "None",
            "cv": "None"}]

        return render_template("index.html", portfolio = pf, cash = usd(cash), sum = 0, total = usd(cash))

    elif pf:
        sum = 0
        for row in pf:
            infos = lookup(row["stock"])
            cp = infos["price"]
            row["price"] = cp
            row["cv"] = cp * row["units"]
            sum += row["cv"]
            row["cv"] = usd(row["cv"])

        total = cash + sum
        return render_template("index.html", portfolio = pf, cash = usd(cash), sum = usd(sum), total = usd(total))



@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")

    if request.method == "POST":
        # Validation 1: Did user input symbol?
        if not request.form.get("symbol"):
            return apology("input symbol", 400)

        # Validation 2: Did user input valid number of shares?
        ns = request.form.get("shares")
        if not ns.isdigit():
            return apology("input a positive integer", 400)
        if ns == "0":
            return apology("input a positive integer", 400)

        # Validation 3: Did user input correct symbol?
        infos = lookup(request.form.get("symbol"))
        dtnow = datetime.datetime.today()
        # (dtnow performed here to be same time as lookup)
        if not infos:
            return apology("incorrect symbol", 400)

        # Validation 4: Does the user have enough funds?
        price = infos["price"]
        nu = int(ns)
        cp = float(price)
        cost = nu*cp
        rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        funds = rows[0]["cash"]
        if (cost > funds):
            return apology("not enough funds", 400)

        # All validations complete. Execute transaction.
        balance = funds - cost
        # Deduct cost from cash and update balance
        db.execute(
            "UPDATE users SET cash = ? WHERE id = ? ", balance, session["user_id"]
            )
        # Log transaction
        db.execute(
            "INSERT INTO transactions (user_id, transaction_type, stock, units, unit_price) VALUES(?,?,?,?,?)", session["user_id"], "buy", infos["symbol"], nu, cp,
            )
        # Log transaction date
        trid = db.execute("SELECT MAX(transaction_id) AS n FROM transactions")[0]["n"]
        db.execute(
            "INSERT INTO trdates (tr_id, tr_year, tr_month, tr_day, tr_hour, tr_min, tr_sec) VALUES(?,?,?,?,?,?,?)", trid, dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second
        )
        # Update inventory
        # Does the user already own this kind of stock?
        cs = db.execute(
            "SELECT * FROM inventory WHERE user_id = ? AND stock = ?", session["user_id"], infos["symbol"]
        )
        if not cs:
            db.execute(
                "INSERT INTO inventory (user_id, stock, units) VALUES(?,?,?)", session["user_id"], infos["symbol"], nu
                )
        else:
            csu = cs[0]["units"]
            upcsu = csu + nu
            db.execute(
                "UPDATE inventory SET units = ? WHERE user_id = ?", upcsu, session["user_id"]
            )
        return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute(
        "SELECT * FROM transactions JOIN trdates ON transactions.transaction_id = trdates.tr_id WHERE user_id = ?", session["user_id"]
    )
    if not transactions:
        return apology("you do not have any transactions yet", 400)

    for row in transactions:
        row["value"] = row["units"]*row["unit_price"]
        row["value"] = usd(row["value"])
        row["unit_price"] = usd(row["unit_price"])

    return render_template("history.html", history = transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        # show the search bar
        return render_template("quote.html")

    if request.method == "POST":
        # show the search bar but with the items as a list
        # Validation 1: Did user input symbol?
        if not request.form.get("symbol"):
            return apology("input symbol", 400)

        # All validations cleared, we output the stock price
        infos = lookup(request.form.get("symbol"))
        if not infos:
            return apology("lookup error", 400)

        return render_template("quoted.html", name = infos["name"], price = usd(infos["price"]), symbol = infos["symbol"])


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Let's first assume the user is not yet logged in.
    # Therefore they will go to the register page.
    if request.method == "GET":
        return render_template("register.html")

    # I now have the form set up. Now to validate the submission form.
    if request.method == "POST":
        # Validation 1: Did user input a username?
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Validation 2: Does the username already exist in the database?
        # Query database for username (copied from login)
        users = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )
        # If username already exists, we return apology
        if len(users) != 0:
            return apology("username already exists", 400)

        # Validation 3: Did user input a password?
        if not request.form.get("password"):
            return apology("must provide password", 400)

        # Validation 4: Did user input the same retype?
        if (str(request.form.get("password")) != str(request.form.get("confirmation"))):
            return apology("password and confirmation do not match", 400)

        # All validations cleared, we insert the user into our database.
        username = request.form.get("username")
        hash = generate_password_hash(str(request.form.get("password")))
        db.execute("INSERT INTO USERS (username,hash) VALUES(?, ?)", username, hash)
        return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        cs = db.execute(
            "SELECT * FROM inventory WHERE user_id = ?", session["user_id"]
        )
        return render_template("sell.html", stocks=cs)

    if request.method == "POST":
        # Validation 1: Does the user own this stock?
        symbol = request.form.get("symbol")
        infos = lookup(symbol)
        dtnow = datetime.datetime.today()
        if not infos:
            return apology("incorrect symbol", 400)
        cs = db.execute(
            "SELECT * FROM inventory WHERE user_id = ? AND stock = ?", session["user_id"], infos["symbol"]
        )
        if not cs:
            return apology("incorrect stock", 400)

        # Validation 2: Did user input valid number of shares?
        nstosell = request.form.get("shares")
        if not nstosell.isdigit():
            return apology("input a positive integer", 400)
        if nstosell == "0":
            return apology("input a positive integer", 400)

        # Validation 3: Did user have enough stocks to sell?
        cns = cs[0]["units"]
        nstosell = int(nstosell)
        if (nstosell > cns):
            return apology("not enough stocks", 400)

        # All validations clear. Perform transaction.

        # Log transaction
        db.execute(
            "INSERT INTO transactions (user_id, transaction_type, stock, units, unit_price) VALUES(?,?,?,?,?)", session["user_id"], "sell", infos["symbol"], nstosell, infos["price"]
        )

        # Log transaction date
        trid = db.execute("SELECT MAX(transaction_id) AS n FROM transactions")[0]["n"]
        db.execute(
            "INSERT INTO trdates (tr_id, tr_year, tr_month, tr_day, tr_hour, tr_min, tr_sec) VALUES(?,?,?,?,?,?,?)", trid, dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second
        )

        # Update inventory
        # Does the user still have this stock after transaction?
        nsrem = cns - nstosell
        if (nsrem == 0):
            db.execute(
                "DELETE FROM inventory WHERE user_id = ? AND stock = ?", session["user_id"], infos["symbol"]
            )
        elif (nsrem > 0):
            db.execute(
                "UPDATE inventory SET units = ? WHERE user_id = ? AND stock = ?", nsrem, session["user_id"], infos["symbol"]
            )

        # Update cash balance
        sold = nstosell * infos["price"]
        cu = db.execute(
            "SELECT * FROM users WHERE id = ?", session["user_id"]
        )
        cash = cu[0]["cash"]
        balance = cash + sold
        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?", balance, session["user_id"]
        )
        return redirect("/")
