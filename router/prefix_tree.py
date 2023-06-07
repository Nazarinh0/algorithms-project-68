class PrefixTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.methods = {}
        self.pattern_path = ''

    def get_pattern_path(self):
        return self.pattern_path

    def get_handler(self, method):
        return self.methods[method]


class PrefixTree:
    def __init__(self):
        self.root = PrefixTreeNode(None)

    def add_route(self, route):
        current_node = self.root
        segments = route['path'].split('/')
        pattern_path = []

        for segment in segments:
            if segment not in current_node.children:
                current_node.children[segment] = PrefixTreeNode(segment)
            current_node = current_node.children[segment]
            pattern_path.append(segment)

        current_node.pattern_path = '/'.join(pattern_path)
        current_node.methods.setdefault(route['method'], route['handler'])

    def find_route(self, request):
        current_node = self.root
        segments = request['path'].split('/')

        for segment in segments:
            if segment not in current_node.children:
                return None
            current_node = current_node.children[segment]

        if request['method'] not in current_node.methods:
            return None
        return current_node
