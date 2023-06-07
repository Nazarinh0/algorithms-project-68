from router.prefix_tree import PrefixTree


class MakeRouter:
    ALLOWED_METHODS = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']

    def __init__(self, routes):
        self.routes_tree = PrefixTree()
        for route in routes:
            self.routes_tree.add_route(route)

    def serve(self, request):
        if request['method'] not in self.ALLOWED_METHODS:
            raise Exception(f'request method {request["method"]} not allowed')
        target_route = self.routes_tree.find_route(request)
        if not target_route:
            raise Exception("No route found")
        pattern_path = target_route.get_pattern_path()
        result = {
            'path': pattern_path,
            'method': request['method'],
            'handler': target_route.get_handler(request['method']),
            'params': self.get_route_params(request['path'], pattern_path)
        }
        return result

    @staticmethod
    def get_route_params(given_path, pattern_path):
        params = {}
        given_path_segments = given_path.split('/')
        pattern_path_segments = pattern_path.split('/')
        for given_path_segment, pattern_path_segment in zip(
                given_path_segments,
                pattern_path_segments
        ):
            if pattern_path_segment.startswith(":"):
                params.setdefault(pattern_path_segment[1:], given_path_segment)
        return params
