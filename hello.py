#from telethon.sync import TelegramClient
from telethon import TelegramClient, connection

# Use your own values from my.telegram.org
api_id = 594415
api_hash = '25e696d465485373139816665e4f7a32'

DC1_ip = '193.46.56.225'
DC_port = 443

proxy_ip = 'catalog.live.ovh'
proxy_port = 443
secret = 'e2528db4ce33feaabb1c0676f6f676c652e636f6d'

proxy = (proxy_ip, proxy_port, secret)

client = TelegramClient('session_name_1', api_id, api_hash, proxy=(proxy_ip,
proxy_port, secret),  connection=connection.tcpmtproxy.ConnectionTcpMTProxy)
client.session.set_dc(1, DC1_ip, DC_port)
client.start()
#print(client.get_me().stringify())
#client = TelegramClient('anon', api_id, api_hash)





@client.on(events.NewMessage)
async def my_event_handler(event):
    if '@' in event.raw_text:
        await event.respond('''ВАС ПРИВЕТСТВУЕТ МАГАЗИН illuminati shop

✅Наши плюсы:
-Свежие клады и качественный товар! ✔️
-Специально для Вас в режиме 24/7! 🕧
-Быстрая оплата на банковскую карту! 🚀
➖➖➖➖➖➖➖➖➖➖
Уважаемый Dob_Maq
Ваш баланс: 0.00
➖➖➖➖➖➖➖➖➖➖
- Наши контакты! 👤 - Отправь:  *
- Работа в шопе! 💼 - Отправь:  #
- Помощь ⁉️ - Отправь: 101
- Инструкция по пополнению баланса 💰 - Отправь: 102
- Ваши покупки 💼 - Отправь: 103
➖➖➖➖➖➖➖➖➖➖
Новосибирск
➖➖➖➖➖➖➖➖➖➖
  - Гречка
    - Гречка 0.10 ГР. - Нет в наличии.
    - Гречка 0.25 ГР. - Нет в наличии.
➖➖➖➖➖➖➖➖➖➖
  - Альфа кристалл
    - Альфа кристалл 0.30 ГР. 800.00 руб.  - Отправь: 200
    - Альфа кристалл 0.50 ГР. 1000.00 руб.  - Отправь: 201
    - Альфа кристалл 1.00 ГР. - Нет в наличии.
➖➖➖➖➖➖➖➖➖➖

➖🤸‍♂️Хорошего трипа! 🤸‍♂️➖''')
    elif '*' in event.raw_text:
            await event.respond('''по всем вопросам - @iIIumiboss
💬 ЧАТ НСК - https://t.me/joinchat/I4N4YjU0hZIjHONFdR2oLew
📢 КАНАЛ ОТЗЫВОВ -  https://t.me/iIlumiNews24
Для выхода в главное меню отправьте любое сообщение!
➖🤸‍♂️Хорошего трипа! 🤸‍♂️➖''')

    else:
        await event.respond('пока')

@client.on(events.NewMessage)
async def my_event_handler1(event):

    if '#' in event.raw_text:
        await event.respond('''В команду iIIuminati требуются трезвые, адекватные работники.
Лучшие условия на рынке, индивидуальный подход, карьерный рост.
Пишите - @iIIumiboss
Для выхода в главное меню отправьте любое сообщение!
➖🤸‍♂️Хорошего трипа! 🤸‍♂️➖''')

    if '101' in event.raw_text:
        await event.respond('''‼️‼️‼️ПЕРЕВОДИТЕ ИМЕННО ТУ СУММУ КОТОРУЮ УКАЖЕТ БОТ! ‼️‼️‼️
‼️‼️‼️ИНАЧЕ ДЕНЬГИ БУДУТ ПОТЕРЯНЫ‼️‼️‼️

Не совершайте перевод если вы отменили пополнение баланса!!!

Если вам нужна помощь связанная с оплатой, Пожалуйста,  приготовьте чек в формате PDF или скриншот чека, на котором он виден ПОЛНОСТЬЮ!

По всем возникшим вопросам обратитесь - @iIIumiboss
Для выхода в главное меню отправьте любое сообщение!
➖🤸‍♂️Хорошего трипа! 🤸‍♂️➖''')

    if '102' in event.raw_text:
        await event.respond('''Следуйте указаниям бота, каждая команда указана цифрами.
Для выхода в главное меню отправьте любое сообщение!''')

    if '103' in event.raw_text:
        await event.respond('''К сожалению вы ещё нечего не покупали!
Для выхода в главное меню отправьте любое сообщение!
➖🤸‍♂️Хорошего трипа! 🤸‍♂️➖''')

    if '200' in event.raw_text:
        await event.respond('''Вами выбран: Альфа кристалл 0.30 ГР. за 800.00 руб. , выберите район:
 Кировский  - Отправь: 10
 Железнодорожный  - Отправь: 11
 Октябрьский  - Отправь: 12
 Дзержинский  - Отправь: 13
 Калининский  - Отправь: 14
 Заельцовский  - Отправь: 15''')

    if '10' in event.raw_text:
        await event.respond('''Выберите метод оплаты:
 Перевод на Карту  - Отправь: 1

Для выхода в главное меню отправьте: 414684''')


    if '1' in event.raw_text:
        await event.respond('''Вы выбрали перевод на карту!
Переведите ‼️808‼️ руб.
‼️ПЕРЕВОДИТЕ ИМЕННО ‼️808 руб. ‼️ ИНАЧЕ ДЕНЬГИ БУДУТ ПОТЕРЯНЫ!‼️
на Карту 4890494670814458

Не выходите из этого меню до зачисления отправленных денег на баланс!
Обычно пополнение происходит в течении 5-10 минут с момента перевода!
Для проверки баланса отправьте сообщение "1"!

Ваш баланс: 0.00
Для выхода в главное меню отправьте: 784657''')








#   @client.on(events.NewMessage)
#   async def my_event_handler(event):
#       if '' in event.raw_text:
#           await event.respond('''Новсиб''')







client.start()
client.run_until_disconnected()


#@client.on(events.NewMessage(pattern='(?i)hi|hello'))
#async def handler(event):
#    await event.respond('Hey!')
