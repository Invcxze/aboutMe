from django.http import HttpResponse 
def index(request,Name, Surname, interests,age):
    return HttpResponse(f"""
    <h2>Главная</h2>
    <p>Имя: {Name}</p>
    <p>Фамилия: {Surname}</p>
    <p>Интересы: {interests}</p>
    <p>Возраст: {age}</p>
    """)
def about(request, city,school,study):
    return HttpResponse(f"""
    <h2>Обо мне</h2>
    <p>Откуда приехал: {city}</p>
    <p>Успеваемость в школе: {school}</p>
    <p>Люблю ли учится: {study}</p>
    """)
def contact(request,vk,inst,github):
    return HttpResponse(f"""\
        <h2>Контакты</h2>
        <p>inst: {inst}</p>
        <p>Github: {github}</p>
        <p>Vk: {vk}</p>
        """)
