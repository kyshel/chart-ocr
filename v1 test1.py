#!/usr/bin/env python
# -*- coding: utf-8 -*-
from util.base import *
# flow: detect > words > nlp > result

import easyocr

reader = easyocr.Reader(['ch_sim','en'], gpu = False) # need to run only once to load model into memory

# result = reader.readtext('EasyOCR-master/EasyOCR-master/examples/chinese.jpg')

filename = r"E:\ml\p9\ds\train\train_1.jpg"
print(filename)
img = cv2.imread(filename, cv2.IMREAD_COLOR)

output = cv2.resize(src, dsize)

result = reader.readtext(img_cv)

print(result)




