def finder(files, queries):
    paths_for_file = {}
    for path in files:
        file_name_start_index = path.rfind('/') + 1
        file_name = path[file_name_start_index:]
        if file_name in paths_for_file:
            paths_for_file[file_name] += [path]
        else:
            paths_for_file[file_name] = [path]
    
    paths_queried = {}
    for query in queries:
        if query in paths_for_file:
            paths = paths_for_file[query]
            for path in paths:
                paths_queried[path] = path

    return list(paths_queried.keys())


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
