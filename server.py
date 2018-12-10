import hug

@hug.get('/')
def welcome():
    return  'Welcome from hug'
