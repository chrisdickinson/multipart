import datetime
import mimetypes
import cStringIO
import StringIO
from cStringIO import StringIO as strio

def get_content_type_and_body(fields, files={}):
    boundary = '------BOUNDARY-%d'%datetime.datetime.now().microsecond
    crlf = '\r\n'
    items = []

    for key, value in fields.iteritems():
        items += [
            ''.join(['--', boundary]),
            'Content-Disposition: form-data; name="%s"' % str(key),
            '',
            str(value),
        ]
    for filename, value in files.iteritems():
        if isinstance(value, file):
            value = strio(value.read())
        if not isinstance(value, (cStringIO.InputType, StringIO.StringIO)):
            raise ValueError, "Files must be of type <StringIO> or <file>"

        items += [
            ''.join(['--', boundary]),
            'Content-Disposition: form-data; filename="%s"' % str(filename),
            'Content-Type: %s' % (mimetypes.guess_type(filename)[0] or 'application/octet-stream'),
            '',
            value.getvalue(),
        ]
    items += [
        ''.join(['--', boundary, '--']),
        ''
    ]
    body = crlf.join(items)
    content_type = 'multipart/form-data; boundary=%s' % boundary
    return content_type, body 

def get_headers_and_body(fields={}, files={}):
    content_type, body = get_content_type_and_body(fields, files)
    headers = {
        'Content-Type':content_type,
        'Content-Length':str(len(body)),
        'MIME-Version':'1.0',
    }
    return headers, body
