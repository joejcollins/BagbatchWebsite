import webapp2
import routes
import config
import logging

'''
Handlers to deal with the 404 and 500 exceptions should they occur
'''
def handle_404(request, response, exception):
    logging.exception(exception)
    template_values = {'title': 'Page Not Found!',
                       'header': 'Page Not Found!',}
    template = config.jinja_environment.get_template('errors/404.html')
    response.out.write(template.render(template_values))
    response.set_status(404)

def handle_500(request, response, exception):
    logging.exception(exception)
    template_values = {'title': 'Server Error!',
                       'header': 'Server Error!',}
    template = config.jinja_environment.get_template('errors/500.html')
    response.out.write(template.render(template_values))
    response.set_status(500)

'''
Entrance to the application which sets up the routes and configuration
'''
wsgi_app = webapp2.WSGIApplication(routes=routes.wsgi_routes, debug=True, config=config.wsgi_config)

wsgi_app.error_handlers[404] = handle_404
wsgi_app.error_handlers[500] = handle_500
