#!/usr/bin/python
from random import choice, randint

if __name__=='__main__' :
	import sys
	sys.path.append("..")
from dice import d6

male_names = [ 'Zweis', 'Kyrill', 'Ilya', 'Fyodor', 'Klas', 'Cartha', 'Pieter', 'Mikel', 'Zogrev', 'Grygory', 'Lucas', 'Mikhail', 'Irenak', 'Janek', 'Poros', 'Antonito', 'Theodosius', 'Mytia', 'Christoph', 'Simion', 'Marek', 'Vasil', 'Petr', 'Iajo', 'Stephanos', 'Zemiros', 'Emil', 'Lev', 'Aleksei', 'Boris', 'Yuri', 'Feodor', 'Aleksander', 'Sergei', 'Vassili', 'Arkadi', 'Grigori', 'Dimitri', 'Valdo', 'Anton', 'Pavel', 'Ivan', 'Kristof', 'Andrei', 'Pyotr', 'Stefan', 'Ioan', 'Gheorge', 'Rodoz', 'Stavros', 'Jorgos', 'Andros', 'Nikolai', 'Vlad', 'Yakov' ]  

female_names = [ 'Darya', 'Ilyana', 'Kuzma', 'Ksenia', 'Anya', 'Rebeca', 'Irena', 'Ordana', 'Gloria', 'Avdotya', 'Veronika', 'Kresimira', 'Nichola', 'Vesna', 'Akatrina', 'Katerina', 'Laina', 'Anastasia', 'Natalya', 'Oksana', 'Magda', 'Alya', 'Roksana', 'Ioana', 'Irina', 'Ivana', 'Yolanda', 'Arkadia', 'Sula', 'Zandra' ] 

surnames_front = [ 'Dmitr', 'Azur', 'Toren', 'Lut', 'Yar', 'Sul', 'Aleks', 'Feodor', 'Grigor', 'Yur', 'Vasil', 'Gheorgh', 'Iren', 'Anton', 'Rad', 'Pop', 'Sim', 'Andr', 'Petr', 'Rod', 'Nikel', 'Vlad', 'Serg', 'Jorg', 'Mar', 'Pavl', 'Nikol', 'Our', 'Stavr', 'Aleksandr', 'Theod' ]
surnames_middle = [ 'an', 'i', 'ian' ]
surnames_back = [ 'os', 'escu', 'ov', 'ovich', 'ev' ]


def get_name(gender):
	res = choice(male_names) if gender=='m' else choice(female_names)
	res+=' '+choice(surnames_front)+ (choice(surnames_middle) if d6()<3 else '')  +choice(surnames_back)
	return res

if __name__ == '__main__' :
   from sys import argv
   gender='m'
   if len(argv)>1 :
      if argv[1] in ['male', 'm', '-m'] : gender='m'
      if argv[1] in ['female', 'f', '-f'] : gender='f'
   res=get_name(gender)	 
   print (res)
