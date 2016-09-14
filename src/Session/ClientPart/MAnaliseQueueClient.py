from threading import Thread

class ClnAnaliseQueueCln(Thread):
    """

    """
    def __init__(self):
        pass

    def run(self):
        """
        либо слушает очередь, либо сама очередь передает сюда сообщение.
        :return:
        """

        while True:
            self.AnaliseMess(mess) #mess - не объявленная пока переменная; сообщение, переданное из очереди


    def AnaliseMess(self, mess):
        """
        огромный свитч на все команды.
        :param mess:
        :return:
        """
        pass
