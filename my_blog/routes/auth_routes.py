# routes/auth_routes.py
from flask import render_template, redirect, url_for, flash, request, session
from app import app, db
from forms import LoginForm, RegisterForm
from email_utils import send_email_code
import random, string

@app.route('/login', methods=['GET','POST'])
def login():
    from models import User
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            session['user_id'] = user.id
            session['username'] = user.username
            flash("登录成功", "success")
            return redirect(url_for('home'))
        else:
            flash("用户名或密码错误", "danger")
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.clear()
    flash("已退出登录", "success")
    return redirect(url_for('login'))

@app.route('/register', methods=['GET','POST'])
def register():
    from models import User, EmailCode
    form = RegisterForm()
    if form.validate_on_submit():
        code_record = EmailCode.query.filter_by(email=form.email.data, code=form.code.data).first()
        if not code_record:
            flash("验证码错误或过期", "danger")
        elif form.password.data != form.confirm_password.data:
            flash("两次密码不一致", "danger")
        else:
            user = User(username=form.username.data, email=form.email.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("注册成功！请登录", "success")
            return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/send_code', methods=['POST'])
def send_code():
    from models import EmailCode
    email = request.form.get('email')
    if email:
        code = ''.join(random.choices(string.digits, k=6))
        send_email_code(email, code)
        db.session.add(EmailCode(email=email, code=code))
        db.session.commit()
        return "验证码已发送，请注意查收"
    return "邮箱错误"
