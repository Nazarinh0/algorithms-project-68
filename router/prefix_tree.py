class PrefixTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.is_terminal = False
        self.pattern_path = None
        self.handler = None

    def get_pattern_path(self):
        return self.pattern_path

    def get_handler(self):
        return self.handler


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

        current_node.is_terminal = True
        current_node.pattern_path = '/'.join(pattern_path)
        current_node.handler = route['handler']

    def find_route(self, route_path):
        current_node = self.root
        segments = route_path.split('/')

        for segment in segments:
            if segment not in current_node.children:
                return None
            current_node = current_node.children[segment]

        return current_node