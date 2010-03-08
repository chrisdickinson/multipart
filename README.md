Multipart
=========

This is just a stupidly simple collection of functions (well, let's be honest,
there's only two functions here) that help out when you're trying to use
`httplib2` to POST or PUT form data that includes files.

the two functions are as follows:

* `get_content_type_and_body`
* `get_headers_and_body`

you'll usually want to use `get_headers_and_body`. you supply two dicts --
one of the fields you want to send, and one of the files you want to send,
where the keys of the file dict correspond to file names, and the values of
the file dict are either `file` objects or `StringIO` objects. It returns
a mime-encoded body and a set of headers. You'll need to set your own
user agent and Http methods.

Tests are forthcoming; pretty much everything is forthcoming; this
release is so rough that nine out of ten Hell's Angels show unwavering
respect for the code. It would probably have a handlebar mustache if it
could grow one.
