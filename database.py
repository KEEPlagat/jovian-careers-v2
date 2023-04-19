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
