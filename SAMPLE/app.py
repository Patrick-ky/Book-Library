from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "password"

@app.route('/')
def home():
    return render_template('homepage.html')

if __name__ =="__main__":
    app.run(debug = True, port = 1234)
    
@app.route('/home', methods = ['GET', 'POST'])
def home():
    data=request.form
    print(data)
    return render_template('homepage.html')