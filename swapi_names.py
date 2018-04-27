import json
import urllib.request

api_url = 'http://swapi.co/api/people/'


def proccess_names(response):
    return [character.get('name', 'Anonymous') for character in response.get('results', [])]


def get_data(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    res = urllib.request.urlopen(req).read()
    return json.loads(res)


def get_names():
    names = []
    current_page = 1

    first_response = get_data(api_url)
    names += proccess_names(first_response)
    next_page = first_response.get('next', None)

    while next_page is not None:
        response = get_data('{}?page={}'.format(api_url, current_page + 1))
        next_page = response.get('next', None)
        current_page += 1
        names += proccess_names(response)

    names.sort()
    return names


def write_people():
    names = get_names()
    print('\r\n'.join(names))


if __name__ == '__main__':
    write_people()
