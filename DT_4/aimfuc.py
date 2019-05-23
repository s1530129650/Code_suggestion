# -*- coding: utf-8 -*-
"""
aimfc.py - 目标函数demo
描述:
    Geatpy的目标函数遵循本案例的定义方法，传入种群表现型矩阵Phen，以及可行性列向量LegV
    若没有约束条件，也需要返回LegV
    若要改变目标函数的输入参数、输出参数的格式，则需要修改或自定义算法模板
"""

import numpy as np

def aimfuc(Phen, LegV):
    x1 = Phen

    f = 18 * x1
    
    return [f, LegV]
