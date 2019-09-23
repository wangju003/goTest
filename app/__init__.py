from flask import Flask

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# from app.views.user import user
from app.views.runTest import runTest
#创建app
def create_app():
    app = Flask(__name__)
    app.debug=True
    #设置配置文件,如果响应体中包含中文，不配置此2项，会出现乱码
    app.config['JSON_AS_ASCII'] = False  # 指定json编码格式 如果为False 就不使用ascii编码
    app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"  # 指定浏览器渲染的文件类型，和解码格式；

    #注册蓝图
    # app.register_blueprint(user)
    app.register_blueprint(runTest)

    return app

