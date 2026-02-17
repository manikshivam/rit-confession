from flask import render_template, redirect, url_for, flash,request
from flask_login import login_required, current_user
from . import posts_bp
from .forms import PostForm
from ..models import Post
from ..extensions import db

@posts_bp.route("/")
def index():
    page = request.args.get('page', 1, type=int)
    #posts = Post.query.all()
    posts = Post.query.order_by(Post.id.desc()).paginate(
        page=page,
        per_page=10,
        error_out=False
    )

    return render_template("index.html", posts=posts)

@posts_bp.route("/like/<int:post_id>", methods=["POST"])
def like_post(post_id):
    post = Post.query.get_or_404(post_id)
    post.likes_count += 1
    db.session.commit()
    return jsonify({"likes": post.likes_count})


@posts_bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,
                    content=form.content.data,
                    user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("posts.index"))
    return render_template("posts/create.html", form=form)


@posts_bp.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit(id):
    post = Post.query.get_or_404(id)
    form = PostForm(obj=post)

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        return redirect(url_for("posts.index"))

    return render_template("posts/edit.html", form=form)


@posts_bp.route("/delete/<int:id>")
@login_required
def delete(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("posts.index"))


