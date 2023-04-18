from flask import Flask, render_template, jsonify


app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': "Data analyst",
  'location': "kenya",
  'salary': "Ksh 3200"
}, {
  'id': 2,
  'title': "Data analyst",
  'location': "kenya",
  'salary': "Ksh 3200"
}, {
  'id': 3,
  'title': "Data analyst",
  'location': "kenya",
  'salary': "Ksh 3200"
}]


@app.route('/')
def index():
  return render_template('home.html', jobs=JOBS)


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


app.run(host='0.0.0.0', port=81, debug=True)
