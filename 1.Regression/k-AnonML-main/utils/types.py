# -*- coding: utf-8 -*-

from collections import namedtuple
from enum import Enum


class Dataset(Enum):
    CMC = 'cmc'
    MGM = 'mgm'
    ADULT = 'adult'
    CAHOUSING = 'cahousing'

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return str(other) == self.value


class AnonMethod(Enum):
    OLA = 'ola'
    MONDRIAN = 'mondrian'
    TDG = 'tdg'
    CB = 'cb'

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return str(other) == self.value


class Classifier(Enum):
    RF = 'rf'
    KNN = 'knn'
    SVM = 'svm'
    XGB = 'xgb'

    # Test
    LOG = 'log'
    LIN = 'lin'

    # Testing other regressions
    RIDGE = 'ridge'
    LASSO = 'lasso'
    def __str__(self):
        return self.value

    def __eq__(self, other):
        return str(other) == self.value

MLRes = list

MLRes2 = list

# MLRes = namedtuple("MLRes", ['score'])
# # python3.6
# MLRes.__new__.__defaults__ = (['score'],['score'])
