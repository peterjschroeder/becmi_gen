#!/usr/bin/python
from random import choice, randint

if __name__ == '__main__':
    import sys
    sys.path.append("..")
from dice import d6

male_names = ['Hussein', 'Suleiman', 'Farid', 'Iyad', 'Tariq', 'Nadir', 'Hakim', 'Jibril', 'Daoud', 'Diyab', 'Aziz', 'Anwar', 'Haroun', 'Walid', 'Jamal', 'Omar',
              'Hassam', 'Khalid', 'Ahmad', 'Ali', 'Osman', 'Khaldun', 'Salman', 'Amin', 'Saleh', 'Abir', 'Asif', 'Ayub', 'Azar', 'Faris', 'Imran', 'Kabil', 'Moussa', 'Qarun', 'Samir']

female_names = ['Azizeh', 'Besma', 'Farah', 'Dunya', 'Maryam', 'Fatimah', 'Aliya', 'Radija', 'Hawa', 'Leya', 'Malika', 'Zumurrud', 'Amina',
                'Khalida', 'Majdala', 'Rahil', 'Safniya', 'Aisha', 'Amira', 'Rana', 'Habiba', 'Nina', 'Samira', 'Salma', 'Karima', 'Jasmina', 'Zaynab']

surnames = ['Awaliq', 'Dayyim', 'Awamir', 'Asir', 'Ifar', 'Ruwalah', 'Qara', 'Qahtan', 'Sulabah', 'Shammar', 'Humum', 'Dawasir', 'Yafi', 'Zahran', 'Manahil', 'Manassir', 'Wayilah', 'Katib', 'Nasir', 'Kalim', 'Jaboor', 'Rashid', 'Bakr',
            'Abbas', 'Anwar', 'Hisan', 'Hakim', 'Muzdahir', 'Namur', 'Tajir', 'Jaboori', 'Cubiani', 'Abbashani', 'Sulbani', 'Jamal', 'Bahar', 'Muharib', 'Muqatil', 'Khiat', 'Parsani', 'Anrami', 'Warqani', 'Uruki', 'Hedjazani', 'Kebiri', 'Fabiani']

immortals = ['Malik', 'Rahman', 'Zephyr',
             'Abu Diba', 'Khabir min al-Bahr', 'Asnam', 'Din']


def get_name(gender):
    res = '' if d6() < 6 else 'Abu ' if gender == 'm' else 'Umm '
    if d6() == 1:
        res += 'Abd al-' if gender == 'm' else 'Amat al-'
        res += choice(immortals)
    else:
        res += choice(male_names) if gender == 'm' else choice(female_names)
    if d6() < 3:
        res += ' al '+choice(surnames)
    else:
        res += ' bint' if gender == 'f' else choice(
            [' ibn', ' ibn', ' ben', ' bin'])
        res += ' '+choice(male_names)
        if d6() < 3:
            res += ' al '+choice(surnames)
    return res


if __name__ == '__main__':
    from sys import argv
    gender = choice(['m', 'f'])
    if len(argv) > 1:
        if argv[1] in ['male', 'm', '-m']:
            gender = 'm'
        if argv[1] in ['female', 'f', '-f']:
            gender = 'f'
    print (get_name(gender))
