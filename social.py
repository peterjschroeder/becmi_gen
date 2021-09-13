#!/usr/bin/python


status = {
        'Atruaghin Clans' : { 
                'Atruaghin': {
                    'common' : 'prevalent',
                    'clan chief' : 'very rare',
                },
        },
	'Norwold' : {
		'Heldanner' : {
			'very wealthy jarl': 'very rare',
			'wealthy jarl'     : 'rare',
			'wealthy karl'     : 'uncommon',
			'comfortable karl' : 'prevalent',
			'struggling karl'  : 'uncommon',
			'penniless thrall' : 'uncommon', 
		},	
		'Vatski/Vrodniki' : {
			'very wealthy Vatski boyar': 'very rare',
			'wealthy Vatski okolnichy' : 'rare',
			'wealthy Vatski freeman'   : 'uncommon',
			'comfortable Vatski freeman' : 'common',
			'struggling Vatski freeman'  : 'common',
			'penniless servant' : 'common', 
			'Vrodniki nomad' : 'prevalent',
			'Vrodniki tribal chief' : 'very rare',
		},
		'Elf' : { 'common' : 'prevalent', 'lord' : 'rare', },
	},
	'Karameikos' : {
		'Thyatian' : { 
			'penniless' : 'common',
			'struggling' : 'prevalent',
			'comfortable' : 'common',
			'wealthy' : 'uncommon',
			'wealthy and titled' : 'uncommon',
			'very wealthy' : 'very rare',
			'very wealthy and titled' : 'rare',
			'royal family' : 'very rare',
		},
		'Traladaran' : {
			'penniless' : 'prevalent',
			'struggling' : 'prevalent',
			'comfortable' : 'common',
			'wealthy' : 'rare',
			'wealthy and titled' : 'rare',
			'very wealthy' : 'very rare',
		},
		'Dwarf' : {  
			'struggling' : 'common',
			'comfortable' : 'prevalent',
			'wealthy' : 'prevalent',
			'very wealthy' : 'very rare',
			'clan head'  : 'very rare',	
		},
		'Elf' : { 'common' : 'prevalent', 'lord' : 'rare', },
		'Halfling' : { 
			'penniless' : 'uncommon',
			'struggling' : 'common',
			'comfortable' : 'prevalent',
			'wealthy' : 'very rare',
		},
	},
	'Rockhome' : {
		'Dwarf' : {
			'poor and despised' : 'prevalent',
			'struggling' : 'prevalent',
			'comfortable' : 'common',
			'wealthy' : 'uncommon',
			'wealthy and influential' : 'uncommon',
			'very wealthy and influential'  : 'rare',	
			'ruling clan head'  : 'very rare',	
		},
	},
        'Darokin' : {
                'Human' : {
                        'copper' : 'prevalent',
                        'silver': 'common',
                        'gold' : 'rare',
                        'elite' : 'very rare',
                },
                'Elf' : {
                        'copper' : 'uncommon',
                        'silver': 'prevalent',
                        'gold' : 'rare',
                        'elite' : 'very rare',
                },
               'Dwarf' : {
                        'copper' : 'common',
                        'silver': 'prevalent',
                        'gold' : 'rare',
                        'elite' : 'very rare',
                },
                'Halfling' : {
                        'copper' : 'uncommon',
                        'silver': 'prevalent',
                        'gold' : 'rare',
                        'elite' : 'very rare',
                },
        },
}
status['Norwold']['Dwarf'] = status['Karameikos']['Dwarf']
status['Rockhome']['Human'] = status['Karameikos']['Halfling']

generic_status = {
	'penniless'  : 'common',
	'struggling' : 'prevalent',
	'comfortable': 'uncommon',
	'wealthy'    : 'rare',
	'wealthy and titled' : 'rare',
	'very wealthy' : 'very rare',
	'very wealthy and titled' : 'very rare',  
}

def get_status_freq(region, race, origin):
	from config import freq
	base = generic_status
	try : base = status[region][race]
	except Exception : pass
	try : base = status[region][origin] 
	except Exception : pass
	return sum([ [i]* freq[base[i]] for i in base ], [] )

def get_status(region, race, origin):
	from random import choice
	return choice(get_status_freq(region, race, origin))

if __name__ == '__main__' :
	print ('Traladaran:', get_status('Karameikos', 'Human', 'Traladaran'))
	print ('Halfling:', get_status('Karameikos', 'Halfling', 'Clanless'))

