from datetime import datetime

from flask import request, redirect, url_for, render_template, Blueprint, flash
from flask_login import login_user, logout_user

from app import db
from models.model_definitions import AdminModel, AnswerModel, QuestionModel

admin_blp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_blp.route('/register', methods=["GET", "POST"])
# This method is very dangerous for security,
# but it has been implemented for convenience of development.
def register():
    # If the user made a POST request, create a new user
    if request.method == "POST":
        user = AdminModel(
            username=request.form.get("username"),
            password=request.form.get("password"),
            email=request.form.get("email"),
            is_admin=True,
            created_at=datetime.now()
        )
        db.session.add(user)
        db.session.commit()

        # Once user account created, redirect them to login route
        return redirect(url_for("admin.login"))
    # Renders sign_up template if user made a GET request
    return render_template("admin/register.html")


@admin_blp.route("/login", methods=["GET", "POST"])
def login():
    # If a post request was made, find the user by
    # filtering for the username
    try:
        if request.method == "POST":
            user = AdminModel.query.filter_by(username=request.form.get("username")).first()
            # Check if the password entered is the
            # same as the user's password
            if user.password == request.form.get("password"):
                # Use the login_user method to log in the user
                login_user(user)
                flash("You are logged in.", "success")
                return redirect(url_for("admin.home"))
            else:
                flash("Incorrect password.", "error")
                return redirect(url_for("admin.login"))
    except AttributeError:
        flash(f"username : {request.form.get("username")} not exist", "error")
        return redirect(url_for("admin.login"))
    except Exception as e:
        flash("Error : {}".format(e), "error")
        return redirect(url_for("admin.login"))
    return render_template("admin/login.html")


@admin_blp.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("admin.home"))


@admin_blp.route("/answer_list", methods=["GET"])
def answer_list():
    # 추후, 페이지네이션 기능 구현 예정
    answers = AnswerModel.query.all()
    return render_template("admin/answer_list.html", answers=answers)


@admin_blp.route("/question_list", methods=["GET"])
def question_list():
    questions = QuestionModel.query.all()
    return render_template("admin/question_list.html", questions=questions)


@admin_blp.route("/")
def home():
    questions = QuestionModel.query.all()
    answers = AnswerModel.query.all()
    return render_template("admin/admin_home.html")