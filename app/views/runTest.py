from flask import Blueprint,jsonify
from app.business.jenkinsAPI import buildJob
runTest = Blueprint('runTest',__name__)

# data = {'responseDemo':'中文字abc123456#$%#'}

# @user.route('/users')
# def index():
#     return jsonify(data)
@runTest.route('/runTest/api/startJenkinsJob/',methods = ['GET','POST'])
def startJenkinsJob():
    '''
    构建自动化测试 automationTest ScriptTest
    :return: 构建状态： 构建中|已构建
    '''
    result = buildJob()
    code ='200'
    result['code']=code
    return jsonify(result)


if __name__ =='__main__':
    from app import create_app
    app = create_app()
    app.run()