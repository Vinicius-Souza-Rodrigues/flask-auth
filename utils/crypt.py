from flask import Flask
import bcrypt

def encriptografar(password):
     hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
     return hashed_password