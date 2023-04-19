from sqlalchemy import create_engine, text
import os

DATABASE_URL = os.getenv('DB_URL')
# Set SSL parameters
ssl_args = {"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}}
# create the engine
engine = create_engine(DATABASE_URL, connect_args=ssl_args)


#reading data from datatabase
def load_jobs_from_db():
  with engine.connect() as conn:
    stmt = text("SELECT * FROM jobs")
    result = conn.execute(stmt)
    jobs = [row for row in result]
  return jobs


#load single job
def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :id"),
                          {"id": id})
    row = result.fetchone()
    if row is None:
      return None
    else:
      columns = result.keys()
      return dict(zip(columns, row))


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(
      "INSERT INTO applications(job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES(:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
    )
    conn.execute(
      query, {
        "job_id": job_id,
        "full_name": data['full_name'],
        "email": data['email'],
        "linkedin_url": data['linkedin_url'],
        "education": data['education'],
        "work_experience": data['work_experience'],
        "resume_url": data['resume_url']
      })
