# -*- coding: utf-8 -*-
# Date: 2015/12/22
# Created by rachel chu
# Thanks http://www.waitalone.cn/python-php-ocr.html
import os,sys
try:
    import pytesseract
    from PIL import Image
except ImportError:
    print '模块导入错误,请使用pip安装,pytesseract依赖以下库：'
    print 'http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil'
    print 'http://code.google.com/p/tesseract-ocr/'
    raise SystemExit
    
def cur_file_dir():
     #获取脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)

imagepath = cur_file_dir() + "\image\captcha1.jpg"
print imagepath
image = Image.open(imagepath)
image.load()
image.split()
vcode = pytesseract.image_to_string(image)
print vcode