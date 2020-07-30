import logging
from stacklog import StackLogHandler

key = '87C8BFFA-1BB9-40BC-9985-167162F800DC'
bucket_id = '7C329EF3-E657-402D-A52F-3533600980DB'

log = logging.getLogger('stacklog')
log.setLevel(logging.INFO)
log.setLevel(logging.DEBUG)

options = {
    'hostname': 'unittest',
    'ip': '10.0.1.1',
    'mac': 'C0:FF:EE:C0:FF:EE'
}

# Defaults to False; when True meta objects are searchable
options['index_meta'] = True

test = StackLogHandler(key, bucket_id, options)

log.addHandler(test)


log.fatal("Fatal Error on StackLog API")