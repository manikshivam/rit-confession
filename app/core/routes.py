import os
import mailtrap as mt
from flask import render_template, request, redirect, flash
from . import core
from config import Config

@core.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        mail = mt.Mail(
            sender=mt.Address(
                email="hello@demomailtrap.co",
                name="Website Contact"
            ),
            to=[mt.Address(email="manikshivam708@gmail.com")],
            subject=f"New message from {name}",
            text=f"""
Name: {name}
Email: {email}
Phone: {phone}

Message:
{message}
""",
            category="Contact Form",
        )

        client = mt.MailtrapClient(token=Config.MAILTRAP_API_TOKEN)
        client.send(mail)

        flash("Message sent successfully!", "success")
        return redirect("/contact")

    return render_template("contact.html")

@core.route("/about")
def about():
    return render_template("about.html")