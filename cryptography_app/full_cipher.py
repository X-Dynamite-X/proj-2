import pandas as pan
############ ( شفرة قيصر  caesar ) ############
def en_caesar (plain_text,key):
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    cipher_list = []
    for pl in  plain_text:
        x=0
        if ord(pl) == 32:
            cipher_list.append(pl)
        for l in letters:
            if l == pl :
                cipher_key = (x+key)%26
                cipher_list.append(letters[cipher_key])
                break
            x=x+1
    cipher_text="".join(cipher_list)
    return cipher_text
def de_caesar(cipher,key):
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    plain_list = []
    for ci in  cipher:
        x=0
        if ord(ci) == 32:
            plain_list.append(ci)
        for l in letters:
            if l == ci :
                cipher_key = (x-key)%26
                plain_list.append(letters[cipher_key])
                break
            x=x+1
    plain_text="".join(plain_list)
    return plain_text
############ (شفرة الستبدال البصيط  mono alph betic ) ############ 
def en_mono_alpha_betic(plain_text):
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
    key     = ["E","Y","O","L","P","R","N","V","F","I","G","Z","Q","K","S","C","D","U","H","M","B","X","A","W","J","T"," "]
    cipher_list=[]
    for p in plain_text:
        x =0
        for l in letters:
            if  l == p:
                cipher_list.append(key[x])
            x=x+1
    cipher_text="".join(cipher_list)
    return cipher_text 
def de_mono_alpha_betic(cipher_text):
    key     = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
    letters = ["E","Y","O","L","P","R","N","V","F","I","G","Z","Q","K","S","C","D","U","H","M","B","X","A","W","J","T"," "]
    plain_list=[]
    for c in cipher_text:
        x =0
        for l in letters:
            if  l == c:
                plain_list.append(key[x])
            x=x+1
    plin_text="".join(plain_list)
    return plin_text 
############ (شفرة فحينير  vigener ) ############
def loop_key_vigener(plain_text,key):
    loop_list_key = []
    while len(plain_text) >= len(loop_list_key):
        if  len(plain_text) == len(loop_list_key):
            break
        for k in key :
            if  len(plain_text) == len(loop_list_key):
                break
            loop_list_key.append(k)
    return loop_list_key
def index_text(text):
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    ind = []
    for te in text:
        x = 0
        for le in letters:
            if le == te :
                index_text = x
                ind.append(index_text)
            x=x+1 
    return ind
def index_key(text,key):
    key_index = []
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    key = loop_key_vigener(text,key)
    for k in key : 
        x=0
        for le in letters:
            if le ==k:
                key_ind=x
                key_index.append(key_ind)
            x=x+1
    return key_index
def en_vigener(plain_text,key):
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    cipher_list=[]
    ind_key1 = index_key(plain_text,key)
    ind_text = index_text(plain_text)
    for i in range(len(ind_text)):
        cipher_ind = ((ind_text[i]+ind_key1[i])%26)
        cipher_list.append(letters[cipher_ind])
    cipher_text ="".join(cipher_list)
    return cipher_text
def de_vigener(cipher_text,key):
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    plin_list=[]
    ind_key1 = index_key(cipher_text,key)
    ind_text = index_text(cipher_text)
    for i in range(len(ind_text)):
        cipher_ind = ((ind_text[i]-ind_key1[i])%26)
        plin_list.append(letters[cipher_ind])
    plin_text ="".join(plin_list)
    return plin_text
############ (شفرة الخلطي  mixed ) ############ 
def key_list(key,letters):
    key_list = []
    for k in key:
        for le in letters:
            if le == k and k not in key_list:
                key_list.append(k)
    return key_list
def key_finesh(key,letters):
    key_list = list(key)
    for k in key_list:
        for le in letters:
            if le not in key_list:
                key_list.append(le)
    return key_list
def en_mixed(plain_text,key):
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    key_lis = key_list(key,letters)
    finesh_key = key_finesh(key_lis,letters)
    cipher_list = []
    for plain in plain_text:
        x=0
        for le in letters:
            if plain == le :
                cipher_list.append(finesh_key[x])
            x=x+1
    cipher_text="".join(cipher_list)
    return cipher_text
def de_mixed(cipher_text,key):
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    key_lis = key_list(key,letters)
    finesh_key = key_finesh(key_lis,letters)
    plain_list = []
    for cipher in cipher_text:
        x=0
        for k in finesh_key:
            if cipher == k :
                plain_list.append(letters[x])
            x=x+1
    plain_text="".join(plain_list)
    return plain_text
