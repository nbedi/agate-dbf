#!/usr/bin/env python

"""
This module contains the DBF extension to :class:`Table <agate.table.Table>`.
"""

import agate
from dbfread import DBF

def recfactory(items):
    return tuple(kv[1] for kv in items)

class TableDBF(object):
    @classmethod
    def from_dbf(cls, path, encoding=None):
        """
        Parse a DBF file.

        :param path:
            Path to an DBF file to load or a file-like object for one.
        """
        dbf = DBF(path, load=True, lowernames=True, encoding=encoding, recfactory=recfactory)
        table = agate.Table(dbf.records, column_names=dbf.field_names)

        return table