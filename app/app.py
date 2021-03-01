from flask import Flask
from config import Configuration
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(Configuration) # передавать в словарь app.config настройки приложения через 
                                        #метод from_object
db = SQLAlchemy(app)# создать экземаляр базы данных


migrate = Migrate(app,db) # создание миграции
manager = Manager(app)
manager.add_command('db',MigrateCommand) #регистрация команды для консоли

### ADMIN ###
from models import *
admin =Admin(app) # создание админки
admin.add_view(ModelView(Post,db.session))
admin.add_view(ModelView(Tag,db.session))