from flask import Flask
def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='blackballslol'



    from .views import views
    from .auths import auths

    app.register_blueprint( views ,url_prefix='/abc')
    app.register_blueprint( auths ,url_prefix='/')

    return app