from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', page='home')


@app.route('/about')
def about():
    return render_template('about.html', page='about')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    submitted = False
    if request.method == 'POST':
        submitted = True
    return render_template('contact.html', page='contact', submitted=submitted)


@app.route('/health')
def health():
    return {'status': 'ok'}, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
