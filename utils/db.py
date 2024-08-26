from flask import Flask

db = []

def adicionar(name , username, email, hashed_password):
    db.append({"name" : name, "username" : username, "email" : email, "hashed_password" : hashed_password})