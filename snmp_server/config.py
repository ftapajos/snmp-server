# SNMP server response config example

def my_response(params):
	res = '|'.join(params.oid.split('.'))
	return octet_string('response: {}'.format(res))


DATA = {
    '1.3.6.1.4.1.1.1.0': integer(12345),
    '1.3.6.1.4.1.1.2.0': bit_string('\x12\x34\x56\x78'),
    '1.3.6.1.4.1.1.3.0': octet_string('test'),
    '1.3.6.1.4.1.1.4.0': null(),
    '1.3.6.1.4.1.1.5.0': object_identifier('1.3.6.7.8.9'),
    '1.3.6.1.4.1.1.6.0': real(1.2345),
    '1.3.6.1.4.1.1.7.0': double(12345.2345),
    # integer enumeration
    '1.3.6.1.4.1.1.8.0': integer(1, enum=[1, 2, 3]),
    # notice the wildcards in the next OIDs:
    '1.3.6.1.4.1.1.?.0': lambda f: octet_string('? {}'.format(f.oid)),
    '1.3.6.1.4.1.2.*': lambda f: octet_string('* {}'.format(f.oid)),
    # lambda or function, with single oid argument, can be used for response generation
    '1.3.6.1.4.1.1001.1.0': my_response,
    '1.3.6.1.4.1.1002.1.0': lambda f: octet_string('-'.join(f.oid.split('.'))),
}

# One thread will be available for each item in HOSTS.
# Each thread will bind to this host and it will be available
# to responses as params.host
HOSTS = [
        '0.0.0.0',
]
