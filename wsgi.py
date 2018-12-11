import hug

@hug.get('/')
def welcome():
    return  'Welcome from hug'

if __name__ == '__main__':
    hug.API(__name__).http.serve()

