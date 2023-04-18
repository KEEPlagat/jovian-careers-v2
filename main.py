from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy text


app = Flask(__name__)



def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row))
    return jobs

@app.route('/')
def index():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


app.run(host='0.0.0.0', port=81, debug=True)
