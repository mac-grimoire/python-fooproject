__author__ = "Marco Antonio Carcano"
__version__ = '1.0.0'

from .foolistitem import FoolistItem

import logging
"""
initialize logger to NullHandler
"""
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


class Foolist():
    """
    Object used to implement a list of FoolistItem
    """
    _unique = False

    def __init__(self):
        """
        Initialize the list by setting its head to None
        """
        self.head = None
        self._unique = False

    @property
    def unique(self):
        """
        if true, set the list so to contain only unique items
        """
        return self._unique

    @unique.setter
    def unique(self, isunique):
        log.debug('Package: '+__name__+', setting unique='+str(isunique))
        self._unique = isunique

    def __iter__(self):
        """
        Iterate throughout the list
        """
        node = self.head
        while node is not None:
            yield node
            node = node._next
        raise StopIteration

    def append(self, name, enabled=False):
        """
        Append a FoolistItem to the list

        :param name: the name to assign to the FoolistItem
        :param enabled: a flag to mark it as enabled or not
        """
        log.debug('Package: ' + __name__ +
                ',Method: append, Params: name="' + name +
                '", enabled: ' + str(enabled))
        if self.head is None:
            self.head = FoolistItem(name, enabled)
            return
        if self._unique is True:
            tmp_node = FoolistItem(name, enabled)
        for current_node in self:
            if self._unique is True and current_node == tmp_node:
                log.debug('Package: ' + __name__ +
                        ',Method: append, Msg: skipping since FoolistItem is already present')
                return
            pass
        current_node.next = FoolistItem(name, enabled)

    def remove(self, name):
        """
        Removes an item from the list

        :param name: the name of the FoolistItem to remove
        """
        log.debug('Package: '+__name__+', Method: remove, Params: name="'+name)
        for f in self:
            if f.name == name:
                if f == self.head:
                    self.head = f._next
                else:
                    hold._next = f._next
                del f
                break
            else:
                hold = f

    def __str__(self):
        """
        Implements the representation of the list
        """
        nodes = []
        for node in self:
            nodes.append(str(node))
        return str(nodes)


    def __repr__(self):
        """
        Implements the representation of the list
        """
        nodes = []
        for node in self:
            nodes.append(repr(node))
        return str(nodes)        
