# -*- coding: utf-8 -*-
# Date: 2015/12/22
# Created by rachel chu
# Thanks http://www.waitalone.cn/python-php-ocr.html
try:
    import pytesseract
    from PIL import Image
except ImportError:
    print '模块导入错误,请使用pip安装,pytesseract依赖以下库：'
    print 'http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil'
    print 'http://code.google.com/p/tesseract-ocr/'
    raise SystemExit

image = Image.open('vcode.png')
vcode = pytesseract.image_to_string(image)
print vcode