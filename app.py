from flask import Flask, render_template, request
import difflib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    if 'text1' in request.form and 'text2' in request.form:
        text1 = request.form['text1']
        text2 = request.form['text2']
        similarity_ratio = difflib.SequenceMatcher(None, text1, text2).ratio()
        return render_template('result.html', similarity_ratio=similarity_ratio)

    return render_template('index.html', error="Please provide both texts for comparison.")

if __name__ == '__main__':
    app.run(debug=True)
