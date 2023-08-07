import requests
import csv


"""Получаем куки"""
cookies = {
    'SNK': '154',
    'u__typeDevice': 'desktop',
    'u__geoCityGuid': 'b835705e-037e-11e4-9b63-00259038e9f2',
    'u__geoUserChoose': '1',
    'SIK': 'mgAAAJLyl0Mo3dYTeE0GAA',
    'SIV': '1',
    'C_kAzzvswivOJr0kAptPIqE57Xpyg': 'AAAAAAAACEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8D8AAABl3_npQbJb0MhS3wsFNLgR0wn8asw',
    '_ym_uid': '1689832452768149438',
    '_ym_d': '1689832452',
    'tmr_lvid': 'f52c447d6cd1a7d8f544ea633a9cc0aa',
    'tmr_lvidTS': '1689832451909',
    'UIN': 'mgAAALDkMERc1YAt8LHgLRgZcHIXF1ZsKN3WE2trDgA',
    'ssaid': 'd9c82420-26c1-11ee-a8f4-2f24b72a0d7b',
    'dd_context.campaign': '{%22name%22:%22MSK|Search|Brand|88709722%22%2C%22source%22:%22yandex%22%2C%22medium%22:%22cpc%22%2C%22term%22:%22ST:search|S:none|AP:no|PT:premium|P:1|DT:desktop|RI:213|CI:88709722|GI:5210648503|PI:45070430478|AI:14377107137|RT:45070430478|KW:%D0%BF%D0%B5%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%87|RN:%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%22%2C%22content%22:%22gid|5210648503|pos|premium1|src|none|dvc|desktop%22}',
    'dd_custom.lastViewedProductImages': '[]',
    'FPID': 'FPID2.2.TGQx7BlnnoXiiO8xBPTIPUBXHoqyU2oQa%2B%2BnqFnxgag%3D.1689832452',
    'count_buy': '0',
    'js_SIK': 'mgAAAJLyl0Mo3dYTeE0GAA',
    'ser_ym_uid': '1689832452768149438',
    'adrcid': 'A_f20hqRJLC75vGhIIs3uDg',
    'yclid': '2101944632694800383',
    'js_count_buy': '0',
    'js_FPID': 'FPID2.2.TGQx7BlnnoXiiO8xBPTIPUBXHoqyU2oQa%2B%2BnqFnxgag%3D.1689832452',
    'ser_adrcid': 'A_f20hqRJLC75vGhIIs3uDg',
    'event_mindbox': '',
    'dd_user.email': 'kuzmich88@inbox.ru',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    '_gid': 'GA1.2.1351063051.1690516543',
    'ser_uid': '13309264',
    'FPLC': 'gzZQYdvEZ3cEp7O8pPPExfrEt4UZ%2FQrOtKrnGZsmSX9vnOwVrLW9RFWIYpvS7a0i7EJRznWliDO7it0tR74k%2BKhq2tEG7OUV4vIp0KxWrwCP%2B2PumLQOY6ZPu5LzDA%3D%3D',
    'dd_user.isReturning': 'true',
    'dd__persistedKeys': '[%22context.campaign%22%2C%22custom.lastViewedProductImages%22%2C%22user.email%22%2C%22user.isReturning%22%2C%22custom.lt13%22%2C%22custom.ts14%22]',
    '_gat_popmechanicManualTracker': '1',
    'dd_custom.lt13': '2023-07-28T03:59:11.475Z',
    'dd_custom.ts14': '{%22ttl%22:2592000%2C%22granularity%22:86400%2C%22data%22:{%221690502400%22:2}}',
    'digi_uc': 'W1siY3YiLCI5NjU1MDIiLDE2OTA1MTY3NDUxMDldLFsiY3YiLCIxMDIzNDciLDE2OTA1MTY3NTEzMDNdXQ==',
    'mindboxDeviceUUID': '15a5716b-d5ab-4420-86f4-d11d97c1221d',
    'directCrm-session': '%7B%22deviceGuid%22%3A%2215a5716b-d5ab-4420-86f4-d11d97c1221d%22%7D',
    '__tld__': 'null',
    'dd__lastEventTimestamp': '1690516773981',
    '_ga_XW7S332S1N': 'GS1.1.1690516542.3.1.1690516774.0.0.0',
    '_ga': 'GA1.1.144385082.1689832452',
}

