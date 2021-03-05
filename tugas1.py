class student:
 """ A class representing a student"""
 def __init__(self,n,a,p,m,k):
    self.full_name=n
    self.age=a
    self.prodi=p
    self.NIM=m
    self.kampus=k
 def get_age(self):
    return self.age
 def get_prodi(self):
    return self.prodi
 def get_NIM(self):
     return self.NIM
 def get_kampus(self):
     return self.kampus
f = student("Fauziyah Rhaudhatul Jannah","Usia 19" ,"Sistem Telekomunikasi", "NIM 1904035", "Kampus UPI di Purwakarta")
print (f.full_name) # Access attribute "Fauziyah Rhaudhatul Jannah"
print (f.get_age()) #get attriibute "USia 19"
print (f.get_prodi()) #get attribute "Sistem Telekomunikasi"
print (f.get_NIM()) #get attribute "NIM 1904035"
print (f.get_kampus()) #get attribute "Kampus UPI di Purwakarta"