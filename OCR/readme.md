# OCR 的研究

## First Test

- [ref](https://www.dotblogs.com.tw/RYNote/2021/01/14/105447)
- 這一篇使用的是 Tesseract
- 操作
```
python -m venv venv
pip install pillow pytesseract
```
- 到這邊下載程式並安裝: https://github.com/UB-Mannheim/tesseract/wiki
- 我是下載 tesseract-ocr-w32-setup-v5.0.0-alpha.20201127.exe 這一個版本
- 安裝程式時我是安裝在`C:\Tesseract` 而不是預設的 programs (x86) 資料夾
- 程式demo1.py如下:
```
from PIL import Image
import pytesseract

def main():
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Tesseract\\tesseract.exe'
    #指定tesseract.exe執行檔位置
    img = Image.open('image/img1.jpg') #圖片檔案位置
    text = pytesseract.image_to_string(img, lang='eng') #讀英文
    print('result: ', text)

    img = Image.open('image/img2.jpg') #圖片檔案位置
    text = pytesseract.image_to_string(img, lang='eng') #讀英文
    print('result: ', text)

    img = Image.open('image/img3.jpg') #圖片檔案位置
    text = pytesseract.image_to_string(img, lang='eng') #讀英文
    print('result: ', text)

    img = Image.open('image/img4.jpg') #圖片檔案位置
    text = pytesseract.image_to_string(img, lang='eng') #讀英文
    print('result: ', text)

if __name__ == '__main__':
    main()

```
- 結果不太好，看來是一定要有前處理才行:
```
C:\Users\Malo\Documents\py\ocr>python demo1.py
result:  AJV-1688

result:  wv.9999



result:

result:  

```
