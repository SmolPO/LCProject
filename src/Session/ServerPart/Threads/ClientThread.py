
from threading import Thread
from ServerThread import QueueSvr

class ClientThread(Thread):
    """
    слушает очередь сообщений QueueCln
    служит как ретранслятор сообщений в базу данных и очередь QueueSvr
    тоже изменяет значение Users в поле пакета.
    содержит функцию listenQueue, которая отбирает сообщения именно для этого потока.
    """
    def __init__(self):
        pass

    def run(self):
        """
        ждет пока появиться сообщение для себя
        отправлять операцию в БД операций
        отправлять сообщение в серверную очередь
        :return:
        """
        while True:
            mess = self.listenQueue()
            self.AnaliseMess(mess)
        pass


    def listenQueue(self):
        """
        так же, что и в классе clnAnaliseQueue
        тоже отбирает сообщения для себя, вощращает их и уменьшает поле Users этого соощения на 1
        :return:
        """
        pass
