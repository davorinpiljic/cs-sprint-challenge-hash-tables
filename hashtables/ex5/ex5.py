# Your code here
def finder(files, queries):
    # Your code here
    dict = {}
    arr = []
    found = []
    for i, e in enumerate(files):
        dict[e] = i

    for i, q in enumerate(queries):
        if [val for key, val in dict.items() if q in key]:
            arr.append(i)
    urllist = list(dict.keys())

    for i in arr:
        if i != None:
            print(i)
            found.append(urllist[i])

    return(found)


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        'foo',
        "qux",
        "baz"
    ]
    print(finder(files, queries))
