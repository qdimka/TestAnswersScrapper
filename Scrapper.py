from bs4 import BeautifulSoup
import requests


sites = ["http://upworktest.in/top-10-popular-test-answers/css-test-2016/",
         "http://tiffinperiod.com/upwork-css-test-answers/",
         "http://www.freelancehelps.com/2015/09/upwork-css-test-answer.html"]


def get_html(url):
    """
    Get HTML string from url
    :param url:
    :return HTML string:
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    req = requests.get(url, headers)
    return req.content

html = [get_html(url) for url in sites]


soup = BeautifulSoup(html[0], "html.parser")


def f_questions(tag):
    return not tag.has_attr('class') and \
           not tag.has_attr('id') and \
           (tag.name == "p" or tag.name == "ol")


def f_answers(tag):
    return tag.name == "li"


def f_one_answers(tag):
    pass


def get_questions_list(filter_quest, filter_answers):
    list_questions = {}
    questions = soup.find_all(filter_quest)

    for q in questions:

        answers = q.find_all(filter_answers)

        if len(answers) != 0:
            for answer in answers:
                if answer.find('span', attrs={'style': "background-color: #c66201; color: #fff;"}) is not None:
                    list_questions.append('***' + ' ' + answer.text)
                else:
                    list_questions.append(answer.text)
        else:
            list_questions.append(q.text)

    return list_questions
