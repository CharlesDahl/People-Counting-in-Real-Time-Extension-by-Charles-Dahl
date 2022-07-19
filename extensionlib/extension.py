#funkcija koja pretvara string u listu koaj sadrzava int-eve

def ListConvert(string):
    empty = []
    string = string.replace("[", "") 
    string = string.replace("]", "")
    string = string.replace(",", "")
    string = string.replace("\n", "")
    string = list(string.split(" "))
    if string[0] == "":
        return empty
    string = [int(j) for j in string]
    return string
