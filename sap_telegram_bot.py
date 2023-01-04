## ## Telegram bot -- SaryarkaAutoProm_HR_bot

import telebot
from config import TOKEN
#from telebot import types



bot = telebot.TeleBot(TOKEN)



"""--------UPLOAD----------"""

# @bot.message_handler(content_types=["document", "video", "audio"])
# def file_upload(message):
#     """загрузка файла в бота и получние file_id"""
#     document_id = message.document.file_id
#     file_info = bot.get_file(document_id)
#     print(document_id)  # Выводим file_id
#     print(f'http://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}')  # Выводим ссылку на файл
#     #bot.send_message(message.chat.id, document_id)  # Отправляем пользователю file_id
#     #bot.send_document(chat_id=message.from_user.id, document=document_id)
#
# @bot.message_handler(content_types=["photo"])
# def photo_upload(message):
#     """загрузка photo в бота и получние file_id"""
#     photo_id = message.photo[0].file_id
#     file_info = bot.get_file(photo_id)
#     print(photo_id)  # Выводим file_id
#     print(f'http://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}')  # Выводим ссылку на файл
#
# @bot.message_handler(content_types=["voice"])
# def voice_upload(message):
#     """загрузка voice в бота и получние file_id"""
#     print("Пришло voice")
#     voice_id = message.voice.file_id
#     file_info = bot.get_file(voice_id)
#     print(voice_id)  # Выводим file_id
#     print(f'http://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}')  # Выводим ссылку на файл

"""--------UPLOAD----------"""




@bot.message_handler(commands=['adaptation'])
def send_message(message):
    """отправка файла - АДАПТАЦИЯ.pptx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAAMwYz0etWDhgFEymeWocmq-e-wXqQoAAushAAK58OlJOoavyuhNfuYqBA")


@bot.message_handler(commands=['timesheet'])
def send_message(message):
    """отправка файла - ОБРАЗЕЦ табеля.xlsx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAAMxYz0eywV2SPBz452yd8Ey0TDqhSsAAuwhAAK58OlJj0Bb0t9vd_oqBA")


@bot.message_handler(commands=['supervisorchecklist'])
def send_message(message):
    """отправка файла - Памятка для руководителя.docx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAAMyYz0e4HqYSsnXkMzTMoXorjL5M10AAu0hAAK58OlJwkeZ9GguBmUqBA")


@bot.message_handler(commands=['infosecur'])
def send_message(message):
    """отправка файла - Политика_информационной_безопасности.pdf"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAAMzYz0e92urh89x_-cVwCT2weOpLuUAAu4hAAK58OlJgf-PkFcyh5UqBA")


@bot.message_handler(commands=['provisionaboutcrew'])
def send_message(message):
    """отправка файла - Пололожение о бригаде от 17 апр 2019.pdf"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAAM0Yz0fEaA7nBoFQTDKPm5Ek_ndiXYAAu8hAAK58OlJm2BdlZ7J_DgqBA")


@bot.message_handler(commands=['provisionaboutemployeepool'])
def send_message(message):
    """отправка файла - Пололожение о кадровом резерве САП от 12 фев 2021.pdf"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAAM1Yz0fK_AWNl9TQ4qkGgHiQVgRrPgAAvIhAAK58OlJzIA978BG4cwqBA")


@bot.message_handler(commands=['provisionaboutmentoring'])
def send_message(message):
    """отправка файла - Пололожение о наставничестве от 23 окт 2020.pdf"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAAM2Yz0fXWiNKten7VEsqjkG423RQxwAAvQhAAK58OlJubNwDwspXykqBA")


@bot.message_handler(commands=['provisionaboutlaborcompensation'])
def send_message(message):
    """отправка файла - Пололожение о оплате труда от 31 марта 2021.pdf"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAAM3Yz0fgCTLQ7hQsZV05Lrw6OKB4k4AAvYhAAK58OlJvsm-2WcK6SAqBA")


