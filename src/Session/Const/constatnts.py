"""
Содержит все константы для работы сервера

* время ожидания подтвержденияв
* время, через коноторе GC будет проверять очередь

Как создавать класс
* передавать словарь со значениями. Пример {DB_Res_O=6, GC_T_O=2, ... }
"""
class myConst:
    """
    алгоритм наименования. ДЛЯ КОГО_ИМЯ
    Пример DB(чья)_RESPONSE_TIME(что за константа)
    """
    DB_RESPONSE_TIME = None # максимальное время на получение подтверждения в DBOperations
    GC_TIME_OUT      = None # время тайм-аута для GC из класса БД для проверки DBOperations.
    SIZE_FIELD       = None # размер кол-ва байт в конце каждого сообщения, хранящих рамер следующего пакета

    # def __init__(self, DB_Res_T, GC_T_O):
    #     """
    #     инициализация констант. Можно передавать просто словарем с ключами.
    #     :param DB_Res_T:
    #     :param GC_T_O:
    #     """
    #     self.DB_RESPONSE_TIME = DB_Res_T
    #     self.GC_TIME_OUT = GC_T_O
