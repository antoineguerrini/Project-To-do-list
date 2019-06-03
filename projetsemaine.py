#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 10:47:23 2019

@author: antoineguerrini
"""

#projet semaine 1
import pandas as pd
data = pd.read_csv('to-do.csv')    
data = {} 

def read():
    read_task = input("Voulez-vous lire vos tasks ? Oui / Non")
    if read_task == "Oui":
        for value in data.values():
            print(value)
    else:
        print ("Okay")
       
def tasking():
    numero_task = 1
    ajouter = input("Voulez-vous ajouter une task ? Oui / Non")
    while ajouter == "Oui":
        data[numero_task] = input("quelles tasks ajouter ?")
        ajouter = input("Voulez-vous ajouter une task ? Oui / Non")
        numero_task += 1
    else:
        print("Okay")
        read()  
        
def delete():
    del_task = input("Voulez-vous supprimer des tasks ? Oui / Non")
    while del_task == "Oui":
        nb_task = int(input ("Quel numéro de task voulez-vous supprimer ?"))
        del(data[nb_task])
        del_task = input("Voulez-vous supprimer des autres tasks ? Oui / Non")
    else:
        read() 
        
tasking()  
delete()


data = pd.DataFrame({"task":["dodo", "manger"]})
data.to_csv('to-do-listing.csv')

### Dry version

pd.DataFrame({"Col_1": tasking()})
        
        