@bot.message_handler(commands=['listofroleswithfinresponsibility'])
def send_message(message):
    """отправка файла - приказ 1-П,1 (Об утверждении перечня должностей, при приеме на которые заключаются договоры о полной мат.ответственности) от 05.01.2022г.pdf"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAAM4Yz0fvTJbArGNv72fjQt7fcduqkUAAvchAAK58OlJbEBa--BQ0DUqBA")


@bot.message_handler(commands=['claimforexplreportmisconduct'])
def send_message(message):
    """отправка файла - Требование о предоставлении объяснения по факту совершенного дисциплинарного проступка.docx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAAM5Yz0f5mEJN-mRS_CVuJQBTYcwIiUAAvohAAK58OlJl-iAip81M_gqBA")


@bot.message_handler(commands=['consentforovertimework'])
def send_message(message):
    """отправка файла - Форма  № 323 СОГЛАСИЕ работника на работу сверхурочно, выходные (праздничные) дни.docx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAAM6Yz0gBV85-e9B1wOSPSYV6EMlOgkAAvwhAAK58OlJ4ZbJbUMQO1AqBA")


@bot.message_handler(commands=['employeeattendanceconfirmation'])
def send_message(message):
    """отправка файла - Форма № 81 Подтверждение о нахождении работника на рабочем месте.docx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAAM7Yz0gF32RsbWaBycRphxYfMNEuXQAAv4hAAK58OlJcGs03xtxBikqBA")


@bot.message_handler(commands=['resignationformfinresponsibility'])
def send_message(message):
    """отправка файла - Форма № 375 Заявления на расторжение трудового договора для лиц с полной материальной ответственностью.docx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAAM8Yz0gNLx2ivnv5ytyJ1M71s_5rw4AAyIAArnw6Ul2iCq3cRr04ioE")

##############################################
@bot.message_handler(commands=['eventnotificationlist'])
def send_message(message):
    """отправка файла - О каких событиях необходимо сообщать в отдел кадров.docx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAAM-Yz0gaYagMYu_nTsph1_-T03OhoIAAgIiAAK58OlJGwynu0vkPHAqBA")


@bot.message_handler(commands=['resignationform72'])
def send_message(message):
    """отправка файла - № 72 Заявление на РАСТОРЖЕНИЕ трудового договора.docx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAANAYz0hInpEOWzwSCOgD7ye8ihu87EAAgYiAAK58OlJQWPvsbfuRDIqBA")


@bot.message_handler(commands=['annualleaveform'])
def send_message(message):
    """отправка файла - № 73 Заявление на ТРУДОВОЙ отпуск.docx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAANCYz0h0M0pfBhrX0x5D8g8gcyChw4AAg0iAAK58OlJ9yg2ZO0mblcqBA")


@bot.message_handler(commands=['leavewithoutpayform'])
def send_message(message):
    """отправка файла - № 74 Заявление на  ОТПУСК БЕЗ СОХРАНЕНИЕ зп.docx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAANEYz0iWmMSDXPv9bv2ngPCDAw3GO0AAhQiAAK58OlJWKZWvHCMI7QqBA")


@bot.message_handler(commands=['explanationrefusalact'])
def send_message(message):
    """отправка файла - № 75 Акт об отказе дачи объяснений.docx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAANFYz0i3bqwU_FYNCaWvcdW6geZvVkAAhsiAAK58OlJmXJdpNd0_G0qBA")


@bot.message_handler(commands=['maternityleaveform'])
def send_message(message):
    """отправка файла - № 77 Заявление на отпуск по БЕРЕМЕННОСТИ и РОДАМ.docx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAANGYz0jioNYjh0WgIIAAWXFN5dn-5IIAAIdIgACufDpSYHfDq29GcdVKgQ")


@bot.message_handler(commands=['withoutpaytomaternityleaveform'])
def send_message(message):
    """отправка файла - № 79 Заявление на  отпуск БЕЗ СОХРАНЕНИЕ ЗП ПО УХОДУ  за ребенком.docx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAANHYz0kHkcxyMlujeXVqdyONL53a9QAAiEiAAK58OlJCfmWc4Zc3wQqBA")


@bot.message_handler(commands=['explanatoryreport'])
def send_message(message):
    """отправка файла - № 80 бланк объяснительная.docx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAANIYz0kpDIzTd6lB82swwcq0zpzAwIAAiUiAAK58OlJJeLyMc4llykqBA")


@bot.message_handler(commands=['personalgoalleaveform'])
def send_message(message):
    """отправка файла - № 159 Заявление за ОТСУТСТВИЕ в личных целях.docx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAANJYz0lFey1DFiG5bLa0stOpWMXH-oAAiwiAAK58OlJGNO3ODvO5rQqBA")


