import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    id = sa.Column(sa.Integer, primary_key=True)
    company = sa.Column(sa.String(50))
    name = sa.Column(sa.String(50))
    metadata = sa.Column(sa.JSONB)
