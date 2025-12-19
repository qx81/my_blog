from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)

# 数据库配置
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_HOST}/{config.MYSQL_DATABASE}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = config.SECRET_KEY

db = SQLAlchemy(app)

# 登录保护装饰器
from functools import wraps
from flask import session, redirect, url_for, flash

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("请先登录", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# 导入路由
if __name__ == "__main__":
    from routes.blog_routes import *
    from routes.admin_routes import *
    from routes.auth_routes import *
    app.run(debug=True)

with app.app_context():
    db.create_all()

# 根路径重定向到登录
@app.route('/')
def index_redirect():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
