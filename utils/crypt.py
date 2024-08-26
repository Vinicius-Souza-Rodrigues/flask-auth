from flask import Flask
import bcrypt
#TEMPORARIO
from utils.db import db

def encriptografar(password):
     hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
     return hashed_password

def verificar_crypto(password):
     #necessita revisao e mudança!
     for user in db:
          hashed_password = bcrypt.checkpw(password, ['user'])