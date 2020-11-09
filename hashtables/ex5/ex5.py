# Your code here

import operator


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    dict = {}
    qict = {}
    for i, e in enumerate(files):
        dict[e] = i
    for i, e in enumerate(queries):
        qict[e] = i

    print(dict)
    print(qict)
    # return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
