import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

load_dotenv()

Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
url = 'postgresql://{}:{}@{}:{}/{}'
user = os.getenv('postgres_user')
password = os.getenv('postgres_pwd')
host = os.getenv('postgres_host')
port = os.getenv('postgres_port')
database = os.getenv('postgres_database')
url = url.format(user, password, host, port, database)
engine = create_engine(url)

# reflect the tables
Base.prepare(engine, reflect=True, schema='pop_schema')

# mapped classes are now created with names by default
# matching that of the table name.
Users = Base.classes.users
ActivityLogs = Base.classes.activity_logs
# CountryDistricts = Base.classes.country_districts
CountryDivisions = Base.classes.country_divisions
CountryThanas = Base.classes.country_thanas
PMPS = Base.classes.pmps
POPS = Base.classes.pops
Wimaxs = Base.classes.wimaxs
# session = Session(engine)

# # rudimentary relationships are produced
# session.add(Address(email_address="foo@bar.com", user=User(name="foo")))
# session.commit()

# collection-based relationships are by default named
# "<classname>_collection"
# print(u1.address_collection)


db = SQLAlchemy()
