from flask import render_template
from flask_mail import Message
from threading import Thread
from app import app, db, mail
from app.models import UserMessages


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()


def send_activation_email(email, confirm_url):
    send_email(
        'Bitte bestätigen Sie Ihre E-Mail Adresse',
        sender=app.config['ADMINS'][0],
        recipients=[email],
        text_body=render_template(
            'email/activate.txt',
            confirm_url=confirm_url),
        html_body=render_template(
            'email/activate.html',
            confirm_url=confirm_url))


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email(
        'KernTrafo Passwortrücksetzung',
        sender=app.config['ADMINS'][0],
        recipients=[
            user.email],
        text_body=render_template(
            'email/reset_password.txt',
            user=user,
            token=token),
        html_body=render_template(
            'email/reset_password.html',
            user=user,
            token=token))


def send_contact_email(name, email, message):
    send_email(
        'KernTrafo Kontaktanfrage',
        sender=app.config['ADMINS'][0],
        recipients=[
            app.config['CONTACT_RECIPIENT'][0]],
        text_body=render_template(
            'email/contact.txt',
            name=name,
            email=email,
            message=message),
        html_body=render_template(
            'email/contact.html',
            name=name,
            email=email,
            message=message))


def send_user_message(email, subject, message):
    send_email(
        'KernTrafo Job Anfrage',
        sender=app.config['ADMINS'][0],
        recipients=[
            app.config['REQUEST_RECIPIENT'][0]],
        text_body=render_template(
            'email/job_request.txt',
            email=email,
            subject=subject,
            message=message),
        html_body=render_template(
            'email/job_request.html',
            email=email,
            subject=subject,
            message=message))


def send_success_email(user):
    send_email('KernTrafo Datenübermittlung',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/success.txt'),
               html_body=render_template('email/success.html')
               )


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)
