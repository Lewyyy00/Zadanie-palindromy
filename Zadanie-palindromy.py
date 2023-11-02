Words_list = [
    "kajak",
    "potop",
    "słoń",
    "anna",
    "komputer",
    "python",
    "jest",
    "super",
]

def Funkcja_sprawdzająca(Words_list):
    for i in Words_list:
        if i == i[::-1]:
            print(True)
        else:
            print(False)
    
Funkcja_sprawdzająca(Words_list)