from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)


@app.route('/')
def index():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


app.run(host='0.0.0.0', port=81, debug=True)
