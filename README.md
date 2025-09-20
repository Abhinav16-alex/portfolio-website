Portfolio Website with Flask
A personal portfolio website built with Flask, featuring a responsive design, contact form, and multiple sections to showcase skills and projects.

Features
Responsive Design: Works on all device sizes

Contact Form: Functional contact form with email capabilities

Multiple Sections: Home, Projects, About, and Contact pages

Modern UI: Clean and professional design with smooth animations

Flash Messages: User feedback for form submissions

Project Structure
text
portfolio-website/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css     # All styling for the website
│   ├── js/
│   │   └── script.js     # JavaScript for interactive elements
│   └── images/
│       └── profile.jpg   # Profile image (replace with your own)
└── templates/
    ├── base.html         # Base template with common elements
    ├── index.html        # Home page
    ├── projects.html     # Projects showcase
    ├── about.html        # About me section
    └── contact.html      # Contact form page
Setup Instructions
Clone the repository:

bash
git clone https://github.com/your-username/portfolio-website.git
cd portfolio-website
Create a virtual environment (recommended):

bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
pip install -r requirements.txt
Configure email settings (for contact form):

Open app.py

Update the email configuration with your details:

python
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_app_password'
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'
Run the application:

bash
python app.py
View the website: Open your browser and go to http://localhost:5000

Customization
Personal Information:

Update content in the HTML files with your information

Replace static/images/profile.jpg with your own photo

Styling:

Modify static/css/style.css to change colors, fonts, and layout

Projects:

Edit templates/projects.html to showcase your actual projects

Deployment
To Heroku:
Create a Procfile with:

text
web: gunicorn app:app
Install gunicorn:

bash
pip install gunicorn
Update requirements.txt:

bash
pip freeze > requirements.txt
Deploy to Heroku using Git or the Heroku CLI

To PythonAnywhere:
Upload all files to your PythonAnywhere account

Configure a web app with Flask

Set the working directory to your project folder

Reload the web app

Technologies Used
Backend: Flask, Python

Frontend: HTML5, CSS3, JavaScript

Styling: Custom CSS with Flexbox and Grid

Icons: Font Awesome

Fonts: Google Fonts (Poppins)

Contact Form Setup
For the contact form to work properly:

Enable less secure apps in your Gmail account or use app-specific passwords

Alternatively, use a different email service by updating the SMTP settings

License
This project is open source and available under the MIT License.

Contributing
Feel free to fork this project and customize it for your own portfolio. If you make improvements, consider submitting a pull request!