@bot.message_handler(commands=['additionalrestdayafterdonation'])
def send_message(message):
    """отправка файла - № 238 Заявление на ДОП.ДЕНЬ ОТДЫХА после дня донации.docx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAANKYz0l7J47GnvMJZ7SsK9iQ09BB_UAAjIiAAK58OlJcxaIOxJWK0cqBA")


@bot.message_handler(commands=['exitfrommaternityleave'])
def send_message(message):
    """отправка файла - № 241 Заявление о ВЫХОДЕ с отпуска по уходу за ребенком.docx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAANLYz0mbGWLx_oX1d2oDf4ywwt-yrMAAjQiAAK58OlJZsYh9QtXMFoqBA")


@bot.message_handler(commands=['onedayleavewithpay'])
def send_message(message):
    """отправка файла - № 300 заявление на ОДИН день с сохранением ЗП.doc"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAANMYz0m-8aa7V5sdU4cw5oBdFYscBQAAjgiAAK58OlJTxlH1rHROR8qBA")


@bot.message_handler(commands=['fourhourleavewithpay'])
def send_message(message):
    """отправка файла - № 301 заявление на 4 часа с сохранением ЗП.doc"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAANNYz0nhNa64dk0BNV5TMLHyITP1eMAAj4iAAK58OlJqxZSkoAktE8qBA")


@bot.message_handler(commands=['annualleavetransfer'])
def send_message(message):
    """отправка файла - № 320 Заявление на перенос трудового отпуска.docx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAANOYz0n70algqZ84sTeDa3TG_4CHCYAAkIiAAK58OlJ90Kt0FtatO4qBA")


@bot.message_handler(commands=['keycardreissue'])
def send_message(message):
    """отправка файла - № 336 Заявление на выдачу элект.пропуска.docx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAANPYz0ozkKRUpgnPBqXGPgxFOXkDF8AAkciAAK58OlJkQABdcxMZ5VFKgQ")


@bot.message_handler(commands=['workplaceabsenceactoneday'])
def send_message(message):
    """отправка файла - № 352 (один день) Акт об отсутствии на рабочем месте.docx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAANQYz0qTnyxTaS6QsUfspHrQAdXJhEAAlMiAAK58OlJ11k2Vm6PdrsqBA")


@bot.message_handler(commands=['workplaceabsenceactweek'])
def send_message(message):
    """отправка файла - № 353 (неделя) Акт об отсутствии на рабочем месте.docx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAANRYz0r8MuxfI9MRiVPBnZbavSqifcAAlwiAAK58OlJQ_svhvMMUJQqBA")


@bot.message_handler(commands=['freewarehousepassreissue'])
def send_message(message):
    """отправка файла - № 401 Заявление о восстановлении пропуска на свободный склад.docx"""
    bot.send_document(chat_id=message.chat.id, document="BQACAgIAAxkBAANSYz0tkr6m8EUgVRlzPliE9FJgYFsAAmMiAAK58OlJfYy-a-WfkOMqBA")




# @bot.message_handler(commands=['audiogreeting'])
# def send_message(message):
#     """отправка voice файла"""
#     bot.send_audio(chat_id=message.chat.id, audio="") #send voice
#
#
# @bot.message_handler(commands=['get_pic'])
# def send_message(message):
#     """отправка картинки"""
#     bot.send_photo(chat_id=message.from_user.id, photo="") #send picture1
#     bot.send_photo(chat_id=message.chat.id, photo="") #send picture2




