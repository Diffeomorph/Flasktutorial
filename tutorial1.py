from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Goodbye world!"

# returns an HTML webpage    
@app.route("/user/<username>")
def xxxx(username):
    return render_template('profile.html',name=username)
    #return "Hello " + username + "!!!"

# returns a piece of data in json format
@app.route("/lotsofdata")
def people():
    my_people = {'Alice' :25,
                 'Bob': 21,
                 'Charlie': 20,
                 'Doug': 28}
    return jsonify(my_people)
    
if __name__ == "__main__":
    app.run(debug=True)

