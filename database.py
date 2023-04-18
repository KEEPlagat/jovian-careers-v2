from sqlalchemy import create_engine, text

DATABASE = 'joviancareers'
USER = 'eolyi4s9kr15eryqb7im'
PASSWORD = 'pscale_pw_CkdJKS61wddkMcTnhdairHJZdCTOyVkLPUVQYInSdPA'
HOST = 'aws.connect.psdb.cloud'
PORT = 3306  # default port for MySQL

DATABASE_URL = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

ssl_args = {"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}}
# create the engine
engine = create_engine(DATABASE_URL, connect_args=ssl_args)

try:
  with engine.connect() as conn:
   print("Connected successfully!")

except Exception as ex:
  print(f"Connection failed: {str(ex)}")
