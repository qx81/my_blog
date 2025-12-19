# routes/blog_routes.py
from flask import render_template
from app import app, login_required

@app.route('/home')
@login_required
def home():
    from models import Post
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
@login_required
def post_detail(post_id):
    from models import Post
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)
