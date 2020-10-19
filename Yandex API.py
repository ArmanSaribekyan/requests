# import requests
# from pprint import pprint
#
#
# TOKEN = "AgAAAAA0U09uAADLWwmQiO8kgUzHqNeIgumhqGk"
# HEADERS = {"Authorization": f'OAuth {TOKEN}'}
# file = "/superhero.py"
#
# response = requests.get(
#     "https://cloud-api.yandex.net/v1/disk/resources/upload",
#     params={"path": file},
#     headers=HEADERS
# )
# print(response.status_code)
# pprint(response.json())
#
# download = requests.put(response.json()['href'])
# print(download.status_code)