from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = 'Abhinav'  # Change this in production

# Mail configuration (update with your details)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'corspus.1999@gmail.com'  # Update with your email
app.config['MAIL_PASSWORD'] = 'Abhinav@16'     # Update with your app password
app.config['MAIL_DEFAULT_SENDER'] = 'corspus.1999@gmail.com'

mail = Mail(app)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Send email
        msg = Message(
            subject=f"Portfolio Contact from {name}",
            recipients=['corspus.1999@gmail.com'],  # Update with your email
            body=f"Name: {name}\nEmail: {email}\nMessage: {message}"
        )
        
        try:
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash('There was an error sending your message. Please try again later.', 'error')
            print(str(e))
            
        return render_template('contact.html')
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
