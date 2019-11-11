from flask import Flask, render_template, redirect, url_for, request
		
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/faq')
def faq():
    return redirect(url_for('faq.html'))

@app.route('/login', methods=['POST'])
def login():
    form = request.form
    print(f"USERNAME: {form.get('username')}")
    print(f"PASSWORD: {form.get('password')}")
    return index()


if __name__ == '__main__':
    app.run(debug=True)