import requests
import csv

# URL страницы с информацией об отелях
url = 'https://www.travel.mts.ru/'

# Получаем содержимое страницы
response = requests.get(url)
html = response.content

# Создаем объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(html, 'html.parser')

# Находим все элементы с информацией о номерах в отеле
rooms = soup.find_all('div', class_='room-info')

# Создаем словарь для хранения информации о каждом номере
room_info = {}

# Проходимся по каждому номеру и добавляем информацию о нем в словарь
for room in rooms:
    room_name = room.find('h3', class_='room-name').text
    room_type = room.find('span', class_='room-type').text
    room_price = room.find('span', class_='room-price').text
    room_days = room.find('span', class_='room-days').text
    room_max_occupancy = room.find('span', class_='room-max-occupancy').text
    room_min_occupancy = room.find('span', class_='room-min-occupancy').text
    room_max_occupancy_days = room.find('span', class_='room-max-occupancy-days').text
    room_min_occupancy_days = room.find('span', class_='room-min-occupancy-days').text
    room_max_occupancy_occupancy = room.find('span', class_='room-max-occupancy-occupancy').text
    room_min_occupancy_occupancy = room.find('span', class_='room-min-occupancy-occupancy').text
    
    # Добавляем информацию о номере в словарь
    room_info['room_name'] = room_name
    room_info['room_type'] = room_type
    room_info['room_price'] = room_price
    room_info['room_days'] = room_days
    room_info['room_max_occupancy'] = room_max_occupancy
    room_info['room_min_occupancy'] = room_min_occupancy
    room_info['room_max_occupancy_days'] = room_max_occupancy_days
    room_info['room_min_occupancy_days'] = room_min_occupancy_days
    room_info['room_max_occupancy_occupancy'] = room_max_occupancy_occupancy_days
    room_info['room_min_occupancy_occupancy'] = room_min_occupancy_occupancy_days

# Выводим информацию о номерах в отелях
for key, value in room_info.items():
    print(key + ': ' + value)


