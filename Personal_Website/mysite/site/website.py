from flask import Flask, render_template

app=Flask(__name__)

@app.route('/') #This refers to the homepage
def home(): #The function defines what the webpage will do
    return render_template("home.html")

@app.route('/about/') #refers to the about page
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
""" Every module in Python has a special attribute called __name__. The value of __name__  attribute is set to '__main__'  
    when module run as main program. Otherwise, the value of __name__  is set to contain the name of the module. """



