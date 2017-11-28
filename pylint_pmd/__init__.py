"""PMD reporter"""
from __future__ import absolute_import, print_function

import cgi
import sys
from xml.dom import minidom
from xml.etree.ElementTree import Element, tostring

from pylint.interfaces import IReporter
from pylint.reporters import BaseReporter


class PMDReporter(BaseReporter):
    """Report messages and layouts compatible with PMD."""

    __implements__ = IReporter
    name = 'pmd'
    extension = 'xml'

    PRIORITY_MAPPING = {
        'fatal': '1',
        'error': '2',
        'warning': '3',
        'refactor': '4',
        'convention': '5',
        'info': '6',
    }

    def __init__(self, output=sys.stdout):
        BaseReporter.__init__(self, output)
        self.root_node = Element('pmd')
        self.file_nodes = {}

    def handle_message(self, msg):
        """Handle messages."""
        file_node = self._get_file_node(msg)
        violation = Element(
            'violation',
            beginline=str(msg.line),
            endline=str(msg.line),
            begincolumn=str(msg.column),
            endcolumn=str(msg.column),
            rule=msg.symbol,
            package=msg.module,
        )
        if msg.obj:
            obj = msg.obj.split('.')
            violation.set('class', obj[0])
            if len(obj) > 1:
                violation.set('method', obj[1])
        violation.set('priority', self.PRIORITY_MAPPING[msg.category])
        violation.text = cgi.escape(msg.msg or '')
        file_node.append(violation)

    def _get_file_node(self, msg):
        """Return xml node for file path."""
        if msg.path in self.file_nodes:
            file_node = self.file_nodes.get(msg.path)
        else:
            file_node = Element('file_node', name=msg.path)
            self.file_nodes[msg.path] = file_node
            self.root_node.append(file_node)
        return file_node

    def display_messages(self, layout):
        """Print messages"""
        if self.file_nodes:
            rough_string = tostring(self.root_node)
            reparsed = minidom.parseString(rough_string)
            print(reparsed.toprettyxml(indent="  "))

    def display_reports(self, layout):
        """Don't do anything"""

    def _display(self, layout):
        """Don't do anything"""

def register(linter):
    """Register Reporter"""
    linter.register_reporter(PMDReporter)
