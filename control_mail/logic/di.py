from injector import Module

from .interface import Logic
from .attachment import AttachmentLogic
from .forward import ForwardLogic
from .send import SendLogic
from .message import MessageLogic


class LogicDiModule(Module):
    def __init__(self, mode: str, daemonize: bool):
        self.__mode = mode
        self.__daemonize = daemonize

    def configure(self, binder):
        if self.__mode == 'attachment':
            binder.bind(Logic, to=AttachmentLogic(self.__daemonize))
        elif self.__mode == 'forward':
            binder.bind(Logic, to=ForwardLogic(self.__daemonize))
        elif self.__mode == 'send':
            binder.bind(Logic, to=SendLogic())
        elif self.__mode == 'get_mail':
            binder.bind(Logic, to=MessageLogic())
        else:
            raise ValueError('指定されたモードが存在しません')
