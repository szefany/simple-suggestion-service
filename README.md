# Simple Suggestion (Auto-Complete) Service

A simple django-based suggestion service for auto-completion on Trie.

## Deployment

**Fastest Deployment (but dirty)**

Requirements:

* memcached
* python-pip
* Other python packages in `deploy/requirements`

Deployment: (super privileges might be required for installation)

```shell
cd deploy && ./deploy.sh
```

Start:

```shell
cd deploy && ./start.sh
```

A better way is to run the service within virtualenv/gunicorn/supervisor/systemd.

## APIs

The service provides the following HTTP APIs.

**Create a service**
```
/service/create/
    Method: POST
    Params:
        service: string, the service name
    Returns:
        Token of the service.
```

**Create a snippet in service**
```
/snippet/create/
    Method: POST
    Params:
        service: string, the service name
        snippet: string, the snippet being inserted to the service
        token: string, token of the service
```

**Delete a service**
```
/service/delete/
    Method: POST
    Params:
        service: string, the service name
        token: string, token of the service
```

**Delete a snippet from a service**
```
/snippet/delete/
    Method: POST
    Params:
        service: string, the service name
        snippet: string, the snippet to be removed
        token: string, token of the service
```

**Query for suggestions**
```
/query/
    Method: GET
    Params:
        service: string, the service name
        query: string, the queried string
        max_count: int, max number of suggested results
    Returns:
        A JSON list of the results.
```
