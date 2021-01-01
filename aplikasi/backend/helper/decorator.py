from flask import Flask, jsonify, request, Response, redirect, session, make_response
from functools import wraps
from instance.config import SECRET_KEY, PERMANENT_SESSION_LIFETIME
import jwt


def check_for_token(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        token = request.args.get("token")
        if not token:
            return jsonify({"message": "Missing Token"}), 403
        try:
            data = jwt.decode(token, SECRET_KEY)
        except:
            return jsonify({"message": "invalid token"}), 403
        return wrapped


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = dict(session).get("id", None)
        if user:
            return f(*args, **kwargs)

        return redirect("/logout")

    return decorated_function
