def animal_log(owner, name, vaccinate= 'no', birth_mark= ''): #making argument optional 
    animal = f"Owner name -{owner.upper()}\nPet name -{name.upper()}\nVaccinated -{vaccinate.upper()}\nBirthmark -{birth_mark.upper()}"
    return animal


print(animal_log(owner='sumit',name='rochak',birth_mark='patch on mouth',vaccinate='yes'))