import hug

#os.execl('uwsgi --http 0.0.0.0:8080 --wsgi-file server.py --callable __hug_wsgi__')

hug.API(__name__).http.serve(port=8080)
