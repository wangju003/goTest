from app import create_app
from flask_script import Manager,Server


app = create_app()
manager = Manager(app)

'''
自定义命令
python manage.py runserver
'''
manager.add_command('runserver',Server())



if __name__ == '__main__':
    # manager.run()
    app.run(host='0.0.0.0',port=5000)