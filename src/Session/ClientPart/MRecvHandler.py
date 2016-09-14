"""

"""


from threading import Thread
from MClientApp import ClientApp
from MQueueCln import clQueueCln

class ClnRecvHandle(Thread):
    """
    прием сообщений с АРМ и добавление их в очередь.
    """
    IsConnect = True # есть ли связь с клиентом
    ARMSocket = None # на время. Потом либо оставить в этом классе, либо использовать одни из ClientApp
    def __init__(self, sock):
        """
        пока не знаю, что сюда писать.
        """
        self.ARMSocket = sock
        pass

    def run(self):
        """
        цикл while пока есть соединение.
        на ожидание данных
        :return:
        добавление в очередь данных.
        входящий пакет - поток байт. Последние ClientApp.SIZE_BYTES указывают, сколько байт с конца посылки
        определяют размер следующей посылки
        второй while пока размер следующего пакета не равен 0
        добавление в очередь
        """
        while self.IsConnect:
            mess = self.ARMSocket.recv(ClientApp.SIZE_HEADER) #!!!!ClientApp.SIZE_HEADER!!!!
            if not mess:
                pass #ошибка
            else:
                #отделить последние N байт для определения размера следующей посылки.
                self.addToCacheClient(mess)
                sizeNextPack = self.sizeNextPacket(mess)
                while sizeNextPack > 0:
                    nextMess = self.ARMSocket.recv()  # !!!!ClientApp.SIZE_HEADER!!!!
                    if not nextMess:
                        pass
                    else:
                        self.addToCacheClient(nextMess)
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


    def addToCacheClient(self, mess):
        """
        :param mess:
        :return:
        """
        pass

