from django.utils.safestring import mark_safe

AGES = (
    ('1', 'до 12'),
    ('2', 'от 12 до 18'),
    ('3', 'от 18 до 25'),
    ('4', 'от 25 до 40'),
    ('5', 'от 40 до 55'),
    ('6', 'от 55'),
)
GENDERS = (
    ('1', 'Мужской'),
    ('2', 'Женский'),
)
COLORS = (
    ('1', 'Красный'),
    ('2', 'Оранжевый'),
    ('3', 'Желтый'),
    ('4', 'Зелёный'),
    ('5', 'Голубой'),
    ('6', 'Синий'),
    ('7', 'Фиолетовый'),
)
SEASONS = (
    ('1', 'Зима'),
    ('2', 'Весна'),
    ('3', 'Лето'),
    ('4', 'Осень'),
)
SCOPES = (
    ('1', 'Учёба'),
    ('2', 'Работа'),
    ('3', 'Пенсия'),
)
PURPOSES = (
    ('1', 'Развлечение'),
    ('2', 'Учёба'),
    ('3', 'Работа'),
    ('4', 'Общение'),
)
COUNTS = (
    ('1', 'до 5'),
    ('2', 'от 5 до 25'),
    ('3', 'от 25 до 100'),
    ('4', 'от 100'),
)

CHOICES1 = (
    ('1', mark_safe(u'<img src="/static/images/help1.jpg" width="250px" height="100px"/>')),
    ('2', mark_safe(u'<img src="/static/images/help2.jpg" width="250px" height="100px"/>'))
)
CHOICES2 = (
    ('1', mark_safe(u'<img src="/static/images/chat1.jpg" width="250px" height="200px"/>')),
    ('2', mark_safe(u'<img src="/static/images/chat2.png" width="200px" height="170px"/>'))
)
CHOICES3 = (
    ('1', mark_safe(u'<img src="/static/images/friend1.png" width="150px" height="150px"/>')),
    ('2', mark_safe(u'<img src="/static/images/friend2.png" width="250px" height="100px"/>'))
)
CHOICES4 = (
    ('1', mark_safe(u'<img src="/static/images/setting1.jpg" width="150px" height="150px"/>')),
    ('2', mark_safe(u'<img src="/static/images/setting2.png" width="200px" height="100px"/>'))
)
CHOICES5 = (
    ('1', mark_safe(u'<img src="/static/images/group1.jpg" width="150px" height="150px"/>')),
    ('2', mark_safe(u'<img src="/static/images/group2.png" width="250px" height="125px"/>'))
)

THEMES = (
    ('1', 'Светлая'),
    ('2', 'Тёмная'),
)
PREFS = (
    ('1', 'Все функции видны сразу.'),
    ('2', 'Отображаются только необходимые функции.'),
    ('3', 'Отображается минимальное количество элементов.'),
)

PREFS2 = (
    ('1', 'Общение'),
    ('2', 'Группы'),
    ('3', 'Настройки'),
    ('4', 'Найти друга'),
    ('5', 'Помощь'),
    ('6', 'Просто элемент \"Меню\"'),
)

FONTS = (
    ('1', 'Маленький'),
    ('2', 'Средний'),
    ('3', 'Большой'),
    ('4', 'Крупный'),
)
