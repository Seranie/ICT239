from flask import Flask, render_template, request
from ICT239_qns2b import app, db
from models.Tour import Tour


@app.template_filter('formatdate')
def formatdate(date, formatString="%a, %d %b %Y"):
    return date.strftime(formatString)

@app.route('/')
@app.route('/about')
def index():
    return render_template("about.html")

@app.route('/tours')
def tours():
    return render_template('tours.html', tours=Tour.getAllTours())

if __name__ == '__main__':
    app.run(debug=True)