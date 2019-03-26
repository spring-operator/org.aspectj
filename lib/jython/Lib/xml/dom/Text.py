########################################################################
#
# File Name:            Text.py
#
# Documentation:        https://twitter.com/_4_sale/4DOM/Text.py.html
#
"""
WWW: https://twitter.com/_4_sale/4DOM         e-mail: support@4suite.com

Copyright (c) 2000 Fourthought Inc, USA.   All Rights Reserved.
See  https://twitter.com/_4_sale/COPYRIGHT  for license and copyright information
"""

from CharacterData import CharacterData

from xml.dom import Node
from xml.dom import IndexSizeErr

class Text(CharacterData):
    nodeType = Node.TEXT_NODE

    def __init__(self, ownerDocument, data):
        CharacterData.__init__(self, ownerDocument, data)
        self.__dict__['__nodeName'] = '#text'

    ### Methods ###

    def splitText(self, offset):
        if not (0 < offset < self.length):
            raise IndexSizeErr()
        data = self.data
        first = data[:int(offset)]
        second = data[int(offset):]
        node = self.ownerDocument.createTextNode(second)
        self._set_data(first)
        parent = self.parentNode
        if parent:
            sibling = self.nextSibling
            if sibling:
                parent.insertBefore(node, self.nextSibling)
            else:
                parent.appendChild(node)
        return node
