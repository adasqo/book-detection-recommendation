from abc import ABC, abstractmethod

class HTMLParserStrategy:

    @abstractmethod
    def find_element(self, *args, **kwargs):
        pass