#!/usr/bin/env python
# coding: utf-8

# In[24]:


def Kullanici_bilgileri(): #NmK
    ad_soyad = input("Adiniz ve Soyadiniz:")    
    #ad ve soyad
    while ad_soyad.isdigit():
        print("rakam Degiskeni girilmez")
        ad_soyad = input("Adiniz ve Soyadiniz:")
    else:
        print("Diger isleminiz...")
    sifre = input("Sifrenizi Giriniz:")
    #sifre degiskeni 
    while not sifre.isdigit():
        print("Sadece sayi degiskeni girilir")
        sifre = input("Sifrenizi Giriniz:")
    else:
        print("Diger isleminiz...")
    e_posta = input("E-posta adresiniz:")
    #Posta bilgileri
    while not (("@" in e_posta) and ("." in e_posta)):
        print("Yanlis eposta girdiniz!!")
        e_posta = input("E-posta adresiniz:")
    else:
        print("islem kayit edildi... \nHosgeldiniz")
#GIRIS SISTEMI BITIS


# In[22]:


Kullanici_bilgileri()


# In[ ]:




