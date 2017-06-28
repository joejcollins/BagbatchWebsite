from controllers import pages

wsgi_routes = [
    (r'/', pages.home),
    (r'/send', pages.send_email),
    (r'/(\w+)', pages.template),
]
