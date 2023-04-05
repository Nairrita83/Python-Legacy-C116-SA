from flask import Flask,render_template
app = Flask(__name__)
@app.route("/SA")
def student_webpage():
    name = "John"
    return render_template("SA.html", student_name = name)

app.run(debug=True)