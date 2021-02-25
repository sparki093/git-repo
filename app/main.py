from app import app
import view
from app import db
from posts.blueprint import posts

app.register_blueprint(posts,url_prefix='/blog') # регитсрация блюпринт

if __name__ =='__main__':
    app.run() #запуск сервера фласк