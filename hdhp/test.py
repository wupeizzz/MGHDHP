"""
    generative_model
    ~~~~~~~~~~~~~~~~~

    Provides the following generative model:
    :class:`generative_model.HDHProcess`
      Implements the generative model of a hierarchical
      Dirichlet-Hawkes process.

    :copyright: 2016 Charalampos Mavroforakis, <cmav@bu.edu> and contributors.
    :license: ISC
"""


import datetime

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from numpy import log as ln
from numpy import asfortranarray, exp
from numpy.random import RandomState
from scipy.misc import logsumexp
from sklearn.utils import check_random_state

for i in [1,2,3,4]:
	rng = np.random.RandomState(23455)
	arrayA = rng.uniform(0,1,(2,3))
	arrayA1 = rng.uniform(0,1,(2,3))
	print (arrayA,arrayA1)