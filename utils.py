import math, copy
import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([1.0, 2.0])
y_train = np.array([300.0,500.0])

def compute_cost(x,y,w,b):
    m = x.shape[0]
    for i in range(m):
        f_wb = w*x[i]+b
        cost = cost + (f_wb -y[i])**2
    total_cost = 1/(2*m) * cost
    return total_cost


def compute_gradient(x,y,w,b):
    m = x.shape[0]
    dj_dw = 0
    dj_db = 0
    
    for i in range(m):
        f_wb = w*x[i]+b
        dj_dw_i = (f_wb - y[i]) * x[i]
        dj_db_i = (f_wb- y[i])
        dj_dw_i += dj_dw_i
        dj_db_i += dj_db_i
    dj_dw = dj_dw/m
    dj_db = dj_db/m
    return dj_dw, dj_db