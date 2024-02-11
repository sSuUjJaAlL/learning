from flask import Blueprint
views=Blueprint('views',__name__)

@views.route('/')
def home_page():
    return '<h1>This is home page</h1>'

@views.route('/sujal')
def sujal_page():
    return '<h1>This is sujal page</h1>'
