from flask import Flask,render_template,request,redirect,flash


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'



@app.route("/test",methods=['GET'])
def test():
    if request.method == 'GET':
        return render_template('test.html')
    
    
@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('puzzlehome.html')
    if request.method == 'POST':
        if 'submit-info' in request.form:
            # if request.form['submit-info'] == 'burst':
            return render_template('shortgame1.html')
        elif 'learn' in request.form:
            if request.form['learn'] == 'Burst the myth bubble':
                return render_template('learn1.html')
        return request.form     

if __name__ == "__main__":
    app.run(debug=True)