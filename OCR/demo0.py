from PIL import Image
import pytesseract

def main():
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Tesseract\\tesseract.exe'
    #指定tesseract.exe執行檔位置
    img = Image.open('image/img2.jpg') #圖片檔案位置
    text = pytesseract.image_to_string(img, lang='eng') #讀英文
    #text = pytesseract.image_to_string(img, lang='chi_sim') #簡體中文
    #text = pytesseract.image_to_string(img, lang='chi_tra') #繁體中文
    print('result: ', text)

if __name__ == '__main__':
    main()

