def order_pick(files, top):
    """
    :type files: list
    :type top: int
    """
    n = 0
    for k, v in files:
        if n < top:
            print(k, v)
            n += 1
        else:
            break


def counting(urls):
    """
    :type urls: list
    :rtype: list
    """
    dc = dict()
    for row in urls:
        file = row.split("/")[-1]
        dc[file] = dc.get(file, 0) + 1
    return [(k, dc[k]) for k in sorted(dc.keys())]


def main():
    urls = [
        "http://www.google.com/a.txt",
        "http://www.google.com.tw/a.txt",
        "http://www.google.com/download/c.jpg",
        "http://www.google.co.jp/a.txt",
        "http://www.google.com/b.txt",
        "https://facebook.com/movie/b.txt",
        "http://yahoo.com/123/000/c.jpg",
        "http://gliacloud.com/haha.png"
    ]
    n = 3
    ordered_file = counting(urls)
    order_pick(ordered_file, n)


if __name__ == '__main__':
    main()