@bot.message_handler(commands=['start', 'greeting'])
def send_message(message):
    #bot.reply_to(message, message="Для ")

    bot.send_photo(chat_id=message.chat.id, photo="AgACAgIAAxkBAAMTYz0ZX71e-YWqVkkTeVa05dNt1VEAAkDEMRu58OlJHVa3cfB8booBAAMCAANzAAMqBA")  # send pic

    txt1 = """
    Добрый день! Направляю памятку для работников/руководителей, обращающихся в телеграмм бот.

Все бланки заявлений можно загружать с помощью команд в данном Telegram боте.

1. Ежегодный трудовой отпуск предоставляется согласно графика отпусков. Заявление на ежегодный трудовой отпуск (Форма № 73) согласованное непосредственным руководителем (мастером/начальником) предоставляется в отдел кадров за 5 (пять) рабочих дней до начала отпуска.
В случае, если работник по каким-либо уважительным причинам предоставил заявление меньше чем за 5 (пять) рабочих дней, то заявление на ежегодный трудовой отпуск необходимо также согласовать с главным бухгалтером.
В случае, если работник уходит в трудовой отпуск не по графику отпусков, то также необходимо предоставить заявление о переносе ежегодного трудового отпуска (Форма № 320), согласованное с непосредственным руководителем (мастером/начальником).
 
2. В случае, отсутствия работника на рабочем месте по личным причинам, работник должен заблаговременно предоставить в отдел кадров согласованное с непосредственным руководителем (мастером, начальником) заявление об отпуске без сохранения заработной платы (Форма № 74) либо заявление об отсутствии в личных целях (по часам) (Форма № 159).
 
3. В случае, если работник по вопросам деятельности предприятия отлучается с рабочего места во время рабочего дня, то необходимо подготовить служебную записку (бланк оформляется в 1С документообороте). Служебную записку можно оформлять в конце каждого месяца (указать все дни, когда работник отлучался с работы и время уход-приход).
 
4.  Согласно п. 5.14 Коллективного договора, работнику предоставляет 1 (один) день с сохранением заработной платы в следующих случаях (Форма №300):
- в связи с регистрацией брака;
-  в связи с рождением ребенка;
- смерти близкого родственника (отец, мать, дедушка, бабушка, полнородные и неполнородные братья и сестры, внуки, дети).
Работник должен предоставить в отдел кадров согласованное с непосредственным руководителем заявление (Форма № 300), затем в течении недели после наступления события необходимо в отдел кадров предоставить: свидетельство о браке, свидетельство о рождении ребенка. Свидетельство о смерти либо справка о смерти предоставляется в канцелярию для оформления материальной помощи работнику.
 
5.  Согласно п. 5.5 Коллективного договора, в дни сдачи (донации) крови и её компонентов работник, являющийся донором, освобождается от работы Работодателем с сохранением средней заработной платы. За донацию крови работнику предоставляется 2 (два) дня с сохранением заработной платы, которые он должен выбрать в течение 1 года. Первый день работник должен отгулять в день сдачи крови. Началом истечения года является день сдачи крови. При этом работник за первый день донорства предоставляет в отдел кадров оригинал справки (форма № 123/у), выданной в КГП «Областной центр крови» УЗАКО, за 2 день донорства работник предоставляет копию справки + заявление (Форма № 238).
 
6.  Согласно п. 5.15 Коллективного договора, работнику предоставляется 4 часа оплачиваемого отгула для одного из родителей, имеющего ребенка до 11-ти лет, для участия в празднике «Первое сентября». Работник должен заблаговременно предоставить в отдел кадров согласованное с непосредственным руководителем заявление (Форма № 301).
 
7. В случае, если работник не выходит на работу без уважительной причины, непосредственный руководитель (мастер/начальник) должен предоставить в отдел кадров акт об отсутствии на рабочем месте (Форма № 352 либо Форма № 353) + объяснительная работника (Форма № 80) либо акт об отказе дачи объяснения (Форма № 75), перед тем как требовать объяснительную с работника необходимо ознакомить его с Требованием и подписывать его заместителем директора, курирующего ваше подразделение (бланк "Требование")"""

    txt2 = """8.  При предоставлении в отдел кадров служебной записки на продление рабочего дня либо на выход на работу в выходной день (бланк расположен в 1С документообороте) к ней прилагается лист согласие работников. В листе согласии указывается фактическое время пребывания на рабочем месте (приход – уход), также данная информация будет проверятьcя при помощи электронной системы CKУД, в случае, если данные указанные в листе согласии не будут отражаться системе СКУД, данное время учитываться не будет. Лист согласия должен быть подписан непосредственным руководителем (мастером/начальником), руководителем структурного подразделения, начальником курирующий данное структурное подразделение, а также первым заместителем директора.

9.  При утере электронного ключа (чипа), работник должен написать заявление об утере ключа и выдачи нового (Форма № 336), согласовать с непосредственным руководителем (мастером/начальником), с этим заявлением обратиться в бухгалтерию, оплатить 500 (Пятьсот) тенге. Вместе с заявлением и квитанцией подойти к специалисту отдела кадров для получения нового электронного ключа. Также для подтверждения нахождения работника на рабочем месте оформляется заявление формы № 81, подписывается руководителем и службой безопасности.
 
10.  При утере таможенного пропуска, работник должен написать заявление о выдачи нового пропуска (Форма № 401), подписать непосредственным руководителем. С данным заявлением и фотографией подойти к специалисту отдела кадров для получения нового таможенного пропуска.
 
11.  В заявлении о расторжении трудового договора (Форма № 72 и Форма 375 для лиц с полной материальной ответственностью согласно приказа директора №1-П/1 от 05.01.22) непосредственный руководитель (начальник/мастер) должен указать будет отработка у работника или не будет (например, «с отработкой 1месяц», либо «без отработки»), также надо указать является ли последний рабочий день рабочим или не рабочим (Например, «30.11.2021г. считать рабочим днём» либо «30.11.2021г. считать не рабочим днём»). Заявление о расторжении трудового договора должно быть подписано непосредственным руководителем (мастером/начальником), руководителем структурного подразделения, а также начальником управления по работе с персоналом. Подписанное заявление предоставляется в отдел кадров заблаговременно.
При увольнении, если последний рабочий день является у Работника рабочим днём, то он приходит за обходным листом в отдел кадров после 14.00 часов. Если последний рабочий день, является не рабочим днём, то работник обходной лист может взять в течение рабочего дня.
 
12.  Непосредственный руководитель (мастер/начальник) должен на ежедневной основе вести табель учёта рабочего времени (Приложение № 1-шаблон, образец табеля ).
Еженедельно непосредственный руководитель (мастер/начальник) отправляет табель учета рабочего времени специалисту отдела кадров для предварительной проверки.
Первого числа каждого месяца непосредственный руководитель (мастер, начальник) отправляет табель учета рабочего времени специалисту отдела кадров для закрытия месяца.

12. При выходе в отпуск по беременности и родам (при предъявлении больничного листа в двух экземплярах) и в дальнейшем оформления выхода в отпуск по уходу за ребенком (при предъявлении свидетельства о рождении ребенка) оформляются бланки заявлений формы №77, №79. В случае, если работник собирается выйти на работу с отпуска по ухода за ребенком раньше указанного срока, то необходимо заполнить бланк заявления формы № 241 заблаговременно, то есть за 1 месяц. А руководителю работника оформить служебную записку в 1С документообороте об изменении оклада и также в случае возвращения работника со службы в армии.
    """

    txt3 = """13. В случае вопроса какие и где оформляются служебные записки:
оформляются СЗ в 1С документообороте и регистрируются заблаговременно в следующих в случаях -  необходимости расширения штата/оптимизации штата, непосредственный руководитель (мастер/начальник) оформляет служебную записку о внесении изменений в штатное расписание; оформления доплаты сотрудникам за: бригадирство, наставничество, возложение обязанностей, расширение зоны обслуживания, совмещение должности, изменение заработной платы, премирование (дата, с которой назначается доплата должна совпадать с датой регистрации служебной записки в канцелярии либо должна быть зарегистрирована заблаговременно); оформления командировки, работы в выходной день, продлении рабочего дня, перемещении работников, изменении графика работ, удаленной работе, о внесении изменений в штатное расписание (вывод из штата), о внесении изменений в штатное расписание (расширение штата), об отсутствии на рабочем месте без уважительной причины, об отсутствии на рабочем месте по вопросам деятельности предприятия, отзыва из ежегодного трудового отпуска, зарегистрированные в канцелярии в день отзыва из ежегодного трудового отпуска.
 
По вопросам установления программы 1С документооборот обращаться в отдел информационных технологий специалистам Двуреченской Дарье Константиновне и Евстафьевой Яне Станиславовне. Контакты можно найти в справочнике.
 
P.S.: Все виды заявлений работник пишет у своего непосредственного руководителя (мастера/начальника), кроме, заявления на перевод.
    """
    bot.send_message(chat_id=message.chat.id, text=txt1)
    bot.send_message(chat_id=message.chat.id, text=txt2)
    bot.send_message(chat_id=message.chat.id, text=txt3)





bot.polling()
