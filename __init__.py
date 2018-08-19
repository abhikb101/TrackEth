from flask import Flask, render_template, request, redirect, url_for
import task1a
import task2
import task3
import hackathon as hck
app = Flask(__name__)
loc={5:"Chirag PC- tilak nagar", 8:"Abhishek PC- uttam nagar"}
@app.route('/')
def index():
    return redirect(url_for("dashboard"))


@app.route('/dashboard/')
def dashboard():
    return render_template("main.html")

@app.route('/register/', methods=["GET","POST"])
def register():
    if request.method == "POST":
        uid=request.form['uid']
        name=request.form['name']
        data.append(uid)
        data.append(name)
        if True:
            task1a.data(uid,name)
            task2.game()
            return redirect(url_for("dashboard"))
            
    return render_template("register.html")

@app.route('/launch/', methods=["GET","POST"])
def launch():
    task3.start()
    return redirect(url_for("dashboard"))

@app.route('/track/', methods=["GET","POST"])
def track():
    if request.method == "POST":
        uid=request.form['uid']
        data=hck.get(uid)
        print(data)
        if True:
            return render_template("display.html", data = [data, loc])
        
    return render_template("track.html")
@app.route('/header/')
def header():
    return render_template("header.html")
if __name__=='__main__':
	app.run()
