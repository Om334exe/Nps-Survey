from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple in-memory list to store survey responses
survey_responses = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/survey', methods=['POST'])
def survey():
    # Get the NPS score from the form
    nps_score = int(request.form['nps_score'])

    # Store the response in the list
    survey_responses.append(nps_score)

    return redirect(url_for('thank_you'))


@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple in-memory list to store survey responses
survey_responses = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/survey', methods=['POST'])
def survey():
    # Get the NPS score from the form
    nps_score = int(request.form['nps_score'])

    # Store the response in the list
    survey_responses.append(nps_score)

    return redirect(url_for('thank_you'))


@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple in-memory list to store survey responses
survey_responses = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/survey', methods=['POST'])
def survey():
    # Get the NPS score from the form
    nps_score = int(request.form['nps_score'])

    # Store the response in the list
    survey_responses.append(nps_score)

    return redirect(url_for('thank_you'))


@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')


if __name__ == '__main__':
    app.run(debug=True)
