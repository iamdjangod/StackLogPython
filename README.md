<p align="center">
  <a href="https://stacklog.io">
    StackLog
  </a>
  <p align="center">Python package for logging to <a href="https://stacklog.io">StackLog</a></p>
</p>

---

* **[Installation](#installation)**
* **[Setup](#setup)**
* **[Usage](#usage)**
* **[API](#api)**
* **[License](#license)**


## Installation

```bash
$ pip install stacklog
```

## Setup
```python
import logging
from stacklog import StackLogHandler

key = 'YOUR ENCRYPTION KEY HERE'
bucket_id = 'YOUR BUCKET ID HERE'

log = logging.getLogger('stacklog')
log.setLevel(logging.INFO)

options = {
  'hostname': 'unittest',
  'ip': '127.0.0.1',
  'mac': 'F0:EE:FF:F0:EE:FF'
}

# Defaults to False; when True meta objects are searchable
options['index_meta'] = True

test = StackLogHandler(key, bucket_id, options)

log.addHandler(test)

log.warning("Warning message")
log.info("Info message")

```
_**Required**_
* [StackLog Encryption Key](https://stacklog.io/dashboard)

_**Optional**_
* Hostname - *(String)* - max length 32 chars
* MAC Address - *(String)*
* IP Address - *(String)*
* Max Length - *(Boolean)* - formatted as options['max_length']
* Index Meta - *(Boolean)* - formatted as options['index_meta']

## Usage

After initial setup, logging is as easy as:
```python
# Simplest use case
log.info('Sample Log Line')

# Add a custom log type
log.info('Sample Log Line', { 'type': 1 })


# Pass associated objects along as metadata
meta = {
    'foo': 'bar',
    'nested': {
        'nest_text': 'nested text'
    }
}

opts = {
    'meta': meta,
    'level': level,
}

log.info('Sample Log Line', opts)
```

### Usage with File Config

To use `StackLogHandler` with [`fileConfig`](https://docs.python.org/2/library/logging.config.html#logging.config.fileConfig) (e.g., in a Django Project `settings.py` file):

```python
import os
import logging
from stacklog import StackLogHandler #  required to register `logging.handlers.StackLogHandler`

LOGGING = {
    # Other logging settings...
    'handlers': {
        'stacklog': {
            'type': logging.DEBUG,
            'class': 'logging.handlers.StackLogHandler',
            'key': os.environ.get('STACKLOG_ENCRYPTION_KEY'),
            'options': {
                'app': '<app name>',
                'env': os.environ.get('ENVIRONMENT'),
                'index_meta': <True|False>,
            },
        },
    },
    'loggers': {
        '': {
            'handlers': ['stacklog'],
            'type': logging.DEBUG
        },
    },
}
```

(This example assumes you have set environment variables for `ENVIRONMENT` and `STACKLOG_ENCRYPTION_KEY`)

## API

### StackLogHandler(key, bucket_id, [options])
---
#### key

* _**Required**_
* Type: `String`
* Values: `YourAPIKey`

The [StackLog API Key](https://stacklog.io/dashboard) associated with your account.

#### bucket_id

* _**Required**_
* Type: `String`
* Values: `YourBucketID`

The [Bucket ID](https://stacklog.io/buckets) bucket associated with your account.

#### options

##### app

* _Optional_
* Type: `String`
* Default: `''`
* Values: `YourCustomApp`
* Max Length: `32`

The default app passed along with every log sent through this instance.

##### env

* _Optional_
* Type: `String`
* Default: `''`
* Values: `YourCustomEnv`
* Max Length: `32`

The default env passed along with every log sent through this instance.

##### hostname

* _Optional_
* Type: `String`
* Default: `''`
* Values: `YourCustomHostname`
* Max Length: `32`

The default hostname passed along with every log sent through this instance.

##### include_standard_meta

* _Optional_
* Type: `Boolean`
* Default: `False`

Python [`LogRecord` objects](https://docs.python.org/2/library/logging.html#logrecord-objects) includes language-specific information that may be useful metadata in logs.  Setting `include_standard_meta` to `True` automatically populates meta objects with `name`, `pathname`, and `lineno` from the `LogRecord`.  See [`LogRecord` docs](https://docs.python.org/2/library/logging.html#logrecord-objects) for more details about these values.


##### index_meta

* _Optional_
* Type: `Boolean`
* Default: `False`

We allow meta objects to be passed with each line. By default these meta objects are stringified and not searchable, and are only displayed for informational purposes.

If this option is set to True then meta objects are parsed and searchable up to three levels deep. Any fields deeper than three levels are stringified and cannot be searched.

*WARNING* If this option is True, your metadata objects MUST have consistent types across all log messages or the metadata object may not be parsed properly.


##### log type

* _Optional_
* Type: `Int`
* Default: 1
* Values: 1, 2, 3, 4, 5

The default type passed along with every log sent through this instance.

##### verbose

* _Optional_
* Type: `String` or `Boolean`
* Default: `True`
* Values: False or any type

Sets the verbosity of log statements for failures.

##### request_timeout

* _Optional_
* Type: `int`
* Default: `30000`

The amount of time (in ms) the request should wait for StackLog to respond before timing out.

#### options

##### Log Type

* _Optional_
* Type: `Int`
* Default: `Info`
* Values: 1, 2, 3, 4, 5

The log type passed along with this log line.


##### env

* _Optional_
* Type: `String`
* Default: `''`
* Values: `YourCustomEnv`
* Max Length: `32`

The environment passed with this log line.

##### meta

* _Optional_
* Type: `JSON`
* Default: `None`

A meta object for additional metadata about the log line that is passed. Please ensure values are JSON serializable,
values that are not JSON serializable will be removed and the respective keys will be added to the `__errors` string.

##### index_meta

* _Optional_
* Type: `Boolean`
* Default: `False`

We allow meta objects to be passed with each line. By default these meta objects will be stringified and will not be
searchable, but will be displayed for informational purposes.

If this option is turned to true then meta objects will be parsed and will be searchable up to three levels deep. Any fields deeper than three levels will be stringified and cannot be searched.

*WARNING* When this option is true, your metadata objects across all types of log messages MUST have consistent types or the metadata object may not be parsed properly!

##### timestamp

* _Optional_
* Default: `time.time()`

The time in seconds since the epoch to use for the log timestamp. It must be within one day or current time - if it is not, it is ignored and time.time() is used in its place.


## License

MIT © [StackLog](https://stacklog.io/)

*logging Made With Love!*