"""Получаем заголовки запроса"""
headers = {
    'authority': 'api.petrovich.ru',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'SNK=154; u__typeDevice=desktop; u__geoCityGuid=b835705e-037e-11e4-9b63-00259038e9f2; u__geoUserChoose=1; SIK=mgAAAJLyl0Mo3dYTeE0GAA; SIV=1; C_kAzzvswivOJr0kAptPIqE57Xpyg=AAAAAAAACEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA8D8AAABl3_npQbJb0MhS3wsFNLgR0wn8asw; _ym_uid=1689832452768149438; _ym_d=1689832452; tmr_lvid=f52c447d6cd1a7d8f544ea633a9cc0aa; tmr_lvidTS=1689832451909; UIN=mgAAALDkMERc1YAt8LHgLRgZcHIXF1ZsKN3WE2trDgA; ssaid=d9c82420-26c1-11ee-a8f4-2f24b72a0d7b; dd_context.campaign={%22name%22:%22MSK|Search|Brand|88709722%22%2C%22source%22:%22yandex%22%2C%22medium%22:%22cpc%22%2C%22term%22:%22ST:search|S:none|AP:no|PT:premium|P:1|DT:desktop|RI:213|CI:88709722|GI:5210648503|PI:45070430478|AI:14377107137|RT:45070430478|KW:%D0%BF%D0%B5%D1%82%D1%80%D0%BE%D0%B2%D0%B8%D1%87|RN:%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%22%2C%22content%22:%22gid|5210648503|pos|premium1|src|none|dvc|desktop%22}; dd_custom.lastViewedProductImages=[]; FPID=FPID2.2.TGQx7BlnnoXiiO8xBPTIPUBXHoqyU2oQa%2B%2BnqFnxgag%3D.1689832452; count_buy=0; js_SIK=mgAAAJLyl0Mo3dYTeE0GAA; ser_ym_uid=1689832452768149438; adrcid=A_f20hqRJLC75vGhIIs3uDg; yclid=2101944632694800383; js_count_buy=0; js_FPID=FPID2.2.TGQx7BlnnoXiiO8xBPTIPUBXHoqyU2oQa%2B%2BnqFnxgag%3D.1689832452; ser_adrcid=A_f20hqRJLC75vGhIIs3uDg; event_mindbox=; dd_user.email=kuzmich88@inbox.ru; _ym_isad=2; _ym_visorc=b; _gid=GA1.2.1351063051.1690516543; ser_uid=13309264; FPLC=gzZQYdvEZ3cEp7O8pPPExfrEt4UZ%2FQrOtKrnGZsmSX9vnOwVrLW9RFWIYpvS7a0i7EJRznWliDO7it0tR74k%2BKhq2tEG7OUV4vIp0KxWrwCP%2B2PumLQOY6ZPu5LzDA%3D%3D; dd_user.isReturning=true; dd__persistedKeys=[%22context.campaign%22%2C%22custom.lastViewedProductImages%22%2C%22user.email%22%2C%22user.isReturning%22%2C%22custom.lt13%22%2C%22custom.ts14%22]; _gat_popmechanicManualTracker=1; dd_custom.lt13=2023-07-28T03:59:11.475Z; dd_custom.ts14={%22ttl%22:2592000%2C%22granularity%22:86400%2C%22data%22:{%221690502400%22:2}}; digi_uc=W1siY3YiLCI5NjU1MDIiLDE2OTA1MTY3NDUxMDldLFsiY3YiLCIxMDIzNDciLDE2OTA1MTY3NTEzMDNdXQ==; mindboxDeviceUUID=15a5716b-d5ab-4420-86f4-d11d97c1221d; directCrm-session=%7B%22deviceGuid%22%3A%2215a5716b-d5ab-4420-86f4-d11d97c1221d%22%7D; __tld__=null; dd__lastEventTimestamp=1690516773981; _ga_XW7S332S1N=GS1.1.1690516542.3.1.1690516774.0.0.0; _ga=GA1.1.144385082.1689832452',
    'origin': 'https://moscow.petrovich.ru',
    'referer': 'https://moscow.petrovich.ru/catalog/95761838/?sort=popularity_desc',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36',
}

"""Получаем параметры запроса"""
params = {
    'sort': 'popularity_desc',
    'limit': '20',
    'offset': '0',
    'path': '/catalog/95761838/',
    'city_code': 'msk',
    'client_id': 'pet_site',
}

"""Сохраняем ответ от сервера"""
response = requests.get(
    'https://api.petrovich.ru/catalog/v3/sections/95761838/products',
    params=params,
    cookies=cookies,
    headers=headers,
).json()['data']['products'] # вытаскиваем ключи с продуктами

"""Проходимся циклом по полученному json"""
for i in response:
    title = (i['title']) # вытаскивам ключ title
    gold = (i['price']['gold'], "рублей за штуку") # вытаскивам ключи с ценами

    with open('woods.csv', 'a', newline='') as file: # открывем файл на дозапись (обязательно, иначе перезатрём данные из цикла)
            writer = csv.writer(file) # сохраняем результат функции writer в переменную writer
            writer.writerow([title, gold]) # записываем в csv файл нужные ключи
варлар
