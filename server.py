from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'SecretClubhousePassword'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if len(request.form['name']) < 1:
        flash("Error: Name needs to contain at least one letter.")
        return render_template('index.html')
    elif len(request.form['textarea']) > 120:
        flash("Error: Comments are to be 120 characters max.")
        return render_template('index.html')
    else:
        return render_template('result.html',
        name=request.form['name'],
        location=request.form['location'],
        language=request.form['language'],
        comment=request.form['textarea'])
    return redirect('/')

@app.route('/back')
def back():
    return redirect('/')

app.run(debug=True)
