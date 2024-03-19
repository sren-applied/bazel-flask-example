import models
import pandas as pd
from flask import Blueprint
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

home = Blueprint("home", __name__, url_prefix="/")


@home.route("/")
def hello():
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [11, 33, 22]}
    )
    return df.to_json()

@home.route("/register_user", methods=['POST'])
def register_user():
    db = app.config["APPLICATION_DB"]
    r = flask.request.get_json()
    company = r.get("company")
    name = r.get("name")
    metadata = eval(r.get("metadata"))
    user = models.User(company=company, name=name, metadata=metadata)
    db.session.add(user)
    db.commit()
    return flask.jsonify({"status": "ok", "user_id": user.id})

def get_user_by_id(user_id):
    db = app.config["APPLICATION_DB"]
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    user_data = db.session.execute(query).first()
    return user_data

@home.route("/get_users", methods=['GET'])
def get_users():
    db = app.config["APPLICATION_DB"]
    query = text("SELECT id FROM users")
    user_ids = db.session.execute(query).all()
    return user_ids

@home.route("/get_user_data/<user_id>", methods=['GET'])
    return get_user_by_id(user_id)

@home.route("/display_user/<user_id>", methods=['GET'])
def display_user():
    user_data = get_user_by_id(user_id)
    return """
    <html>
      <head>
        <title>Users</title>
      </head>
      <body>
        <span>Company: """ + user_data.company + """</span><br>
        <span>Name: """ + user_data.name + """</span><br>
        <span>Metadata: """ + user_data.metadata + """</span><br>
      </body>
    </html>
    """


@app.route('/error_page')
def error_page():
    return "404"
