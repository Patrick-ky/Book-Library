from flask import Blueprint, render_template,request,flash

auth = Blueprint ('auth', __name__)

@auth.route('/home', methods = ['GET', 'POST'])
def home():
    data=request.form
    print(data)
    return render_template('homepage.html')