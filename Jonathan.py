from flask import Flask, jsonify, abort, make_response, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')


if __name__ == '__main__':
    app.run()
