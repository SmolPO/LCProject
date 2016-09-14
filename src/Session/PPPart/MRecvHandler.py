"""

"""


from threading import Thread
from MPowerPostApp import PPApp
from MQueuePP import clQueuePP


class RecvHandle(Thread):
    """
    прием сообщений с АРМ и добавление их в очередь.
    """
    IsConnect = True # есть ли связь с клиентом
    PPSocket = None  # на время. Потом либо оставить в этом классе, либо использовать одни из ClientApp

    def __init__(self, sock):
        """
        пока не знаю, что сюда писать.
        """
        self.PPSocket = sock
        pass

    def run(self):
        """
        цикл while пока есть соединение.
        на ожидание данных
        :return:
        добавление в очередь данных.
        входящий пакет - поток байт. Константа  указывают, сколько байт с конца посылки
        определяют размер следующей посылки
        второй while пока размер следующего пакета не равен 0
        добавление в очередь
        """
        while self.IsConnect:
            mess = self.PPSocket.recv(Protocol.SIZE_BYTES) #!!!!ClientApp.SIZE_HEADER!!!!
            if not mess:
                pass #ошибка
            else:
                #отделить последние SIZE_BYTES байт для определения размера следующей посылки.
                self.addToCachePP(mess)
                sizeNextPack = self.sizeNextPacket(mess)
                while sizeNextPack > 0:
                    nextMess = self.PPSocket.recv()  # !!!!Protocol.SIZE_BYTES!!!!
                    if not nextMess:
                        pass
                    else:
                        self.addToCachePP(nextMess)
                        sizeNextPack = self.sizeNextPacket(nextMess)
                pass
            pass
        pass


    def sizeNextPacket(self, mess):
        """
        из байт отбирает последине N байт и переводит в int
        :param mess: байты
        :return: int
        """
        pass


    def addToCachePP(self, mess):
        """
        проблема читателей и писателей ПЧиП !!!!
        :param mess:
        :return:
        """

        pass

