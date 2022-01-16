def hello(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    body = environ['QUERY_STRING']
    body =( '\n'.join(body.split('&'))+ '\n').encode('utf-8')
    start_response(status, headers)
    return body
