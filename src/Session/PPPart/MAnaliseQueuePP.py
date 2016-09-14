from  threading import Thread


class PPAnaliseQueue(Thread):
    def __init__(self):
        pass

    def run(self):
        """
            работает как воркер для очереди. Полчает необходимые сообщения из очереди
            :return:
            """

        while True:
            #Пробуждается при появление нового сообщения
            self.AnaliseMess(mess)
            pass


    def AnaliseMess(self, mess):
        """
        огромный свитч на все команды.
        :param mess:
        :return:
        """
        pass