############ ( شفرة بيلايفير  beliver ) ############
def key_matrex(key,letters):
    key_input = []
    for k in key :
        if k == "J":
            key_input.append("I")
        else:
            key_input.append(k)
    key_list0=[]
    for k in key_input:
        for le in letters:
            if k  == le  and  le not in key_list0:
                key_list0.append(le)
    for k in key_list0:
        for le in letters:
            if le not in key_list0 :
                key_list0.append(le)
    key_list1 = []
    key_list2 = []
    key_list3 = []
    key_list4 = []
    key_list5 = []
    for i in range(0,5):
        key_list1.append(key_list0[i])
        key_list2.append(key_list0[i+5])
        key_list3.append(key_list0[i+10])
        key_list4.append(key_list0[i+15])
        key_list5.append(key_list0[i+20])
    matrex_key = pan.DataFrame([key_list1,key_list2,key_list3,key_list4,key_list5])
    print(matrex_key)
    return matrex_key
def en_beliver(plain_text,key):
    letters = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    key =key_matrex(key,letters)
    x = 0
    plain_list = []
    for i in range(len(plain_text)):
        if plain_text != plain_text[x-1]and x>0:
            plain_list.append(plain_text[x])
        elif x==0:
            plain_list.append(plain_text[x])
        else:
            plain_list.append("X")
            plain_list.append(plain_text[x])
        x=x+1
    if len(plain_list)%2 ==1:
        plain_list.append("X")
    loop=int(len(plain_list)/2)
    x = 0
    c1 = 0
    c2 = 0
    r1 = 0
    r2 = 0
    index_cipher = []
    for i in range(loop):
        for col1 in range(5):
            for row1 in range(5):
                if key[col1][row1] == plain_list[x]:
                    c1 = col1
                    r1 = row1
                    break
        for col2 in range(5):
            for row2 in range(5):
                if key[col2][row2] == plain_list[x+1]:
                    c2 = col2
                    r2 = row2
                    break
        if c1 == c2 :
            index_cipher.append(key[c1][(r1+1)%5])
            index_cipher.append(key[c2][(r2+1)%5])
        elif r1 == r2 :
            index_cipher.append(key[(c1+1)%5][r1])
            index_cipher.append(key[(c2+1)%5][r2])
        else:
            index_cipher.append(key[c2][r1])
            index_cipher.append(key[c1][r2])
        x=x+2
    cipher_text= "".join(index_cipher)
    return cipher_text
def de_beliver(cipher_text,key0):
    letters = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    key =key_matrex(key0,letters)
    x=0
    c1 = 0
    c2 = 0
    r1 = 0
    r2 = 0
    plain_list = [] 
    loop =int(len(cipher_text)/2)
    for lis_plain in range(loop):
        for col1 in  range(5):
            for row1 in range(5):
                if key[col1][row1] == cipher_text[x]:
                    c1 = col1
                    r1 = row1
                    break
        for col2 in range(5):
            for row2 in range(5):
                if key[col2][row2] == cipher_text[x+1]:
                    c2 = col2
                    r2 = row2
                    break
        if c1 == c2 :
            plain_list.append(key[c1][(r1-1)%5])
            plain_list.append(key[c2][(r2-1)%5])
            
            
        elif r1 == r2 :
            plain_list.append(key[(c1-1)%5][r1])
            plain_list.append(key[(c2-1)%5][r2])
            
            
        else :
            plain_list.append(key[c2][r1])
            plain_list.append(key[c1][r2])
        x=x+2
    plain_text="".join(plain_list)
    return plain_text



