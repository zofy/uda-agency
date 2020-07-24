import os

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# SQLALCHEMY_DATABASE_URI = 'postgresql://patrik@localhost:5432/agency'
SQLALCHEMY_DATABASE_URI = 'postgres://frwjonqxllkeax:dbcfdfff06c69309bebd5f454588f37f780dce261a538d603ee402b0700e6d72@ec2-52-22-216-69.compute-1.amazonaws.com:5432/dco6kaopaoa91p'
SQLALCHEMY_TRACK_MODIFICATIONS = False
