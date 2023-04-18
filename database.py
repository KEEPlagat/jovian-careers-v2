from sqlalchemy import create_engine, text
import os

# Get database credentials from environment variables
DATABASE = 'joviancareers'
USER = 'eolyi4s9kr15eryqb7im'
PASSWORD = 'pscale_pw_CkdJKS61wddkMcTnhdairHJZdCTOyVkLPUVQYInSdPA'
HOST = 'aws.connect.psdb.cloud'
PORT = 3306  # default port for MySQL

# Build the database URL
DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

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
