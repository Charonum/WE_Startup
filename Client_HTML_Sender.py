from flask import Flask, render_template
import ctypes

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("results.html")


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    app.run(debug=True)
