from docx import Document
import os

def search(docx_file: str, search_strings: tuple, icrc: bool = None) -> bool:
    doc = Document(docx_file)
    foundnum = 0
    human_index = 0
    for a in search_strings:
        for par in doc.paragraphs:
            if icrc is not None:
                if "RČ" in par.text:
                    human_index += 1
                if "IČ" in par.text:
                    human_index -= 1
            if a in par.text:
                foundnum += 1
                break

    if foundnum < len(search_strings):
        return False
    if icrc is None or icrc == None:
        return True

    if human_index > 0 and icrc:
        return True
    elif human_index < 0 and not icrc:
        return True
    else:
        return False

def main(folder: str, search_strings: str, icrc: bool = None):
    #print(search_strings + "input")
    if "\n" in search_strings:
        search_strings = search_strings.splitlines()
        print(search_strings)
    elif type(search_strings) != tuple or type(search_strings) != list:
        search_strings = (search_strings)

    for line in search_strings:
        if "" == line:
            search_strings.remove(line)
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.docx'):
                f = open(str(os.path.join(root, file)), 'rb')
                try:    
                    if search(f, search_strings, icrc):
                        yield os.path.join(root, file)
                    f.close()
                except Exception as e:
                    f.close()



if __name__ == '__main__':
    gotten = input('ic nebo rc')
    if gotten.startswith('i') or gotten.startswith('I'):
        gotten = False
    elif gotten.startswith('r') or gotten.startswith('R'):
        gotten = True
    else:
        gotten = None

    j = int(input("zadejte kolik ustanovení chcete zadat"))

    inputstr = ""
    for i in range(j):
        if i+1 == j:
            inputstr += f"{input(f'Ustanoveni {i+1}: ')}"
            continue
        inputstr += f"{input(f'Ustanoveni {i+1}: ')}\n"
    print(main(input("filepath"), inputstr, icrc = gotten))


            