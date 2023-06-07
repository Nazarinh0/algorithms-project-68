import pytest
from router.router import MakeRouter

static_routes = [
    {
        'method': 'GET',
        'path': '/courses',
        'handler': lambda params: 'all courses'
    },
    {
        'method': 'POST',
        'path': '/courses',
        'handler': lambda params: 'create course'
    },
    {
        'method': 'GET',
        'path': '/courses/sql',
        'handler': lambda params: 'PostgreSQL course'
    },
    {
        'method': 'GET',
        'path': '/courses/sql/introduction',
        'handler': lambda params: 'PostgreSQL course introduction'
    },
]

static_routing_test_cases = [
    (
        {'path': '/courses', 'method': 'GET'},
        {
            'path': '/courses',
            'method': 'GET',
            'params': {},
            'handler_output': 'all courses'
        },
    ),
    (
        {'path': '/courses', 'method': 'POST'},
        {
            'path': '/courses',
            'method': 'POST',
            'params': {},
            'handler_output': 'create course'
        },
    ),
    (
        {'path': '/courses/python', 'method': 'GET'},
        {
            'path': '/courses/python',
            'method': 'GET',
            'params': {},
            'handler_output': 'PostgreSQL course'
        },
    ),
    (
        {'path': '/courses/python/trees', 'method': 'GET'},
        {
            'path': '/courses/sql/introduction',
            'method': 'GET',
            'params': {},
            'handler_output': 'PostgreSQL course introduction'
        },
    ),
]

@pytest.mark.parametrize('static_request, expected', static_routing_test_cases)
def test_static_routing(static_request, expected):
    result_raw = MakeRouter(static_routes).serve(static_request)
    result = {
        'path': result_raw['path'],
        'method': result_raw['method'],
        'params': result_raw['params'],
        'handler_output': result_raw['handler'](result_raw['params'])
    }
    assert result == expected
