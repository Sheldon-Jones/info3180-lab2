from app import app
from flask import render_template, request, redirect, url_for, flash
from datetime   import datetime, date


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Sheldon Jones")


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


"""returns the month and year from date provided"""
def format_date_joined(date):
        return date.strftime("%B, %Y")

# creating view function
@app.route('/profile/')
def view_profile():
    """Render user's profile."""

    
    date_joined = date(2025, 12, 4)  
    formatted_date = format_date_joined(date_joined)

    return render_template('profile.html', fullName= "George Jones", username= "oneGjones", email="onegjones@helloworld",
        location= "Portmore, St. Catherine", joined_date= formatted_date,
        bio= "I like playing football and doing art. It would be nice to meet friends who like those as well",
        num_post= "15",
        num_following= "23",
        num_followers= "1236",)
  
    
