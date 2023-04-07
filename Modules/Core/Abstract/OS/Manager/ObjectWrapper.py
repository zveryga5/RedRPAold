from abc import ABC, abstractmethod
from Modules.Core.Descriptors.ObjectDescriptor import ObjectDescriptor
from Modules.Core.Abstract.OS.Manager.Window import AbstractWindow


class WindowObject:
    def __init__(self, window: AbstractWindow, object_desc: ObjectDescriptor):
        self._object = object_desc
        self._window = window

