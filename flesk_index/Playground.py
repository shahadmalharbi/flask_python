from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template("index.html",times=3)

@app.route('/play/<x>')
def indexX(x):
    return render_template("index.html", times=int(x))

@app.route('/play/<x>/<color>')
def indexXColor(x,color):
    return render_template("index.html",times = int(x),color = color)

if __name__=="__main__":
    app.run(debug=True)




