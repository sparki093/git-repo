from flask import Flask
from config import Configuration


from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(Configuration) # передавать в словарь app.config настройки приложения через 
                                        #метод from_object
db = SQLAlchemy(app)# создать экземаляр базы данных

