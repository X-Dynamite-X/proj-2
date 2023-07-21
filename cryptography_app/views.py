from django.shortcuts import render,redirect
from . import full_cipher as fc
# Create your views here.
def cryptography(request):
    if request.method == 'POST':
        type_crepto = request.POST['type_crepto']
        cipher_Type = request.POST['cipher_Type']
        key = request.POST['key'].upper()
        text = request.POST['text'].upper()
        if type_crepto =="encryption":
            if cipher_Type =="caesar":
                key=int(key)
                out=fc.en_caesar(text,key)
                print(out)

            # elif cipher_Type =="alpha_betic":
            #     out=fc.en_mono_alpha_betic(text,key)
            #     print(out)

            elif cipher_Type =="vigener":
                text=list(text)
                key=list(key)
                out=fc.en_vigener(text,key)
                print(out)

            elif cipher_Type =="beliver":
                text=list(text)
                key=list(key)
                out=fc.en_beliver(text,key)
                print(out)


        elif type_crepto =="decryption":
            if cipher_Type =="caesar":
                key=int(key)
                out=fc.de_caesar(text,key)
                print(out)

            elif cipher_Type =="vigener":
                text=list(text)
                key=list(key)
                out=fc.de_vigener(text,key)
                print(out)


            elif cipher_Type =="beliver":
                text=list(text)
                key=list(key)
                out=fc.de_beliver(text,key)
                print(out)
                


    # context={'out':out,'type_crepto':type_crepto}
    return render(request,"cryptography.html")
