import random
import time
import requests

api_key = ""
phones = []
messages = [
    "Привлекайте новых клиентов с нашей рекламой в ВК и Телеграм",
    "Увеличьте поток клиентов с помощью профессиональной рекламы",
    "Высокоэффективная реклама для массажисток и салонов массажа",
    "Автоматизированные каталоги повысят вашу видимость в сети",
    "Создадим сайт, который привлечет клиентов со всего города",
    "Комплексное рекламное обслуживание для успешного бизнеса",
    "Выгодные условия рекламы для массажных салонов и специалистов",
    "Доверьте рекламу профессионалам и увидите результат",
    "Мы поможем вывести ваш бизнес в ТОП поисковых запросов",
    "Реклама, которая окупится новыми постоянными клиентами",
    "Расширьте клиентскую базу с помощью наших рекламных услуг",
    "Профессиональная SMM-реклама для массажных специалистов",
    "Создание и продвижение сайтов для массажных салонов",
    "Автоматизируйте свой бизнес с нашими каталогами массажисток",
    "Индивидуальный подход к рекламе вашего массажного бизнеса",
    "Выделитесь среди конкурентов с помощью нашей рекламы",
    "Наши услуги помогут увеличить ваши доходы и клиентскую базу",
    "Закажите рекламу и получите первых клиентов уже сегодня",
    "Профессиональное продвижение в социальных сетях для массажистов",
    "Реклама, которая работает: привлекаем целевую аудиторию",
    "Доверьтесь экспертам в сфере рекламы массажных услуг",
    "Повысим узнаваемость вашего бренда с помощью рекламы",
    "Создадим и продвинем сайт, который станет вашей визитной карточкой",
    "Качественная реклама по доступным ценам для массажных салонов",
    "Увеличьте свои доходы, воспользовавшись нашими рекламными услугами",
    "Расскажем о ваших услугах массажа тысячам потенциальных клиентов",
    "Мы сделаем вас заметными в сети с помощью рекламы и продвижения",
    "Эффективная реклама в ВК и Телеграм для массажистов и салонов",
    "Создание сайтов и ведение каталогов для массажных специалистов",
    "Автоматизируйте свои рекламные кампании вместе с нами",
    "Профессиональная SMM-реклама по выгодным ценам",
    "Привлечем новых клиентов с помощью таргетированной рекламы",
    "Увеличьте продажи массажных услуг благодаря нашей рекламе",
    "Наша реклама поможет вам выйти на новый уровень успеха",
    "Ведение и продвижение каталогов массажисток в вашем городе",
    "Создадим сайт, который станет вашей эффективной визитной карточкой",
    "Профессиональная реклама для массажных салонов и специалистов",
    "Доверьтесь экспертам в области рекламы массажных услуг",
    "Расскажем о ваших предложениях тысячам потенциальных клиентов",
    "Повысим узнаваемость вашего бренда с помощью рекламных кампаний",
    "Привлечем новых клиентов с помощью таргетированной рекламы в ВК",
    "Профессиональное продвижение сайтов массажных салонов",
    "Увеличьте свои доходы, воспользовавшись нашей качественной рекламой",
    "Эффективная реклама по доступным ценам для массажистов",
    "Создадим и продвинем сайт, ставший вашей визитной карточкой",
    "Наши рекламные услуги помогут расширить вашу клиентскую базу",
    "Автоматизируйте свои рекламные кампании вместе с профессионалами",
    "Качественная SMM-реклама для массажных салонов и специалистов",
]
def send_sms(api_key, phone, message):
    url = "https://sms-free.ru/api/send?key=" + api_key
    data = {
        "phone": phone,
        "message": message
    }
    response = requests.post(url, data=data)
    return response.json()


while True:
    # Выбираем случайное сообщение и номер телефона из списков
    selected_message = random.choice(messages)
    selected_phone = random.choice(phones)

    # Отправляем сообщение
    result = send_sms(api_key, selected_phone, selected_message)
    print(f"Отправлено сообщение на номер {selected_phone}: {selected_message}")

    # Удаляем использованный номер и сообщение из списков
    messages.remove(selected_message)
    phones.remove(selected_phone)

    # Генерируем случайное количество секунд для ожидания перед следующей отправкой
    wait_time = random.randrange(3567, 4276)
    print(f"Ждем {wait_time} секунд перед следующей отправкой")
    time.sleep(wait_time)
