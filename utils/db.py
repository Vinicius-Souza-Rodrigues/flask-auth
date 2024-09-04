from flask import Flask
import os

db = []

def adicionar(name , username, email, hashed_password):
    current_id = os.urandom(6)

    account_info = {"saldo" : 1.0, "user_id" : current_id}
    
    #DAO
    db.append({"name" : name, "username" : username, "email" : email, "hashed_password" : hashed_password, "account_info" : account_info})
    print(db)