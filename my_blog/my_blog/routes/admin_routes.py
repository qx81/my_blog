# routes/admin_routes.py
from flask import render_template, redirect, url_for, flash, request
from app import app, db, login_required
from forms import PostForm

@app.route('/admin')
@login_required
def admin():
    from models import Post
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('admin_list.html', posts=posts)

@app.route('/admin/new', methods=['GET','POST'])
@login_required
def admin_new():
    from models import Post
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        flash('文章发布成功！', 'success')
        return redirect(url_for('admin'))
    return render_template('admin_form.html', form=form, action='新增文章')

@app.route('/admin/edit/<int:post_id>', methods=['GET','POST'])
@login_required
def admin_edit(post_id):
    from models import Post
    post = Post.query.get_or_404(post_id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('文章更新成功！', 'success')
        return redirect(url_for('admin'))
    return render_template('admin_form.html', form=form, action='编辑文章')

@app.route('/admin/delete/<int:post_id>', methods=['POST'])
@login_required
def admin_delete(post_id):
    from models import Post
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('文章已删除', 'success')
    return redirect(url_for('admin'))
