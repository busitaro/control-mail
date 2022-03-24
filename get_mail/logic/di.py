from injector import Module

from .interface import Logic
from .attachment import AttachmentLogic


class LogicDiModule(Module):
    def __init__(self, mode: str, daemonize: bool):
        self.__mode = mode
        self.__daemonize = daemonize

    def configure(self, binder):
        if self.__mode == 'attachment':
            binder.bind(Logic, to=AttachmentLogic(self.__daemonize))
        else:
            raise ValueError('指定されたモードが存在しません')
