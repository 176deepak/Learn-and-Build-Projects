from flask import Flask, request
from flask.templating import render_template
import model
app = Flask(__name__, template_folder='templates')


@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/iris/', methods=['GET','POST'])
def iris():
    pred = None
    if request.method == "POST":
        s_l=request.form["sl"]
        s_w=request.form["sw"]
        p_l=request.form["pl"]
        p_w=request.form["pw"]
        n = model.species(s_l,s_w,p_l,p_w)
        pred = n
    return render_template("species_prediction.html", pred=pred)


@app.route('/cancer/', methods=['GET','POST'])
def cancer():
    pred = None
    if request.method == "POST":
        CT = request.form["CT"]
        uSize = request.form["uSize"]
        uShape = request.form["uShape"]
        mA = request.form["mA"]
        SECS = request.form["SECS"]
        BN = request.form["BN"]
        BC = request.form["BC"]
        NN = request.form["NN"]
        Mit = request.form["Mit"]
        n = model.cancer(CT,uSize,uShape,mA,SECS,BN,BC,NN,Mit)
        pred = n
    return render_template("cancer_prediction.html", pred=pred)


@app.route('/score/', methods=['GET','POST'])
def score():
    pred = None
    if request.method == "POST":
        hrs=request.form["hour"]
        n = model.score(hrs)
        pred = n
    return render_template("score_prediction.html",pred=pred)


if __name__ == "__main__":
    app.run(debug=True)





