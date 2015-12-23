#ISSUE解决：
###1.
```javascript
Traceback (most recent call last):
  File "C:\Users\rachelc\Documents\GitHub\captcha\captcha.py", line 28, in <modu
le>
    vcode = pytesseract.image_to_string(image)
  File "C:\Python27\lib\site-packages\pytesseract\pytesseract.py", line 143, in
image_to_string
    if len(image.split()) == 4:
  File "C:\Python27\lib\site-packages\PIL\Image.py", line 1497, in split
    if self.im.bands == 1:
AttributeError: 'NoneType' object has no attribute 'bands'
Press any key to continue . . .
```

`Answer`：http://stackoverflow.com/questions/12413649/python-image-library-attributeerror-nonetype-object-has-no-attribute-xxx 

With googling I found this comment on SO, stating that PIL is sometimes 'lazy' and 'forgets' to load after opening. So you have to do it like this:
```javascript
import Image
img = Image.open('IMG_0007.jpg')
img.load()
img.split()
```

###2.
```javascript
Traceback (most recent call last):
  File "C:\Users\rachelc\Documents\GitHub\captcha\captcha.py", line 28, in <modu
le>
    vcode = pytesseract.image_to_string(image)
  File "C:\Python27\lib\site-packages\pytesseract\pytesseract.py", line 161, in
image_to_string
    config=config)
  File "C:\Python27\lib\site-packages\pytesseract\pytesseract.py", line 94, in r
un_tesseract
    stderr=subprocess.PIPE)
  File "C:\Python27\lib\subprocess.py", line 672, in __init__
    errread, errwrite)
  File "C:\Python27\lib\subprocess.py", line 882, in _execute_child
    startupinfo)
WindowsError: [Error 2] The system cannot find the file specified
Press any key to continue . . .
```

`Answer`：http://stackoverflow.com/questions/31217647/error-using-pytesser-winerror-2-the-system-cannot-find-the-file-specified

In my case, this file is located in the folder:
C:\Python27\Lib\site-packages\pytesseract\pytesseract.py

Search the following lines (for me it's line 60):
```javascript
# CHANGE THIS IF TESSERACT IS NOT IN YOUR PATH, OR IS NAMED DIFFERENTLY
tesseract_cmd = 'tesseract'
```
and change it to the location, where your pytesseract.exe is located, in my case the line looks like this:

```javascript
# CHANGE THIS IF TESSERACT IS NOT IN YOUR PATH, OR IS NAMED DIFFERENTLY
tesseract_cmd = 'C:\\Tesseract-OCR\\tesseract'
```

Now your code should work.