from docx import Document
import os

def is_In(string: str, substring: str):
    if substring in string:
        return True
    else:
        return False

def search(docx_file: str, search_strings: tuple, icrc: bool = None):
    doc = Document(docx_file)
    foundnum = 0
    human_index = 0
    for a in search_strings:
        for par in doc.paragraphs:
            if is_In(par.text, "RČ"):
                human_index += 1
            if is_In(par.text, "IČ"):
                human_index -= 1
            if is_In(par.text, a):
                foundnum += 1
                break

    if foundnum < len(search_strings):
        return False
    if icrc is None:
        return True

    if human_index > 0 and icrc:
        return True
    elif human_index < 0 and not icrc:
        return True
    else:
        return False

def main(folder: str, search_strings: str, icrc: bool = None):
    gudfiles = []

    if "\n" in search_strings:
        search_strings = search_strings.splitlines()
    else:
        search_strings = (search_strings)

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.docx'):
                f = open(str(os.path.join(root, file)), 'rb')
                try:    
                    if search(f, search_strings, icrc):
                        print(os.path.join(root, file))
                        gudfiles += [os.path.join(root, file)]
                    f.close()
                except Exception as e:
                    f.close()

    return gudfiles



if __name__ == '__main__':
    gotten = input('ic nebo rc')
    if gotten.startswith('i') or gotten.startswith('I'):
        gotten = False
    elif gotten.startswith('r') or gotten.startswith('R'):
        gotten = True
    else:
        gotten = None

    inputstr = f"{input('str1')}\n {input('str2')}\n, {input('str3')}"
    main(input("filepath"), inputstr, icrc = gotten)


            