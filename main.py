from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/контакти')
def contact():
    return render_template('contact.html')

@app.route('/товари')
def store():
    return render_template('store.html')

@app.route('/прайс')
def prices():
    return render_template('prices.html')

if __name__ == "__main__":
    app.run(debug=True)