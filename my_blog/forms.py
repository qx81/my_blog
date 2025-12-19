from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, EmailField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('标题', validators=[DataRequired()])
    content = TextAreaField('内容', validators=[DataRequired()])
    submit = SubmitField('提交')

class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('登录')

class RegisterForm(FlaskForm):
    email = EmailField('邮箱', validators=[DataRequired()])
    code = StringField('验证码', validators=[DataRequired()])
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    confirm_password = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField('注册')
