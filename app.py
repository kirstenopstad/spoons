import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///spoons.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    """Display default activities"""

    # Define total spoons
    spoons = 15

    # Select user-defined activities from
    one_spoon_activities = db.execute(
        "SELECT * FROM activities WHERE def_val IS ? LIMIT 3", 1)
    two_spoon_activities = db.execute(
        "SELECT * FROM activities WHERE def_val IS ? LIMIT 3", 2)
    three_spoon_activities = db.execute(
        "SELECT * FROM activities WHERE def_val IS ? LIMIT 3", 3)
    four_spoon_activities = db.execute(
        "SELECT * FROM activities WHERE def_val IS ? LIMIT 3", 4)

    return render_template("index.html",
                                one_spoon_activities=one_spoon_activities,
                                two_spoon_activities=two_spoon_activities,
                                three_spoon_activities=three_spoon_activities,
                                four_spoon_activities=four_spoon_activities,
                                spoons=spoons)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    """Allow user to add a new activity"""

    # User reached route via POST
    if request.method == "POST":

       # Define inputs & validate
       activity = request.form.get("title")
       spoons = request.form.get("def_val")

       # Validate inputs <--TODO-->

       # That there is a title, that it doesn't already exist
       if not activity:
            return apology("must provide activity", 400)

       # That there is a value given, that it is a positive integer between 1 and 4
       try:
            if (int(spoons) < 0) or (int(spoons) > 4):
                return apology("spoon value must be between 1 and 4", 400)

       except:
            return apology("must provide valid spoon value", 400)

       else:
            try:
                # Insert into activities
                db.execute("INSERT INTO activities (title, def_val) VALUES (?,?)", activity, spoons)

                # Get user id
                id = session["user_id"]
                user = db.execute(
                    "SELECT * FROM users WHERE id IS ?", id)
                user_id = user[0]["id"]

                # Get activity id
                activity_id = db.execute(
                    "SELECT * FROM activities WHERE title IS ?", activity)
                activity_id = activity_id[0]["activity_id"]

                # Store info in user profile
                db.execute("INSERT INTO profiles (user, activity, user_value) VALUES (?,?, ?)", user_id, activity_id, spoons)

                return redirect("/profile")

            except:
                    return apology("activity already exists", 400)



    # User reached route via GET
    else:
        graphics = db.execute("SELECT * FROM graphics")
        return render_template("add.html", graphics=graphics)


@app.route("/change", methods=["GET", "POST"])
@login_required
def change():
    """Allow user to change value of an activity"""

    if request.method == "POST":

        # Define user, activity & value
        user = session["user_id"]
        activity_title = request.form.get("activity")
        activity_value = request.form.get("value")

        # Validate value is a positive int between 1 and 4
        try:
            if int(activity_value) < 0:
                return apology("Value must be greater than 0", 400)
            elif int(activity_value) > 4:
                return apology("Value cannot be greater than 4", 400)
        except:
            return apology("Value must be a number", 400)

        # Validate activity
        if not activity_title:
            return apology("Must provide activity", 400)
        else:
            # If activity id is in user profile, update value
            user_activities = db.execute(
                "SELECT * FROM activities JOIN profiles ON activities.activity_id=profiles.activity WHERE user = ?", user)

            for row in user_activities:
                if activity_title == row["title"]:
                    activity_id = row["activity_id"]
                    db.execute(
                        "UPDATE profiles SET user_value = ? WHERE user = ? AND activity = ?", activity_value, user, activity_id)
                    return redirect("/profile")

            # Else, if existing activity, add activity and value to user profile
            try:
                activity_id = db.execute(
                    "SELECT activity_id FROM activities WHERE title = ?", activity_title)
                activity_id = activity_id[0]["activity_id"]
                db.execute(
                    "INSERT INTO profiles (user, activity, user_value) VALUES (?,?,?)", user, activity_id, activity_value)
                return redirect("/profile")
            except:
                return apology("Activity does not yet exist", 400)

    # If reached via GET
    else:
        return redirect("/profile")

