import requests

url = 'https://api.hh.ru/vacancies'
job = 'python'
per_page = 100
schedule = ['remote']
par = {'text': job, 'per_page': per_page, 'page': 0, 'schedule': schedule}


def get_vacancy_id_list()->list:
    """возвращает список id вакансий по запросу поиска"""

    def extend_list(ex_list: list, json): ex_list.extend(v['id'] for v in json['items'])

    id_list = []
    r = requests.get(url, params=par)
    e = r.json()
    # кол-во страниц всего
    pages_number = e['pages']

    # загрузили 0-юстраницу и записали id
    extend_list(id_list, r.json())
    # грузим 1-ю и последующие
    for i in range(1, pages_number):
        par['page'] = i
        r = requests.get(url, params=par)
        extend_list(id_list, r.json())
    return id_list


print(get_vacancy_id_list())
