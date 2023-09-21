from django.shortcuts import render, redirect
from . import full_cipher as fc  # استيراد ملف full_cipher.py

def cryptography(request):
    outtext = ""
    type_crept = ""
    
    if request.method == 'POST':
        type_crepto = request.POST['type_crepto']
        type_crept = type_crepto
        cipher_Type = request.POST['cipher_Type']
        key = request.POST['key'].upper()
        text = request.POST['text'].upper()
        
        if type_crepto == "encryption":
            if cipher_Type == "caesar":
                key = int(key)
                out = fc.en_caesar(text, key)  # تشفير كيسار
                outtext = out
            elif cipher_Type == "vigener":
                text = list(text)
                key = list(key)
                out = fc.en_vigener(text, key)  # تشفير فيجينير
                outtext = out
            elif cipher_Type == "beliver":
                text = list(text)
                key = list(key)
                out = fc.en_beliver(text, key)  # تشفير بيليفر
                outtext = out
            elif cipher_Type == "morse":
                text = list(text)
                out = fc.en_morse(text)  # تشفير مورس
                outtext = out
        elif type_crepto == "decryption":
            if cipher_Type == "caesar":
                key = int(key)
                out = fc.de_caesar(text, key)  # فك تشفير كيسار
                outtext = out
            elif cipher_Type == "vigener":
                text = list(text)
                key = list(key)
                out = fc.de_vigener(text, key)  # فك تشفير فيجينير
                outtext = out
            elif cipher_Type == "morse":
                out = fc.de_morse(text)  # فك تشفير مورس
                outtext = out
            elif cipher_Type == "beliver":
                text = list(text)
                key = list(key)
                out = fc.de_beliver(text, key)  # فك تشفير بيليفر
                outtext = out
    
    context = {'outtext': outtext, 'type_crept': type_crept}
    return render(request, "cryptography.html", context)  # إعادة عرض صفحة cryptography.html مع النص المشفر/المفكوك ونوع العملية
