from requests import get
from requests import post
from requests import delete
from requests import put

print(post('http://localhost:5000/api/news').json())

print(post('http://localhost:5000/api/news',
           json={'title': 'Заголовок'}).json())

print(post('http://localhost:5000/api/news',
           json={'title': 'Заголовок',
                 'content': 'Текст новости',
                 'user_id': 1,
                 'is_private': False}).json())
# print(delete('http://localhost:5000/api/news/999').json())
#
# print(delete('http://localhost:5000/api/news/1').json())

print(put('http://localhost:5000/api/news/2',
           json={'title': 'Измененный заголовок',
                 'content': 'Исправленная новость'}).json())
