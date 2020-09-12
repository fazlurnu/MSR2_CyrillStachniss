# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 21:32:46 2020

@author: Muhammad Fazlur Rahman
"""

def icp(q, p):
    """
        [TR, TT] = icp(q,p)   returns the rotation matrix TR and translation
        vector TT that minimizes the distances from (TR * p + TT) to q.
        p is a 3xm matrix and q is a 3xn matrix.
    """
    
    