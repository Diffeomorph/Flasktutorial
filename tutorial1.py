from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Goodbye world!"
    
@app.route("/user/<username>")
def xxxx(username):
    return render_template('profile.html',name=username)
    #return "Hello " + username + "!!!"

if __name__ == "__main__":
    app.run(debug=True)

