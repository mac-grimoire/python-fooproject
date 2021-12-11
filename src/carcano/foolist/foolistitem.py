__author__ = "Marco Antonio Carcano"
__version__ = '1.0.0'

import functools


@functools.total_ordering
class FoolistItem():
    """
    Object used as Item into Foolist class
    """
    _name = ""
    _enabled = False
    _next = None

    def __init__(self, name, enabled=False):
        """
        Initalize an Item assigning a name. You can optionally assign a value
        to the "enabled" boolean attribute, that defaults to False

        :param name: the name to assign to this FoolistItem Object
        :param enabled: a flag to mark this FoolistItem Object as enabled
                        or not
        """
        self._name = name
        self._enabled = enabled
        self._next = None

    def __str__(self):
        """
        Implements the representation of the Item

        :returns: pretty-print of this FoolistItem Object
        """
        return f"Name: {self._name}, Enabled: {self._enabled}"

    def __repr__(self):
        """
        Implements the representation of the Item

        :returns: an unambiguous representation of this FoolistItem Object
        """
        return f"Id: {id(self)}, Name: {self._name}, Enabled: {self._enabled}"

    @property
    def next(self):
        """
        a reference to the next Item when used into a list
        """
        return self._next

    @next.setter
    def next(self, node):
        self._next = node

    @property
    def name(self):
        """
        the name of this FoolistItem Object
        """
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def enabled(self):
        """
        wether or not this FoolistItem Object is enabled
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        self._enabled = enabled

    def __lt__(self, other):
        """
        Lower_than comparison implementation
        """
        return self.name < other.name

    def __eq__(self, other):
        """
        Equal_to comparison implementation
        """
        if other is not None:
            return (self.name) == (other.name)
        else:
            return (self.name) is None

