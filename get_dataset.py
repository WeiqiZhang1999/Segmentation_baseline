#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/26/2022 8:13 PM
# @Author  : ZHANG WEIQI
# @File    : get_dataset.py
# @Software: PyCharm


from d2l import torch as d2l

d2l.DATA_HUB['voc2012'] = (d2l.DATA_URL + 'VOCtrainval_11-May-2012.tar',
                           '4e443f8a2eca6b1dac8a6c57641b67dd40621a49')

voc_dir = d2l.download_extract('voc2012', 'VOCdevkit/VOC2012')