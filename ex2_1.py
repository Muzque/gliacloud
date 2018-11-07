import requests
from bs4 import BeautifulSoup


def get_mainweb(board):
    url = "https://www.ptt.cc/bbs/{}/index.html".format(board)
    res = requests.get(url=url)
    return res


def get_detail(boardtag):
    url = "https://www.ptt.cc{}".format(boardtag)
    res = requests.get(url=url)
    return res


def etl_content(board, res):
    essay_list = list()
    soup = BeautifulSoup(res, "lxml")
    for essay in soup.select(".r-ent"):
        post = dict()
        post['board'] = board
        post['title'] = essay.find('a').string
        url = essay.find('a')['href']
        post['author'] = essay.find('div', class_='author').string
        post['date'] = essay.find("div", class_="date").string
        res_detail = get_detail(url)
        if res_detail.status_code == 200:
            soup = BeautifulSoup(res_detail.text, "lxml")
            post['content'] = soup.find("div", {"id": "main-content"})
        else:
            post['content'] = "Empty"
        # print(post)
        essay_list.append(post)
    return essay_list


def main():
    board = "Soft_Job"
    res = get_mainweb(board)
    if res.status_code == 200:
        essay_list = etl_content(board, res.text)
        print(essay_list)
    else:
        print("error")


if __name__ == "__main__":
    main()