@app.route("/change_spooncount", methods=["POST"])
@login_required
def change_spooncount():
    """ Allow users to change daily spoon count """

    # Get user spoon count
    spoon_count = db.execute(
        "SELECT spoon_total FROM users where id = ?", session["user_id"])
    spoon_count = spoon_count[0]["spoon_total"]

    # Define inputs for user & daily spoon count
    user = session["user_id"]
    daily_spoons = request.form.get("spoon_total")

    # Validate input is a positive integer
    try:
        if int(daily_spoons) < 0:
            return apology("Spoon value must be greater than 0", 400)
        elif int(daily_spoons) > 100:
            return apology("Spoon value cannot be greater than 100", 400)
    except:
        return apology("Spoon value must be a number", 400)

    # Update user spoon_total on table users
    db.execute(
        "UPDATE users SET spoon_total = ? where id = ?", daily_spoons, user)

    # Return to change
    return redirect("/profile")


@app.route("/counter", methods=["GET", "POST"])
@login_required
def counter():
    """Display standard activities"""

    # Define id, username & spoons
    id = session["user_id"]
    user = db.execute(
        "SELECT username, spoon_total FROM users WHERE id IS ?", id)
    username = user[0]["username"]
    spoons = user[0]["spoon_total"]
    defult = 0;

    # Select user-defined activities from
    one_spoon_activities = db.execute(
        "SELECT * FROM activities JOIN profiles ON activities.activity_id=profiles.activity WHERE user_value IS ? AND user = ?", 1, id)
    two_spoon_activities = db.execute(
        "SELECT * FROM activities JOIN profiles ON activities.activity_id=profiles.activity WHERE user_value IS ? AND user = ?", 2, id)
    three_spoon_activities = db.execute(
        "SELECT * FROM activities JOIN profiles ON activities.activity_id=profiles.activity WHERE user_value IS ? AND user = ?", 3, id)
    four_spoon_activities = db.execute(
        "SELECT * FROM activities JOIN profiles ON activities.activity_id=profiles.activity WHERE user_value IS ? AND user = ?", 4, id)

    return render_template("counter.html",
                                one_spoon_activities=one_spoon_activities,
                                two_spoon_activities=two_spoon_activities,
                                three_spoon_activities=three_spoon_activities,
                                four_spoon_activities=four_spoon_activities,
                                username=username,
                                spoons=spoons)


@app.route("/profile", methods=["GET"])
@login_required
def profile():
    """Display activities added or modified by user"""

    # Get user id
    id = session["user_id"]

    # Get activity and spoon values from profiles, if user_value is > 0
    user_activities = db.execute(
        "SELECT * FROM profiles JOIN activities ON profiles.activity=activities.activity_id WHERE user = ? AND user_value > ? ORDER BY user_value", id, 0)

    # Get all activities
    activities = db.execute(
        "SELECT * FROM activities ORDER BY title")

    # Get user spoon count
    spoon_count = db.execute(
        "SELECT spoon_total FROM users where id = ?", session["user_id"])
    spoon_count = spoon_count[0]["spoon_total"]

    return render_template("profile.html", user_activities=user_activities, activities=activities, spoon_count=spoon_count)

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
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        id = session["user_id"]

        user = db.execute("SELECT * FROM users WHERE id IS ?", id)

        # Redirect user to index
        return redirect("/profile")

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

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # User reached via POST
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username doesn't already exist
        if len(rows) != 0:
            return apology("username already exists", 400)

        # Ensure passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match", 400)

        else:
            # Hash user's password
            hash = generate_password_hash(request.form.get("password"))

            # Define username
            username = request.form.get("username")

            # Insert new user into database
            db.execute("INSERT INTO users (username, hash) VALUES(?,?)", username, hash)

            # Redirect users to profile page
            return render_template("login.html")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/remove", methods=["GET", "POST"])
@login_required
def remove():
    """Remove activity from user profile"""

    # Define user
    user = session["user_id"]
    activity = request.form.get("activity")

    # "Remove" by setting user_vaule to 0
    db.execute (
        "UPDATE profiles SET user_value = ? WHERE user = ? AND activity = ?", 0, user, activity)

    return redirect("/profile")