"""
Client

Заметки:
    *соединение создает класс Connect. Он полность выполняет задачи получени правд доступа и авторизации.
        Он передает классу ClientApp сокет соединения
    * Очередь входящих сообщений хранится в классе ClientApp.
    * ARM - слиент. Расшифровывается как автомотизированная рабочая м...
    * Разобраться как работает соединение в питоне. Как декодировать и кодировать сообщенения.
    * использовать ClientApp как класс констант. То есть обращаться к полям класса, объявленным по умолчанию

    * разобрать с доступом к переменным, хранящимся в других модулях.

    * когда закрывать все потоки. После обрыва соединения или как то еще отслеживать это. И кто их будет закрывать?
        заовдить переменную для этого или завершать из класса ClientApp?

    * передача всех переменных из класса Connection можно сделать через словарь ключ-значение
    * смущает связь между классами. Надо как то из жестко закрепить за определенным ClientApp.
        А то связь получается очень хлипкая и неопределенная

"""
import socket
from threading import Thread

from MAnaliseQueueClient import ClnAnaliseQueueCln
from MAnaliseCasheCl import AnaliseCasheCl
from MQueueCln import clQueueCln
from MRecvHandler import ClRecvHandle
from MSendMess import ClSendMess


class ClientApp(Thread):
    #классы
    RecvHandle         = None
    AnaliseQueueClient = None
    AnaliseCasheCl     = None
    MessageFromARM     = None  #RubMQ

    #константы
    # Может лучше перенести в класс MyConst?
    SIZE_BYTES      = None  # размер
    SIZE_HEADER     = None  # размер заголовочного сообщения

    #частное
    ID = None  # для каждого подключения свой ID
    ARMSocket = None  # сокет соединения

    def __init__(self, sock, id):
        """
        создает все классы
        :param sock:
        """
        self.RecvHandle         = ClnRecvHandle()
        self.AnaliseCaсheCl = AnaliseCacheeClient()
        self.AnaliseQueueClient    = ClnAnaliseQueueCln()
        #self.MessageFromARM    = RubMQ
        self.ID = id
        self.ARMSocket = sock

        pass

    def run(self):
        """
        запускает все потоки клиента. Активизирует сущность клиента

        """
        self.RecvHandle.start()
        self.AnaliseCacheCl.start()
        self.AnaliseQueueClient.start()
        pass




