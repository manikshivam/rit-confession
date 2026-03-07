from flask import render_template, request, redirect, flash
from flask_mail import Message
from . import core
from ..extensions import mail

@core.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        msg = Message(
            subject="New Contact Form Message",
            recipients=["your_email@gmail.com"]
        )
        msg.body = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}

        Message:
        {message}
        """
        mail.send(msg)

        flash("Thank you for your message! We will get back to you soon.", "success")
        return redirect("/contact")

    return render_template("contact.html")

@core.route("/about")
def about():
    return render_template("about.html")