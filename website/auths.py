from flask import Blueprint
auths=Blueprint('auths',__name__)

@auths.route('/signup')
def sign_page():
    return '<h1>This is sign page</h1>'

def login_page():
    return '<h1>This is login page</h1>'

def logout_page():
    return '<h1>This is logout page</h1>'


