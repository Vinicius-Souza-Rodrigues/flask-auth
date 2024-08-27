db = []
def adicionar(name , username, email, hashed_password):
    db.append({"name" : name, "username" : username, "email" : email, "password" : hashed_password})

name = 'pedro'
username = 'pedro123'
email = 'teste@gmail.com'
hashed_password = '123'

adicionar(name, username, email, hashed_password)
for a in db:
    print(a['name'])