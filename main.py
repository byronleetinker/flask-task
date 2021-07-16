from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/user/<name>')
def user(name):
    if name == "Byron Lee":
        return redirect(url_for('admin', name=name))
    else:
        return redirect(url_for('guest', name=name))


@app.route('/guest/<name>')
def guest(name):
    return "I am a guest user. My name is %s" % name


@app.route('/admin/<name>')
def admin(name):
    return "I am the admin. My name is %s" % name


@app.route('/moola/<int:salary>')
def payment(salary):
    if salary > 10000:
        return redirect("https://www.sahomeloans.com/")
    else:
        return "Sorry, unfortunately you do not qualify."


if __name__ == '__main__':
    app.debug = True
    app.run()