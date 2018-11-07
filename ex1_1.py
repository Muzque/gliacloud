def counting(urls):
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
    dc = counting(urls)
    n = 0
    for k, v in dc:
        if n < 3:
            print(k, v)
            n += 1


if __name__ == '__main__':
    main()
