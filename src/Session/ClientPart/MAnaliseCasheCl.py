
from threading import Thread
import RubbitMQ


class AnaliseCaсheCl(Thread):
    """
    слушает очередь сообщеений. При получение нового: распарсивает.
    """
    def __init__(self):
        pass


    def run(self):
        """

        :return:
        """
        while True:
            # запускается из rubbitMQ. Очередь передает сюда сообщение.
            self.ParseMess(mess)
            self.AnaliseMess(mess)


    def AnaliseMess(self, mess):
        """
        парсит сообщение
        анализирует сообщение
        содержит в себе свитч по командам.
        :param mess:
        :return:
        """
        pass


    def ParseMess(self, mess):
        """
        парсит сообщение
        :param mess:
        :return:
        """
        pass