############ (الختيار من انواع التشفير و فك التشفير و انواع الشيفرات) ############ 
# def choose_1():
#     print("[1] encryption")
#     print("[2] decryption")
#     choose1 = int(input("choose encryption or decryption >> "))
#     return choose1
# def choose_2_en():
#     print("[1] caesar")
#     print("[2] mono alpha betic ")
#     print("[3] vigener")
#     print("[4] mixed")
#     print("[5] beliver")
#     print("[6] back")
#     print("[7] start ")
#     print("[0] exit")
#     choose2 = int(input("choose type encryption >> "))
#     return choose2
# def choose_2_de():
#     print("[1] caesar")
#     print("[2] mono alpha betic ")
#     print("[3] vigener")
#     print("[4] mixed")
#     print("[5] beliver")
#     print("[6] back")
#     print("[7] start ")
#     print("[0] exit")
#     choose2 = int(input("choose type decryption >> "))
#     return choose2
# ############ (الي بدء عمل البرنامج ) ############ 
# def start():
#     choose=choose_1()
#     while 1 :
#         if choose ==1:
#             choose2=choose_2_en()
#             if choose2 == 1 :
#                 while 1:
#                     plain_text = list(input("Entar to plain text: ").upper())
#                     if plain_text ==["E","X","I","T","!"]:
#                         exit()
#                     elif plain_text == ["B","A","C","E","!"]:
#                         choose_2_en()
#                         break
#                     elif plain_text == ["S","T","A","R","T","!"]: # start!
#                         start()
#                         break
#                     key = int(input("Entar to key: "))
#                     caesar = en_caesar(plain_text,key)
#                     print(caesar)
#             elif choose2 == 2 :
#                 while 1:
#                     plain_text = list(input("Entar to plin text : ").upper())
#                     if plain_text ==["E","X","I","T","!"]:
#                         exit()
#                     elif plain_text == ["B","A","C","E","!"]:
#                         choose_2_en()
#                         break
#                     elif plain_text == ["S","T","A","R","T","!"]: # start!
#                         start()
#                         break
#                     mono_alpha_betic = en_mono_alpha_betic(plain_text)
#                     print(mono_alpha_betic)
#             elif choose2 == 3:
#                 while 1:
#                     plain_text = list(input("Entar to plain text: ").upper())
#                     if plain_text ==["E","X","I","T","!"]:
#                         exit()
#                     elif plain_text == ["B","A","C","E","!"]:
#                         choose_2_en()
#                         break
#                     elif plain_text == ["S","T","A","R","T","!"]: # start!
#                         start()
#                         break
#                     key = list(input("Entar to key: ").upper())
#                     vigener = en_vigener(plain_text,key)
#                     print(vigener)
#             elif choose2 == 4:
#                 while 1 :
#                     plain_text = list(input("Entar to plain text: ").upper())
#                     if plain_text ==["E","X","I","T","!"]:
#                         exit()
#                     elif plain_text == ["B","A","C","E","!"]:
#                         choose_2_en()
#                         break
#                     elif plain_text == ["S","T","A","R","T","!"]: # start!
#                         start()
#                         break
#                     key = list(input("Entar to key: ").upper())
#                     mixed = en_mixed(plain_text,key)
#                     print(mixed)
#             elif choose2 == 5:
#                 while 1:
#                     plain_text = list(input("Entar to plain text: ").upper())
#                     if plain_text ==["E","X","I","T","!"]:
#                         exit()
#                     elif plain_text == ["B","A","C","E","!"]:
#                         choose_2_en()
#                         break
#                     elif plain_text == ["S","T","A","R","T","!"]: # start!
#                         start()
#                         break
#                     key =str(input("Entar to key: ").upper())
#                     beliver =en_beliver(plain_text,key)
#                     print(beliver)
#             elif choose2 == 6:
#                 choose_1()
#             elif choose2 == 7:
#                 start()
#             elif choose2 == 0:
#                 exit()
#         elif choose == 2:
#             choose2=choose_2_de()
#             if choose2 == 1 :
#                 while 1:
#                     cipher_text = list(input("Entar to cipher text text: ").upper())
#                     if cipher_text ==["E","X","I","T","!"]:
#                         exit()
#                     elif cipher_text == ["B","A","C","E","!"]:
#                         choose_2_en()
#                         break
#                     elif cipher_text == ["S","T","A","R","T","!"]: # start!
#                         start()
#                         break
#                     key = int(input("Entar to key: "))
#                     caesar = de_caesar(cipher_text,key)
#                     print(caesar)
#             elif choose2 == 2 :
#                 while 1:
#                     cipher_text = list(input("Entar to cipher text : ").upper())
#                     if cipher_text ==["E","X","I","T","!"]:
#                         exit()
#                     elif cipher_text == ["B","A","C","E","!"]:
#                         choose_2_en()
#                         break
#                     elif cipher_text == ["S","T","A","R","T","!"]: # start!
#                         start()
#                         break
#                     mono_alpha_betic =de_mono_alpha_betic(cipher_text)
#                     print(mono_alpha_betic)
#             elif choose2 == 3:
#                 while 1:
#                     cipher_text = list(input("Entar to cipher text: ").upper())
#                     if cipher_text ==["E","X","I","T","!"]:#exit
#                         exit()
#                     elif cipher_text == ["B","A","C","E","!"]:#bace
#                         choose_2_en()
#                         break
#                     elif cipher_text == ["S","T","A","R","T","!"]: # start!
#                         start()
#                         break                
#                     key = list(input("Entar to key: ").upper())
#                     vigener = de_vigener(cipher_text,key)
#                     print(vigener)
#             elif choose2 == 4:
#                 while 1 :
#                     cipher_text = list(input("Entar to cipher text: ").upper())
#                     if cipher_text ==["E","X","I","T","!"]:
#                         exit()
#                     elif cipher_text == ["B","A","C","E","!"]:
#                         choose_2_en()
#                         break
#                     elif cipher_text == ["S","T","A","R","T","!"]: # start!
#                         start()
#                         break
#                     key = list(input("Entar to key: ").upper())
#                     mixed = de_mixed(cipher_text,key)
#                     print(mixed)
#             elif choose2 == 5:
#                 while 1:
#                     cipher_text = list(input("Entar to cipher text : ").upper())
#                     if cipher_text ==["E","X","I","T","!"]:
#                         exit()
#                     elif cipher_text == ["B","A","C","E","!"]:
#                         choose_2_en()
#                         break
#                     elif cipher_text == ["S","T","A","R","T","!"]: # start!
#                         start()
#                         break
#                     key =str(input("Entar to key: ").upper())
#                     beliver =de_beliver(cipher_text,key)
#                     print(beliver)
#             elif choose2 == 6:
#                 choose_1()
#             elif choose2 == 7:
#                 start()
#             elif choose2 == 0:
#                 exit()
# # start()
