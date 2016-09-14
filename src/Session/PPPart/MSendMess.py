
class ClnSendMess:
    """
    содержит в себе только интерфейс отправки сообщений. В методе инит прописываются уникальные параметры для ПП. Сокет
    пароль, логин.... все что уникально для этого соединения.
    Или все это можно брать из класса PPApp.
    индивидуален для каждого ПП, так как содержит сокет (и еще что то в будущем) уникальное для каждого ПП
    """
    PPSocket = None

    def __init__(self, sock):
        self.PPSocket = sock

    def sendMessage(self, mess):
        """
        отправка на сокет, забитый в классе PPApp
        :param mess: [] список данный. Создается в методе createMessage
        :return: true or false
        """
        return self.PPSocket.send(mess)

    def createMessage(self, cmd, sender, data, nextMess):
        """
        создает сообщение для отправки. Возможно стоит празднить
        :param cmd:
        :param sender:
        :param data:
        :param nextMess:
        :return:
        """
        return [cmd, sender, data, nextMess]
