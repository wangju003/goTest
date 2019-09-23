from flask import Blueprint,jsonify
user = Blueprint('user',__name__)

data = {'responseDemo':'中文字abc123456#$%#'}

@user.route('/users')
def index():
    return jsonify(data)

if __name__ =='__main__':
    from app import create_app
    app = create_app()
    app.run()