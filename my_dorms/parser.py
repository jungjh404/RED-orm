import requests
from bs4 import BeautifulSoup

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()

from dorms.models import Context

def parse_notice(start_index, end_index) :
    data = []

    start_page = (start_index//10)*10
    end_page = ((end_index-1)//10 +1)*10

    crawling_number = list(range(start_page, end_page, 10))

    num = 0
    for page_num in crawling_number :
        url = "https://dorm.skku.edu/dorm_suwon/notice/notice_all.jsp?mode=list&board_no=16&pager.offset="+str(page_num)
        req = requests.get(url)
        html = req.text
        result = BeautifulSoup(html, 'html.parser')
        post_urls = result.select("#jwxe_main_content > div > div.list_wrap > table > tbody > tr > td.td.title > a")

        for (i, post_url) in enumerate (post_urls) :
            #중복 삭제
            if (i <= num) :
                continue
            if (i+page_num > end_index) :
                continue
            print(str(i+page_num) + "번째 게시물입니다.")
            print(post_url)
            post_url = post_url["href"].replace("amp;","")
            post_url = "https://dorm.skku.edu/dorm_suwon/notice/notice_all.jsp" + post_url
            print(post_url)

            req = requests.get(post_url)
            html = req.text
            result = BeautifulSoup(html, 'html.parser')

            #title
            title = result.select_one("div.view_wrap > table > tr:nth-of-type(1) > td").text
            title = title.replace("\n", "")
            title = title.replace("  ", "")
            print("title : ", title)

            #date
            date = result.select_one("div.view_wrap > table > tr:nth-of-type(2) > td > span:nth-of-type(4)").text
            print("date: ", date)

            #context
            context = result.select_one("#article_text").text
            context = context.replace("  ", "")
            context = context.replace("\n\n", '\n')
            print(context)

            #writer은 admin
            writer = "admin"

            data_object = {
                "title" : title,
                "date" : date,
                "content" : context,
            }

            data.append(data_object)

        num = i - 10
        print("\n")

    return data

if __name__=='__main__' :
    result = parse_notice(0,40)
    for data in result :
        notice = Context(title = data["title"], date = data["date"], content = data["content"])
        notice.save()