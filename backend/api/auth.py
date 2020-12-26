from flask import Blueprint, session, request, redirect, render_template, url_for
from backend.database.conn import connect
from passlib.hash import sha256_crypt

auth_routes = Blueprint('auth_routes', __name__)

# Endpoint for login
@auth_routes.route('/login', methods=['POST'])
def userLogin():
    conn = connect()
    c = conn.cursor()
    username = request.form['username']
    password = request.form['password']

    c.execute("SELECT * FROM mahasiswa WHERE username = %s", (username,))
    result = c.fetchone()

    if not sha256_crypt.verify(password, result['password']):
        return redirect('/login')

    session['id'] = result['id']

    if result.get('access', None) is not None:
        session['token'] = makeToken(session['id'])
        session['access'] = result['access']
        session['type'] = result['type']
    
        if session['access'] == 'admin':
            return redirect('/superuser')

        elif session['access'] == 'mahasiswa':
            return redirect('/dashboard')

    else:
        session['token'] = makeToken(session['id'])
        return redirect(f"/{result['username']}")



# Endpoint for logging out
@auth_routes.route('/api/logout')
def userLogout():
    session['token'] = None
    session.clear()
    return redirect('/')
