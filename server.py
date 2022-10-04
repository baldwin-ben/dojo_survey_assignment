from flask import Flask, render_template, request, redirect, session # don't forget to import redirect!
app = Flask(__name__)
app.secret_key = "There are no secrets on GitHub" #tp use sessions we need a secret key

@app.route('/')
def main():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    session['data'] = { #adding a key to the session dictionary called data that is storing the form data.
        'name':request.form['name'],
        'location':request.form['location'],
        'language':request.form['language'],
        'comment':request.form['comment']
    }
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('show.html')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.