from flask import Flask,render_template,request
app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def home():
    return render_template('home.html')
@app.route("/x")
def index():
     return render_template("ind.html")
@app.route('/submitform', methods=['POST'])
def submitform():
    name = request.form.get('name')
    email = request.form.get('Email')
    phone = request.form.get('phone')
    clg = request.form.get('clg')
    course = request.form.get('course')
    obj = request.form.get('obj')
    with open('students.csv','a') as f:
        f.write(f"{name},{email},{phone},{clg},{course},{obj}\n")
    return render_template('submit.html')



