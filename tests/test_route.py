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

# def test_serve_method():
#     # Define a set of routes to use in the test
#     routes = [
#         {
#             'method': 'GET',
#             'path': '/users/:id',
#             'handler': lambda params: f'get user {params["id"]}'
#         },
#         {
#             'method': 'POST',
#             'path': '/users',
#             'handler': lambda params: 'create user'
#         }
#     ]
#
#     # Create a router instance with the defined routes
#     router = MakeRouter(routes)
#
#     # Test a request that matches a dynamic route
#     request1 = {'path': '/users/123', 'method': 'GET'}
#     result1 = router.serve(request1)
#     assert result1.path == '/users/:id'
#     assert result1.params == {'id': '123'}
#     assert result1.handler(result1.params) == 'get user 123'
#
#     # Test a request that matches a static route
#     request2 = {'path': '/users', 'method': 'POST'}
#     result2 = router.serve(request2)
#     assert result2.path == '/users'
#     assert result2.params == {}
#     assert result2.handler(result2.params) == 'create user'
#
#     # Test a request that does not match any route
#     request3 = {'path': '/posts', 'method': 'GET'}
#     with pytest.raises(Exception):
#         router.serve(request3)
#
#     # Test a request with an unsupported method
#     request4 = {'path': '/users/123', 'method': 'DELETE'}
#     with pytest.raises(Exception):
#         router.serve(request4)
#
#     # Test a request that partially matches a dynamic route
#     request5 = {'path': '/users/', 'method': 'GET'}
#     with pytest.raises(Exception):
#         router.serve(request5)
#
#     # Test a request that partially matches a static route
#     request6 = {'path': '/course', 'method': 'GET'}
#     with pytest.raises(Exception):
#         router.serve(request6)
#
#     # Test a request with multiple dynamic segments
#     request7 = {'path': '/users/123/posts/456', 'method': 'GET'}
#     result7 = router.serve(request7)
#     assert result7.path == '/users/:id/posts/:post_id'
#     assert result7.params == {'id': '123', 'post_id': '456'}
#     assert result7.handler(result7.params) == 'get post 456 for user 123'
#
#     # Test a request with multiple dynamic segments that partially match a route
#     request8 = {'path': '/users/123/posts', 'method': 'GET'}
#     with pytest.raises(Exception):
#         router.serve(request8)
