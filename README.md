### Hexlet tests and linter status:
[![Actions Status](https://github.com/Nazarinh0/algorithms-project-68/workflows/hexlet-check/badge.svg)](https://github.com/Nazarinh0/algorithms-project-68/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/79f78ee7dde4f00e8907/maintainability)](https://codeclimate.com/github/Nazarinh0/algorithms-project-68/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/79f78ee7dde4f00e8907/test_coverage)](https://codeclimate.com/github/Nazarinh0/algorithms-project-68/test_coverage)

# Description
The router is one of the most commonly used components on any website through which it is accessed. The performance of the site depends on how fast the router works. For example, if a resource receives thousands of requests per second and there are many routes, then it may take significant time to load. Therefore, the design and speed of the router are important.

To make it work efficiently, developers use special data structures, for example, express the internal structure as a prefix tree.

I made this project to improve my skills in working with tree-like structures. This topic was studied on the trees and algorithms course, and here it is revealed through a task that modern frameworks solve. During development, we will create an abstraction to easily traverse the tree and accumulate work results.

Each page of the site has a URL. When we access a site, the engine on which it is written analyzes the URL and tries to find a function to generate a response. Routing is responsible for this process, which is implemented as a separate component - the router. It selects a function depending on the URL.

Routers are often implemented as separate libraries that are then used within the site. This is good practice, and in this project, we will write such a library. In the end, our router can be used on real sites.

