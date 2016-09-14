from threading import Thread


class PPAnaliseCache(Thread):
    """слушает очередь сообщеений.
    При получение нового: распарсивает и анализирует
    """
    def __init__(self):
        """
        пока не знаю, что сюда писать
        """
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
        содержит в себе свитч по командам.
        :param mess:
        :return:
        """

        pass