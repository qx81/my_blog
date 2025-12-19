#my_blog

这是一个基于Flask框架开发的简单博客系统，支持用户注册、登录、发布文章、编辑文章和删除文章等功能。

## 功能特点

- 用户认证：支持注册、登录和退出功能
- 文章管理：支持发布、查看、编辑和删除文章
- 后台管理：提供文章管理界面
- 响应式设计：使用Bootstrap实现响应式布局，适配不同设备

## 技术栈

- 后端：Python + Flask
- 前端：HTML + Bootstrap 5
- 数据库：MySQL
- ORM：SQLAlchemy

## 项目结构

```
my_blog/
├── app.py                 # 应用入口
├── config.py              # 配置文件
├── forms.py               # 表单定义
├── models.py              # 数据模型
├── email_utils.py         # 邮件发送工具
├── routes/                # 路由模块
│   ├── blog_routes.py     # 博客相关路由
│   ├── admin_routes.py    # 管理员相关路由
│   └── auth_routes.py     # 认证相关路由
└── templates/             # 模板文件
    ├── base.html          # 基础模板
    ├── index.html         # 首页
    ├── post.html          # 文章详情页
    ├── login.html         # 登录页
    ├── register.html      # 注册页
    ├── admin_list.html    # 文章管理列表
    └── admin_form.html    # 文章编辑表单
```

## 安装与配置

1. 克隆仓库

```bash
git clone <仓库地址>
cd my_blog
```

2. 安装依赖

```bash
pip install flask flask-sqlalchemy flask-wtf pymysql
```

3. 配置数据库

修改`config.py`文件，设置你的MySQL数据库信息：

```python
MYSQL_HOST = '127.0.0.1'
MYSQL_USER = '你的数据库用户名'
MYSQL_PASSWORD = '你的数据库密码'
MYSQL_DATABASE = 'my_blog'  # 数据库名称
SECRET_KEY = 'your_secret_key'  # 替换为你的密钥
```

4. 配置邮件服务（用于注册验证码）

修改`email_utils.py`文件，设置你的SMTP服务器信息：

```python
SMTP_SERVER = "smtp.qq.com"  # 邮件服务器
SMTP_PORT = 587              # 端口
SMTP_USER = "your_email@qq.com"  # 你的邮箱
SMTP_PASS = "your_email_password"  # 邮箱密码或授权码
```

5. 运行应用

```bash
python app.py
```

6. 访问应用

在浏览器中访问 `http://127.0.0.1:5000` 即可打开博客系统

## 使用说明

1. 首先注册一个账号
2. 登录系统后可查看文章列表
3. 点击"新增文章"可发布新文章
4. 在文章管理页面可对文章进行编辑和删除操作

## 许可证

[MIT](LICENSE)
