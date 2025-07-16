'''
Структура вопроса:
number - Номер вопроса. 1, 2, 3....
text - Текст вопроса
photo - фото к вопросу. 1 или несколько штук
type_button - тип кнопки. [some_buttons - InlineKeybaordMarkup. Несколько вариантов ответа; one_buttons - InlineKeyboardMarkup. Один вариант ответа; text - Ручной ввод]
buttons - массив кнопок.
skip - Пропуск вопроса.
check" - Проверка ответа.
db_column_num - Номер ячейки вопроса в базе данных.
ques_logic - Логика пропуска в зависимости от выбранных ответов.
'''

ALL_QUESTIONS = [
    [
        {
            "number": 0,
            "text": "Выберите категорию объекта",
            "photo": [],
            "type_button": "one_buttons",
            "buttons": ["Квартира", "Дом"],
            "skip": None,
            "check": None,
            "db_column_num": 0,
            "ques_logic": None
        },
        {
            "number": 1,
            "text": "Введите ваше имя и фамилию",
            "photo": [],
            "type_button": "text",
            "buttons": [],
            "skip": None,
            "check": None,
            "db_column_num": 1,
            "ques_logic": None
        },
        {
            "number": 2,
            "text": "Укажите адрес объекта. Для этого отправьте ссылку на объект на Яндекс Картах",
            "photo": [],
            "type_button": "text",
            "buttons": [],
            "skip": None,
            "check": None,
            "db_column_num": 2,
            "ques_logic": ["IF", 0, "==", [1], 5]
        },
        {
            "number": 3,
            "text": "Номер квартиры\n\nВведите только число",
            "photo": [],
            "type_button": "text",
            "buttons": [],
            "skip": None,
            "check": "int",
            "db_column_num": 3,
            "ques_logic": None
        },
        {
            "number": 4,
            "text": "Этаж\n\nВведите только число",
            "photo": [],
            "type_button": "text",
            "buttons": [],
            "skip": None,
            "check": "int",
            "db_column_num": 4,
            "ques_logic": None
        },
        {
            "number": 5,
            "text": "Фотографии объекта или ссылка на фотографии объекта (Например, на яндекс диск/гугл драйв и тд)\n\nПри отправке ссылки проверьте, пожалуйста, чтобы к файлам был открыт общий доступ",
            "photo": [],
            "type_button": "text",
            "buttons": [],
            "skip": None,
            "check": "some_photo",
            "db_column_num": 5,
            "ques_logic": None
        },
        {
            "number": 6,
            "text": "Описание объекта",
            "photo": [],
            "type_button": "text",
            "buttons": [],
            "skip": None,
            "check": None,
            "db_column_num": 6,
            "ques_logic": None
        },
        {
            "number": 7,
            "text": "Площадь объекта (м.кв)\n\nВведите только число",
            "photo": [],
            "type_button": "text",
            "buttons": [],
            "skip": None,
            "check": "int",
            "db_column_num": 7,
            "ques_logic": ["IF", 0, "==", [0], 10]
        },
        {
            "number": 8,
            "text": "Потолок: max высота",
            "photo": [],
            "type_button": "text",
            "buttons": [],
            "skip": None,
            "check": "float",
            "db_column_num": 8,
            "ques_logic": None
        },
        {
            "number": 9,
            "text": "Потолок: max высота",
            "photo": [],
            "type_button": "text",
            "buttons": [],
            "skip": None,
            "check": "float",
            "db_column_num": 9,
            "ques_logic": ["IF", 0, "==", [1], 11]
        },
        {
            "number": 10,
            "text": "Потолок: высота",
            "photo": [],
            "type_button": "text",
            "buttons": [],
            "skip": None,
            "check": "float",
            "db_column_num": [8, 9],
            "ques_logic": None
        },
        {
            "number": 11,
            "text": "Стоимость 14часовой смены на вашем объекте",
            "photo": [],
            "type_button": "text",
            "buttons": [],
            "skip": None,
            "check": "float",
            "db_column_num": 10,
            "ques_logic": None
        },
        {
            "number": 12,
            "text": "Готовы ли вы к короткой смене (Например, 7часовой за 50% от стоимости 14часовой смены)",
            "photo": [],
            "type_button": "one_buttons",
            "buttons": ["Да", "Нет"],
            "skip": None,
            "check": None,
            "db_column_num": 11,
            "ques_logic": ["IF", 12, "==", [1], 14]
        },
        {
            "number": 13,
            "text": "Минимальный порог оплаты",
            "photo": [],
            "type_button": "text",
            "buttons": [],
            "skip": None,
            "check": None,
            "db_column_num": 12,
            "ques_logic": None
        },
        {
            "number": 14,
            "text": "Платный ли въезд на парковку?",
            "photo": [],
            "type_button": "one_buttons",
            "buttons": ["Да", "Нет"],
            "skip": None,
            "check": None,
            "db_column_num": 13,
            "ques_logic": None
        },
        {
            "number": 15,
            "text": "Временные и прочие ограничения на въезд",
            "photo": [],
            "type_button": "text",
            "buttons": [],
            "skip": None,
            "check": None,
            "db_column_num": 14,
            "ques_logic": None
        },
        {
            "number": 16,
            "text": "Ограничения по доступу на объект",
            "photo": [],
            "type_button": "text",
            "buttons": [],
            "skip": None,
            "check": None,
            "db_column_num": 15,
            "ques_logic": None
        },
        {
            "number": 17,
            "text": "Порядок оформления пропусков",
            "photo": [],
            "type_button": "text",
            "buttons": [],
            "skip": None,
            "check": None,
            "db_column_num": 16,
            "ques_logic": ["IF", 0, "==", [1], 19]
        },
        {
            "number": 18,
            "text": "Лифт",
            "photo": [],
            "type_button": "some_buttons",
            "buttons": ["Грузовой", "Пассажирский", "Отсутствует"],
            "skip": None,
            "check": None,
            "db_column_num": 19,
            "ques_logic": None
        },
        {
            "number": 19,
            "text": 'Фото или файл с планировкой объекта\n\nВведите "Нет", если нет такого фото',
            "photo": [],
            "type_button": "text",
            "buttons": [],
            "skip": None,
            "check": "one_photo_all",
            "db_column_num": 18,
            "ques_logic": ["IF", 0, "==", [1], 21]
        },
        {
            "number": 20,
            "text": "Особенности объекта (выберите несколько штук)",
            "photo": [],
            "type_button": "some_buttons",
            "buttons": ["Съёмки с игровыми животными", "Можно двигать мебель", "Готовы к перекраске стен", "Нужна сменная обувь", "Хейзер, дым-машина"],
            "skip": None,
            "check": None,
            "db_column_num": 19,
            "ques_logic": ["IF", 0, "==", [0], 22]
        },
        {
            "number": 21,
            "text": "Особенности объекта (выберите несколько штук)",
            "photo": [],
            "type_button": "some_buttons",
            "buttons": ["Съёмки с игровыми животными", "Можно двигать мебель", "Готовы к перекраске стен", "Нужна сменная обувь", "Курение на территории", "Хейзер, дым-машина", "Отопление", "Водоснабжение"],
            "skip": None,
            "check": None,
            "db_column_num": 20,
            "ques_logic": None
        },
        {
            "number": 22,
            "text": "Есть ли газовая плита?",
            "photo": [],
            "type_button": "one_buttons",
            "buttons": ["Да", "Нет"],
            "skip": None,
            "check": None,
            "db_column_num": 21,
            "ques_logic": None
        },
        {
            "number": 23,
            "text": "Соседи",
            "photo": [],
            "type_button": "one_buttons",
            "buttons": ["Ангелы", "Демоны", "Без соседей"],
            "skip": None,
            "check": None,
            "db_column_num": 22,
            "ques_logic": ["IF", 0, "==", [0], 27]
        },
        {
            "number": 24,
            "text": "Туалет",
            "photo": [],
            "type_button": "one_buttons",
            "buttons": ["Септик", "Центральная канализация", "Отсутствует"],
            "skip": None,
            "check": None,
            "db_column_num": 23,
            "ques_logic": None
        },
        {
            "number": 25,
            "text": "Подключение электричества",
            "photo": [],
            "type_button": "one_buttons",
            "buttons": ["220 В", "380 В", "Отсутствует"],
            "skip": None,
            "check": None,
            "db_column_num": 24,
            "ques_logic": None
        },
        {
            "number": 26,
            "text": "Количество кВт",
            "photo": [],
            "type_button": "one_buttons",
            "buttons": ["До 25 кВт", "От 25 до 50 кВт", "От 50 до 110 кВт", "Более 110 кВт"],
            "skip": None,
            "check": None,
            "db_column_num": 25,
            "ques_logic": ["IF", 25, "==", [2], 27]
        },
        {
            "number": 27,
            "text": "Ограничения / особые пожелания собственника объекта",
            "photo": [],
            "type_button": "text",
            "buttons": [],
            "skip": None,
            "check": None,
            "db_column_num": 26,
            "ques_logic": None
        }
    ]
]