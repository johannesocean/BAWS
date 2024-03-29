# -*- coding: utf-8 -*-
"""
Created on 2019-05-16 15:08

@author: a002028
"""
import pandas as pd
import numpy as np


class NumpyReaderBase:
    """"""

    def __init__(self):
        """Initialize."""
        super(NumpyReaderBase, self).__init__()

    @staticmethod
    def read(*args, **kwargs):
        """"""
        return np.loadtxt(*args, **kwargs)


class PandasReaderBase:
    """"""

    def __init__(self):
        """Initialize."""
        super(PandasReaderBase, self).__init__()

    @staticmethod
    def read(*args, **kwargs):
        """"""
        return pd.read_csv(*args, **kwargs)


class NoneReaderBase:
    """Dummy base."""

    def __init__(self):
        """Initialize."""
        super(NoneReaderBase, self).__init__()

    @staticmethod
    def read(*args, **kwargs):
        """"""
        print('Warning! No shape was read due to unrecognizable datatype')


def text_reader(reader_type, *args, **kwargs):
    """"""
    if reader_type is 'pandas':
        base = PandasReaderBase
    elif reader_type is 'numpy':
        base = NumpyReaderBase
    else:
        base = NoneReaderBase

    class TextReader(base):
        """"""

        def __init__(self):
            """Initialize."""
            super(TextReader, self).__init__()

    tr = TextReader()
    return tr.read(*args, **kwargs)
