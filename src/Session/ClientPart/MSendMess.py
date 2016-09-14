

class ClnSendMess:
    """
    содержит в себе только интерфейс отправки сообщений. В методе инит прописываются уникальные параметры для клиента. Сокет
    пароль, логин.... все что уникально для этого соединения.
    Или все это можно брать из класса ClientApp.
    индивидуален для каждого АРМ, так как содержит сокет (и еще что то в будущем) уникальное для каждого АРМ
    """
    ARMSocket = None

    def __init__(self, sock):
        self.ARMSocket = sock

    def sendMessage(self, mess):
        """
        отправка на сокет, забитый в классе ClientApp
        :param mess: [] список данный. Создается в методе createMessage
        :return: true or false
        """
        return self.ARMSocket.send(mess)

    def createMessage(self, cmd, sender, data, nextMess):
        """
        создает сообщение для отправки. Может стоит упразднить из-за тривиальности
        :param cmd:
        :param sender:
        :param data:
        :param nextMess:
        :return:
        """
        return [cmd, sender, data, nextMess]



