from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='C:/Users/alishern/PycharmProjects/WorldOfGames')


@app.route('/')
def score_server():
    score = open('Scores.txt', 'r').read()
    return render_template("score_web.html", variable1=score)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=8080)
