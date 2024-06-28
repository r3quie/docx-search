from docx import Document
import os

def search(string: str, substring: str):
    if substring in string:
        return True
    else:
        return False

def searcha(docx_file: str, search_strings: tuple):
    doc = Document(docx_file)
    foundnum = 0
    for a in search_strings:
        for par in doc.paragraphs:
            if search(par.text, a):
                foundnum += 1
    if foundnum >= len(search_strings):
        return True
    else:
        return False

def main(folder: str, search_strings: tuple):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.docx'):
                f = open(str(os.path.join(root, file)), 'rb')
                if searcha(f, search_strings):
                    print(os.path.join(root, file))
                f.close()

if __name__ == '__main__':
    main(input("filepath"), (input("str1"), input('str2'), input('str3')))


            