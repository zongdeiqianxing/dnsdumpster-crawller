import re
import requests


def dnsdumpster(domain):
    url = 'https://dnsdumpster.com'
    headers = {'Referer': 'https://dnsdumpster.com/',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52'}

    session = requests.session()
    response = session.get(url=url)
    cookie_text = response.headers['Set-Cookie']
    csrftoken = cookie_text[cookie_text.index('=')+1:cookie_text.index(';')]
    print(csrftoken)

    data = {'csrfmiddlewaretoken': csrftoken,
            'targetip': domain,
            'user': 'free'}
    response = session.post(url=url, headers=headers, data=data)
    print(response.status_code)

    result = re.findall('\w+?\.{}'.format(domain), response.text)
    print(result)
    print(len(set(result)))


if __name__ == '__main__':
    dnsdumpster('oxy.com')
