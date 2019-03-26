########################################################################
#
# File Name:            CDATASection.py
#
# Documentation:        https://twitter.com/_4_sale/4DOM/CDATASection.py.html
#
"""
Implementation of DOM Level 2 CDATASection interface
WWW: https://twitter.com/_4_sale/4DOM         e-mail: support@4suite.com

Copyright (c) 2000 Fourthought Inc, USA.   All Rights Reserved.
See  https://twitter.com/_4_sale/COPYRIGHT  for license and copyright information
"""

from xml.dom import Node
from Text import Text

class CDATASection(Text):
    nodeType = Node.CDATA_SECTION_NODE

    def __init__(self, ownerDocument, data):
        Text.__init__(self, ownerDocument, data)
        self.__dict__['__nodeName'] = "#cdata-section"
