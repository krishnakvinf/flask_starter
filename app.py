from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html', user_agent=user_agent)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
