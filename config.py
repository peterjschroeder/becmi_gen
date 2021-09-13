#!/usr/bin/python

__doc__ = """Configuration of the BECMI NPC generator

This file contains setups for the NPC generator. Modify the following structures to
change the frequencies of each possible choice.

freq		            Controls the relative frequencies of character classes, races, etc. 
                    By default, rare is twice as common as very rare, etc.

classes_by_origin   Defines, for each character origin (e.g., Thyatian or Mountain Rakasta),
                    the relative frequencies of the different character classes.
										A class can be entirely absent.
race_by_region      Defines for each available region (e.g., Norwold, Thyatis, Alphatia),
										the relative frequencies of the different races (Humans, Dwarves, Elves, 
										Halflings, Rakasta, and Lupins).
ethnic_by_region		Defines, for each region and for each race, which breeds or ethnic groups
										are present, and with which frequency.
align_by_origin			Defines, for each character origin, the frequency of the three alignments.

regions							Defines the available regions
"""

exponential_freq = {
	'prevalent' : 16,
	'common'    : 8,
	'uncommon'  : 4,
	'rare'      : 2,
	'very rare' : 1,
}

default_freq = {
	'prevalent' : 6,
	'common'    : 4,
	'uncommon'  : 3,
	'rare'      : 2,
	'very rare' : 1,
}

variant_freq = {
	'prevalent' : 8,
	'common'    : 4,
	'uncommon'  : 3,
	'rare'      : 2,
	'very rare' : 1,
}

quadratic_freq = {
	'very rare' : 1,
	'rare'      : 4,
	'uncommon'  : 9,
	'common'    : 16,
	'prevalent' : 25, 
}

linear_freq = {
	'very rare' : 1,
	'rare'      : 2,
	'uncommon'  : 4,
	'common'    : 6,
	'prevalent' : 8,
}


freq=default_freq

regions=['Norwold', 'Thyatis', 'Alphatia', 'Isle of Dawn', 'Ylaruam', 'Karameikos', 'Glantri', 'Rockhome', 'Savage Coast', 'Ethengar Khanate', 'Darokin', 'Hule', 'Alfheim', 'Ierendi', 'Atruaghin Clans', 'Shimmering Lands' ]

abilities = ['str', 'int', 'wis', 'dex', 'con', 'cha' ]
hclasses = [ 'Shamani', 'Dervish', 'Horse Warrior', 'Bratak', 'Hakomon', 'Fighter', 'Cleric', 'Shaman', 'Thief', 'Bard', 'Rake', 'Magic User', 'Mystic', 'Druid', 'Forester' ]
classes = { 
 'Human' : hclasses,
 'Lupin' : hclasses,
 'Rakasta' : hclasses,
 'Dwarf' : [ 'Dwarf', 'Dwarf Cleric' ],
 'Elf' : ['Elf'],
 'Halfling' : ['Halfling']
}

primary_scores = {
	'Fighter' : ['str'],
	'Magic User' : ['int'],
	'Cleric' : ['wis'],
	'Thief' : ['dex'],
	'Dwarf' : ['str'],
	'Elf' : ['str','int'],
	'Halfling' : ['str'],
	'Forester' : ['str', 'int'],
	'Druid' : ['wis'],
	'Shaman' :['wis'],
	'Shamani' :['wis', 'con'],
	'Hakomon' : [ 'int' ],
	'Bard' : ['dex'],
	'Rake' : ['dex'],
	'Mystic' : ['str'],
	'Dwarf Cleric' : [ 'str', 'wis'],
	'Horse Warrior' : [ 'str' ],
	'Bratak' : [ 'dex' ],
        'Dervish' : ['wis'],
}

classes_by_origin = {
        'Atruaghin' : {
                'Fighter' : 'prevalent',
                'Thief'   : 'common',
                'Cleric'  : 'uncommon',
                'Druid'   : 'uncommon',
                'Shamani' : 'uncommon',
                'Magic User' : 'very rare',
            },
        'Hulean' : {
                'Fighter' : 'common',
                'Thief' : 'common',
                'Cleric' : 'common',
                'Magic User' : 'rare',
                'Druid'  : 'rare',
                'Shaman' : 'very rare',
                'Mystic' : 'very rare',
        },
	'Alphatian' : {
		'Fighter' : 'common', 
		'Cleric'  : 'rare', 
		'Thief'   : 'very rare', 
		'Rake'    : 'very rare', 
		'Magic User' : 'uncommon', 
		'Mystic'  : 'very rare', 
		'Druid'   : 'rare',
	},
	'Thothian' : {
		'Fighter' : 'common', 
		'Cleric'  : 'uncommon', 
		'Thief'   : 'uncommon', 
		'Rake'    : 'very rare', 
		'Magic User' : 'uncommon', 
		'Mystic'  : 'very rare', 
		'Druid'   : 'rare',
	},
	'Thyatian' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'common', 
		'Thief'   : 'common', 
		'Bard'    : 'rare', 
		'Rake'    : 'uncommon', 
		'Magic User' : 'common', 
		'Mystic'  : 'uncommon', 
		'Druid'   : 'very rare',
		'Forester': 'common',
		'Shaman'  : 'very rare',
	},
	'Verdan' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'uncommon', 
		'Thief'   : 'common', 
		'Bard'    : 'very rare', 
		'Rake'    : 'prevalent', 
		'Magic User' : 'uncommon', 
		'Mystic'  : 'very rare', 
		'Druid'   : 'very rare',
	},
	'Ispan' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'common', 
		'Thief'   : 'common', 
		'Bard'    : 'very rare', 
		'Rake'    : 'prevalent', 
		'Magic User' : 'uncommon', 
		'Mystic'  : 'very rare', 
		'Druid'   : 'very rare',
	},
	'Traladaran' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'common', 
		'Thief'   : 'common', 
		'Bard'    : 'uncommon', 
		'Rake'    : 'very rare', 
		'Magic User' : 'uncommon', 
		'Druid'   : 'rare',
	},
	'Heldanner' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'common', 
		'Thief'   : 'uncommon', 
		'Bard'    : 'uncommon', 
		'Rake'    : 'very rare', 
		'Magic User' : 'uncommon', 
		'Druid'   : 'common',
	},
	'Heldannic' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'common', 
		'Thief'   : 'uncommon', 
		'Bard'    : 'rare', 
		'Rake'    : 'very rare', 
		'Magic User' : 'uncommon', 
		'Druid'   : 'rare',
		'Forester': 'very rare',
	},
	'Alasiyan' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'common', 
		'Thief'   : 'uncommon', 
		'Rake'    : 'uncommon', 
		'Magic User' : 'common', 
		'Druid'   : 'very rare',
                'Dervish' : 'uncommon',
	},
	'Ethengar' : {
		'Bratak'   : 'uncommon',
		'Horse Warrior' : 'prevalent',
		'Cleric'  : 'uncommon',
		'Shaman'  : 'uncommon',
		'Hakomon' : 'rare',
	},
	'Ochalean' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'common', 
		'Thief'   : 'uncommon', 
		'Rake'    : 'uncommon', 
		'Magic User' : 'uncommon', 
		'Druid'   : 'uncommon',
		'Shaman'  : 'uncommon',
		'Mystic'  : 'prevalent',
		'Forester': 'rare',
		'Bard'    : 'very rare',
	},
	'Dunael' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'common', 
		'Thief'   : 'uncommon', 
		'Bard'    : 'common', 
		'Rake'    : 'rare', 
		'Magic User' : 'uncommon', 
		'Druid'   : 'common',
		'Mystic'  : 'very rare',
	},
	'Vatski/Vrodniki' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'common', 
		'Thief'   : 'uncommon', 
		'Bard'    : 'uncommon', 
		'Shaman'  : 'uncommon', 
		'Magic User' : 'rare', 
		'Druid'   : 'uncommon',
	},
	'Flaem' : {
		'Fighter' : 'prevalent',
		'Cleric'  : 'very rare',
		'Magic User' : 'common',
		'Thief'   : 'uncommon',
		'Rake'    : 'common',
		'Mystic'  : 'rare', 
	},
	'Averoignese' : {
		'Fighter' : 'prevalent',
		'Cleric'  : 'very rare',
		'Magic User' : 'common',
		'Thief'   : 'common',
		'Rake'    : 'common',
		'Mystic'  : 'very rare', 
	},
        'Daro': {
                'Fighter' : 'prevalent',
                'Thief'   : 'common',
                'Rake'    : 'common',
                'Cleric'  : 'common',
                'Magic User' : 'rare',
                'Bard'    : 'very rare',
                'Druid'   : 'very rare',
        },
        'Ierendian' : {
                'Fighter' : 'prevalent',
                'Cleric'  : 'uncommon',
                'Thief'   : 'common',
                'Rake'    : 'uncommon',
                'Magic User' : 'uncommon',
                'Druid'   : 'rare',
        },
        'Makai' : {
                'Fighter' : 'prevalent',
                'Shaman'  : 'uncommon',
                'Thief'   : 'uncommon',
                'Druid'   : 'uncommon',
                'Magic User' : 'very rare',
                'Cleric'  : 'very rare',
        },
	'Dwarf' : {
		'Dwarf'   : 'prevalent',
		'Dwarf Cleric' : 'uncommon',
	},
	'Elf' : { 'Elf' : 'prevalent' },
	'Halfling' : { 'Halfling' : 'prevalent' },
	'Mountain Rakasta' : {
		'Fighter' : 'prevalent', 
		'Thief'   : 'uncommon', 
		'Bard'    : 'rare', 
		'Shaman'  : 'common', 
		'Magic User' : 'uncommon', 
		'Druid'   : 'uncommon',		
	},
	'Bellaynish' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'uncommon', 
		'Thief'   : 'common', 
		'Bard'    : 'rare', 
		'Rake'    : 'common', 
		'Magic User' : 'uncommon', 
		'Druid'   : 'uncommon',
	},
	'Doggerman' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'uncommon',
		'Thief'   : 'rare', 
		'Rake'    : 'rare', 
		'Magic User' : 'uncommon', 
		'Druid'   : 'uncommon',		
		'Forester': 'common',
	},
	'Mongrel Lupin' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'common',
		'Thief'   : 'uncommon', 
		'Rake'    : 'uncommon', 
		'Bard'    : 'rare', 
		'Magic User' : 'uncommon', 
		'Druid'   : 'uncommon',	
		'Forester': 'common',
	},
	'Heldann Shepherd' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'common',
		'Thief'   : 'uncommon', 
		'Bard'    : 'rare', 
		'Magic User' : 'rare', 
		'Druid'   : 'uncommon',	
		'Shaman'  : 'very rare',
	},
	'Foxfolk' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'uncommon',
		'Thief'   : 'uncommon', 
		'Bard'    : 'uncommon', 
		'Magic User' : 'rare', 
		'Druid'   : 'common',	
		'Shaman'  : 'very rare',
		'Forester': 'rare',
	},
	'Shar-Pei' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'uncommon',
		'Thief'   : 'rare', 
		'Magic User' : 'rare', 
		'Druid'   : 'rare',	
		'Shaman'  : 'very rare',
		'Forester': 'uncommon',
		'Mystic'  : 'common',
	},
	'Ochalean Houndling' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'common',
		'Thief'   : 'common', 
		'Rake'    : 'uncommon', 
		'Magic User' : 'uncommon', 
		'Druid'   : 'uncommon',	
		'Shaman'  : 'rare',
		'Forester': 'rare',
	},
	'Ochalean Crested' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'common',
		'Thief'   : 'uncommon', 
		'Rake'    : 'uncommon', 
		'Magic User' : 'common', 
		'Druid'   : 'uncommon',	
		'Shaman'  : 'uncommon',
		'Forester': 'rare',
	},
	'Nithian Rambler' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'common',
		'Thief'   : 'common', 
		'Rake'    : 'uncommon', 
		'Magic User' : 'uncommon', 
		'Druid'   : 'very rare',
                'Dervish' : 'uncommon',
	},
	'Fennec' : {
		'Fighter' : 'common', 
		'Cleric'  : 'uncommon',
		'Thief'   : 'common', 
		'Rake'    : 'common', 
		'Bard'    : 'uncommon',
		'Magic User' : 'uncommon', 
		'Druid'   : 'rare',
                'Dervish' : 'uncommon',
	},
	'Mastiff' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'uncommon',
		'Thief'   : 'rare', 
		'Rake'    : 'rare', 
		'Bard'    : 'very rare',
		'Magic User' : 'rare', 
		'Druid'   : 'very rare',
		'Mystic'  : 'common',
		'Forester': 'uncommon',
	},
	'Beagle' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'common',
		'Thief'   : 'common', 
		'Rake'    : 'uncommon', 
		'Magic User' : 'uncommon', 
		'Druid'   : 'very rare',	
		'Bard'    : 'rare',
		'Forester': 'rare',
	},
	'Renardois Folk' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'common',
		'Thief'   : 'uncommon', 
		'Rake'    : 'common', 
		'Bard'    : 'rare', 
		'Magic User' : 'uncommon', 
		'Druid'   : 'rare',	
	},
	'Narvaezan Maremma' : {
		'Fighter' : 'prevalent', 
		'Cleric'  : 'common',
		'Thief'   : 'uncommon', 
		'Rake'    : 'uncommon', 
		'Bard'    : 'rare', 
		'Magic User' : 'rare', 
		'Druid'   : 'rare',	
	},
	'Moadreg' : {
		'Dwarf'   : 'prevalent',
		'Dwarf Cleric' : 'uncommon',
	},
}
classes_by_origin['Chow Chow']=classes_by_origin['Shar-Pei']
classes_by_origin['Das Hund']=classes_by_origin['Fennec']
classes_by_origin['Snoutzer']=classes_by_origin['Heldann Shepherd']
classes_by_origin['Pardasta']=classes_by_origin['Mountain Rakasta']
classes_by_origin['Klantyrian']=classes_by_origin['Flaem']
classes_by_origin['Bouchon']=classes_by_origin['Beagle']
classes_by_origin['Carrasquito']=classes_by_origin['Fennec']
classes_by_origin['Papillon']=classes_by_origin['Fennec']
classes_by_origin['Slagovici Gonic']=classes_by_origin['Beagle']
classes_by_origin['Zvornikian Sentinel']=classes_by_origin['Narvaezan Maremma']
classes_by_origin['Eusdrian']=classes_by_origin['Heldanner']
classes_by_origin['Caurenzan']=classes_by_origin['Thyatian']

races_by_region = {
        'Atruaghin Clans' : { 'Human' : 'prevalent' },
        'Hule' : {
                'Human' : 'prevalent',
        },
	'Savage Coast' : { 
		'Human' : 'prevalent', 
		'Dwarf' : 'uncommon', 
		'Elf'   : 'uncommon', 
		'Halfling' : 'rare', 
		'Lupin' : 'common', 
		'Rakasta' : 'uncommon', 
	},
	'Norwold' : { 
		'Human' : 'prevalent', 
		'Dwarf' : 'uncommon', 
		'Elf'   : 'uncommon', 
		'Halfling' : 'uncommon', 
		'Lupin' : 'common', 
		'Rakasta' : 'uncommon', 
	},
	'Thyatis' : { 
		'Human' : 'prevalent', 
		'Dwarf' : 'uncommon', 
		'Elf'   : 'uncommon', 
		'Lupin' : 'uncommon', 
		'Rakasta' : 'rare',
		'Halfling': 'very rare', 
	},
	'Karameikos' : { 
		'Human' : 'prevalent', 
		'Dwarf' : 'uncommon', 
		'Elf'   : 'uncommon', 
		'Halfling' : 'rare', 
	},
	'Ylaruam' : { 
		'Human' : 'prevalent', 
		'Dwarf' : 'rare', 
		'Lupin' : 'uncommon', 
	},
	'Alphatia' : { 
		'Human' : 'prevalent', 
		'Dwarf' : 'uncommon', 
		'Elf'   : 'uncommon', 
		'Halfling' : 'uncommon', 
	},
	'Isle of Dawn' : { 
		'Human' : 'prevalent', 
		'Elf'   : 'very rare', 
		'Rakasta' : 'very rare', 
	},
	'Glantri' : { 
		'Human' : 'prevalent', 
		'Elf'   : 'common', 
		'Lupin' : 'common', 
		'Rakasta' : 'rare', 
	},
	'Ethengar Khanate' : {
		'Human' : 'prevalent',
		'Dwarf' : 'uncommon',
	},
	'Rockhome' : {
		'Dwarf' : 'prevalent',
		'Human' : 'rare',
	},
        'Darokin' : {
                'Human' : 'prevalent',
                'Elf'  : 'rare',
                'Dwarf' : 'uncommon',
                'Halfling' : 'rare',
                'Lupin' : 'very rare',
        },
        'Alfheim' : {
                'Elf' : 'prevalent',
                'Human' : 'rare',
        },
        'Ierendi' : {
                'Human' : 'prevalent',
                'Elf' : 'uncommon',
                'Halfling' : 'uncommon',
        },
	'Shimmering Lands' : {
		'Dwarf' : 'prevalent',
	},
}

ethnic_by_region = {
        'Atruaghin Clans' : { 'Human' : { 'Atruaghin' : 'prevalent' }, },
        'Hule' : {
                'Human' : {
                        'Hulean' : 'prevalent',
                        'Traladaran' : 'rare',
                },    
        },
	'Rockhome' : {
		'Dwarf' : { 'Denwarf' : 'prevalent' },
		'Human' : { 
			'Ethengar' : 'common',
			'Alasiyan' : 'common',
			'Thyatian' : 'uncommon',
			'Heldanner': 'common',
			'Traladaran' : 'rare',
		},
	},
	'Savage Coast' : { 
		'Human' : {
			'Ispan' : 'prevalent',
			'Verdan' : 'common',
			'Traladaran' : 'uncommon',
			'Dunael' : 'uncommon',
			'Eusdrian' : 'uncommon',
		}, 
		'Dwarf' : { 'Montoya' : 'prevalent', 'Eusdrian' : 'uncommon' },
		'Elf'   : { 'Belcadiz' : 'prevalent', 'Eusdrian' : 'uncommon' },
		'Halfling' : { 'Eusdrian' : 'prevalent', 'Bellaynish' : 'uncommon' },
		'Lupin' : { 
			'Foxfolk' : 'uncommon', 
			'Renardois Folk' : 'prevalent' ,
			'Narvaezan Maremma' : 'uncommon',
			'Bouchon' : 'uncommon', 
			'Carrasquito' : 'uncommon', 
			'Papillon' : 'uncommon', 
			'Slagovici Gonic' : 'uncommon', 
			'Zvornikian Sentinel' : 'uncommon', 
		},
		'Rakasta' :  { 'Bellaynish' : 'prevalent', }, 
	},
	'Norwold' : { 
		'Human' : {
			'Heldanner' : 'prevalent',
			'Vatski/Vrodniki' : 'common',
			'Alphatian' : 'uncommon',
			'Thyatian' : 'uncommon',
			'Dunael' : 'rare',
			'Heldannic' : 'rare',
		}, 
		'Dwarf' : { 'Denwarf' : 'prevalent', },
		'Elf'   : { 'Shiye' : 'prevalent', },
		'Halfling' : { 'Leeha' : 'prevalent', },
		'Lupin' : { 
			'Foxfolk' : 'prevalent', 
			'Heldann Shepherd' : 'prevalent' ,
			'Snoutzer' : 'uncommon',
		},
		'Rakasta' :  { 'Mountain Rakasta' : 'prevalent', }, 
	},
	'Thyatis' : { 
		'Human' : {
			'Thyatian' : 'prevalent',
			'Heldannic' : 'common',
			'Caurenzan' : 'uncommon',
			'Dunael' : 'uncommon',
			'Heldanner' : 'rare',
			'Ochalean' : 'uncommon',
			'Alasiyan' : 'rare',
		}, 
		'Dwarf' : { 'Denwarf' : 'prevalent', },
		'Elf'   : { 'Vyalia' : 'prevalent', },
		'Lupin' : { 
			'Mongrel Lupin' : 'prevalent', 
			'Doggerman' : 'common', 
			'Mastiff' : 'common', 
			'Beagle' : 'common', 
			'Ochalean Crested' : 'common', 
			'Ochalean Houndling' : 'common', 
			'Shar-Pei' : 'common' ,
			'Chow Chow': 'common' ,
			'Das Hund' : 'common' ,
		},
		'Rakasta' :  { 'Pardasta' : 'prevalent', }, 
		'Halfling': { 'Thyatian' : 'prevalent', },
	},
	'Ylaruam' : { 
		'Human' : { 'Alasiyan' : 'prevalent', }, 
		'Dwarf' : { 'Denwarf' : 'prevalent', },
		'Lupin' : { 
			'Fennec' : 'common',
			'Nithian Rambler' : 'common' ,
		},
	},
	'Ethengar Khanate' : {
		'Human' : { 'Ethengar' : 'prevalent', },
		'Dwarf' : { 'Denwarf' : 'prevalent', },
	},
	'Karameikos' : { 
		'Human' : { 
			'Traladaran' : 'prevalent', 
			'Thyatian' : 'common',
			'Heldannic' : 'uncommon',
			'Dunael' : 'very rare',
		 }, 
		'Dwarf' : { 'Denwarf' : 'prevalent', },
		'Elf' : { 'Vyalia' : 'common', 'Callarii' : 'prevalent' },
		'Halfling' : { 'Clanless' : 'prevalent' }, 
	},
	'Alphatia' : { 
		'Human' : {
			'Alphatian' : 'prevalent',
			'Dunael' : 'uncommon',
			'Heldanner' : 'uncommon',
			'Thothian' : 'very rare',
		}, 
		'Dwarf' : { 'Alphatian' : 'prevalent' }, 
		'Elf'   : { 'Shiye' : 'prevalent' }, 
		'Halfling' : { 'Alphatian' : 'prevalent' }, 
	},
	'Isle of Dawn' : { 
		'Human' :  {
			'Dunael' : 'prevalent',
			'Alphatian' : 'common',
			'Thyatian' : 'common',
			'Heldanner' : 'uncommon',
			'Heldannic' : 'rare',
			'Thothian' : 'common', 
		},  
		'Elf'   : { 
			'Truedyl' : 'prevalent', 
			'Vyalia' : 'rare', 
			'Shiye' : 'rare', 
		}, 
		'Rakasta' : { 'Fast Runner' : 'prevalent' }, 
	},
	'Glantri' : { 
		'Human' : {
			'Thyatian' : 'common',
			'Caurenzan' : 'common',
			'Heldannic' : 'common',
			'Alphatian' : 'common',
			'Traladaran' : 'common',
			'Flaem' : 'common',
#			'Ethengarian' : 'common', NOT IMPLEMENTED YET
			'Klantyrian' : 'common',
			'Averoignese' : 'common',
		}, 
		'Elf'   : { 'Eredyl' : 'prevalent', 'Belcadiz' : 'prevalent' },
		'Lupin' : { 
			'Mongrel Lupin' : 'prevalent', 
			'Doggerman' : 'uncommon', 
			'Mastiff' : 'uncommon', 
			'Heldann Shepherd' : 'uncommon', 
			'Das Hund' : 'uncommon' ,
		},
		'Rakasta' :  { 'Mountain Rakasta' : 'prevalent', }, 
	},
        'Darokin' : {
                'Human' : { 
                    'Daro' : 'prevalent', 
                    'Thyatian' : 'rare', 
                    'Traladaran' : 'rare',
                    'Alasiyan'  : 'rare',
                    'Averoignese' : 'rare',
                    'Klantyrian' : 'rare',
                },
                'Elf' : { 'Daro' : 'common', 'Alfheim' : 'rare', 'Belcadiz' : 'very rare' },
                'Dwarf' : { 'Denwarf' : 'common' },
                'Halfling' : { 'Shire': 'common', 'Clanless' : 'common' },
                'Lupin' : { 'Beagle' : 'common', 'Mongrel Lupin' : 'common', 'Mastiff' : 'rare' },
        },
        'Alfheim' : {
                'Elf' : { 'Alfheimer' : 'prevalent', 'Belcadiz' : 'very rare' },
                'Human' : { 'Daro' : 'common', 'Thyatian' : 'uncommon', 'Traladaran' : 'very rare' },
        },
        'Ierendi'  : {
                'Human' : {
                    'Ierendian' : 'prevalent',
                    'Makai' : 'uncommon',
                    'Daro' : 'very rare',
                    'Traladaran' : 'very rare',
                    'Thyatian' : 'very rare',
                    'Caurenzan':  'very rare',
                },
                'Elf' : { 'Ierendian' : 'prevalent' },
                'Halfling' : { 'Ierendian' : 'prevalent', 'Shire' : 'rare', },
        },
	'Shimmering Lands' : {
		'Dwarf' : { 'Moadreg' : 'prevalent' },
		'Human' : {
			'Ierendian' : 'very rare',
		},
#		'Gnome' : { 'Shimmering Lands' : 'common' },
#		'Soulbound' : { 'Shimmering Lands' : 'rare' },
#		'Giantkin' : { 'Shimmering Lands' : 'very rare' },
#		'Shade' : { 'Shimmering Lands' : 'rare' },
	},

}


align_by_origin = {
	'Human' : { 
		'Lawful'  : 'common',
		'Neutral' : 'common',
		'Chaotic' : 'uncommon',
	},
	'Alphatian' : { 
		'Lawful'  : 'uncommon',
		'Neutral' : 'common',
		'Chaotic' : 'common',
	},
	'Mountain Rakasta' : { 
		'Lawful'  : 'uncommon',
		'Neutral' : 'common',
		'Chaotic' : 'uncommon',
	},
	'Ochalean' : { 
		'Lawful'  : 'prevalent',
		'Neutral' : 'common',
		'Chaotic' : 'uncommon',
	},
	'Dwarf' : { 
		'Lawful'  : 'prevalent',
		'Neutral' : 'common',
		'Chaotic' : 'rare',
	},
	'Halfling' : { 
		'Lawful'  : 'common',
		'Neutral' : 'uncommon',
		'Chaotic' : 'uncommon',
	},
        'Hulean' : {
                'Lawful'  : 'rare',
                'Neutral' : 'common',
                'Chaotic' : 'prevalent',
        },
}
align_by_origin['Alasiyan']=align_by_origin['Dwarf']
align_by_origin['Elf']=align_by_origin['Human']
align_by_origin['Thyatian']=align_by_origin['Human']
align_by_origin['Traladaran']=align_by_origin['Human']
align_by_origin['Vatski/Vrodniki']=align_by_origin['Human']
align_by_origin['Heldannic']=align_by_origin['Human']
align_by_origin['Heldanner']=align_by_origin['Human']
align_by_origin['Shar-Pei']=align_by_origin['Ochalean']
align_by_origin['Chow Chow']=align_by_origin['Ochalean']
align_by_origin['Ochalean Crested']=align_by_origin['Ochalean']
align_by_origin['Ochalean Houndling']=align_by_origin['Ochalean']
align_by_origin['Mongrel Lupin']=align_by_origin['Human']
align_by_origin['Mastiff']=align_by_origin['Human']
align_by_origin['Snoutzer']=align_by_origin['Human']
align_by_origin['Heldann Shepherd']=align_by_origin['Human']
align_by_origin['Beagle']=align_by_origin['Human']
align_by_origin['Doggerman']=align_by_origin['Human']
align_by_origin['Das Hund']=align_by_origin['Human']
align_by_origin['Nithian Rambler']=align_by_origin['Halfling']
align_by_origin['Fennec']=align_by_origin['Alasiyan']
align_by_origin['Foxfolk']=align_by_origin['Mountain Rakasta']
align_by_origin['Dunael']=align_by_origin['Mountain Rakasta']
align_by_origin['Pardasta']=align_by_origin['Mountain Rakasta']
align_by_origin['Flaem']=align_by_origin['Alphatian']
align_by_origin['Klantyrian']=align_by_origin['Human']
align_by_origin['Averoignese']=align_by_origin['Mountain Rakasta']
align_by_origin['Ispan']=align_by_origin['Human']
align_by_origin['Verdan']=align_by_origin['Mountain Rakasta']
align_by_origin['Bellaynish']=align_by_origin['Mountain Rakasta']
align_by_origin['Zvornikian Sentinel']=align_by_origin['Dwarf']
align_by_origin['Slagovici Gonic']=align_by_origin['Human']
align_by_origin['Bouchon']=align_by_origin['Human']
align_by_origin['Renardois Folk']=align_by_origin['Human']
align_by_origin['Papillon']=align_by_origin['Alphatian']
align_by_origin['Carrasquito']=align_by_origin['Human']
align_by_origin['Narvaezan Maremma']=align_by_origin['Dwarf']
align_by_origin['Eusdrian']=align_by_origin['Human']
align_by_origin['Thothian']=align_by_origin['Alphatian']
align_by_origin['Ethengar']=align_by_origin['Human']
align_by_origin['Caurenzan']=align_by_origin['Alphatian']
align_by_origin['Daro']=align_by_origin['Human']
align_by_origin['Ierendian']=align_by_origin['Mountain Rakasta']
align_by_origin['Makai']=align_by_origin['Mountain Rakasta']
align_by_origin['Atruaghin']=align_by_origin['Human']
align_by_origin['Moadreg']=align_by_origin['Hulean']

common_weapons = {
	'any' : [ 'Dagger', 'Club', 'Staff', 'Spear', 'Mace', 'Short Bow' ],
	'Traladaran' : [ 'Short Sword', 'Hand Axe', 'Long Sword' ],
	'Thyatian' : [ 'Short Sword', 'Javelin', 'Long Sword', 'Trident', 'Net', 'Cestus', 'Rapier', 'Light Crossbow' ],
	'Heldanner' : [ 'Battle Axe', 'Hand Axe', 'Pole Axe', 'Warhammer', 'Short Sword', 'Long Sword', 'Two Handed Sword', 'Bastard Sword' ],
	'Heldannic' : [ 'Long Sword', 'Lance', 'Halberd', 'Warhammer', 'Two Handed Sword', 'Pike' ],
	'Dunael' : [ 'Long Sword', 'Javelin', 'Long Bow', 'Bastard Sword' ],
	'Ochalean' : ['Long Sword', 'Chakram', 'Bullroarer Knife', 'Light Crossbow' ],
	'Alphatian' : [ 'Long Sword', 'Pike' ],
	'Dwarf' : [ 'Battle Axe', 'Hand Axe', 'Pole Axe', 'Warhammer', 'Long Sword', 'Throwing Hammer', 'Heavy Crossbow', 'Light Crossbow', 'Halberd' ],
	'Elf' : [ 'Long Sword', 'Long Bow', 'Short Sword' ],
	'Halfling' : [ 'Bastard Sword', 'Sling', 'Short Sword', 'Hand Axe' ],
	'Alasiyan' : [ 'Long Sword', 'Lance', 'Halberd', 'Pike', 'Short Sword' ],
	'Daro' : [ 'Rapier', 'Dagger', 'Halberd', 'Short Sword' ],
	'Ispan' : [ 'Six-Shooter', 'Rapier', 'Dagger', 'Long Sword', 'Short Sword' ],
	'Thothian' : [ 'Long Sword', 'Battle axe' ],
	'Ethengar' : [ 'Long Sword', 'Hand Axe', 'Bolas', 'Long Bow', 'Lance', ],
        'Hule' : [ 'Long Sword', 'Short Sword', 'Long Bow', 'Short Bow', 'Mace', ],
        'Makai' : [ 'Trident', 'Net', ],
        'Atruaghin' : [ 'Hand Axe' ],
}
common_weapons['Heldann Shepherd'] = common_weapons['Heldanner']
common_weapons['Doggerman'] = common_weapons['Heldannic']
common_weapons['Das Hund'] = common_weapons['Heldannic']
common_weapons['Vatski/Vrodniki'] = common_weapons['Heldanner']
common_weapons['Eusdrian'] = common_weapons['Heldanner']
common_weapons['Shar-Pei'] = common_weapons['Ochalean']
common_weapons['Ochalean Houndling'] = common_weapons['Ochalean']
common_weapons['Fennec'] = common_weapons['Halfling']
common_weapons['Mastiff'] = common_weapons['Thyatian']
common_weapons['Shiye'] = common_weapons['Elf']
common_weapons['Denwarf'] = common_weapons['Dwarf']
common_weapons['Modrigswerg'] = common_weapons['Dwarf']
common_weapons['Nithian Rambler'] = common_weapons['Alasiyan']
common_weapons['Snoutzer'] = common_weapons['Heldanner']
common_weapons['Chow Chow'] = common_weapons['Ochalean']
common_weapons['Mongrel Lupin'] = common_weapons['Thyatian']
common_weapons['Foxfolk'] = common_weapons['Heldanner']
common_weapons['Pardasta'] = common_weapons['Ochalean']
common_weapons['Beagle'] = common_weapons['Thyatian']
common_weapons['Ochalean Crested'] = common_weapons['Halfling']
common_weapons['Averoignese'] = common_weapons['Daro']
common_weapons['Flaem'] = common_weapons['Daro']
common_weapons['Belcadiz'] = common_weapons['Daro']
common_weapons['Caurenzan'] = common_weapons['Daro']
common_weapons['Bellaynish'] = common_weapons['Ispan']
common_weapons['Verdan'] = common_weapons['Ispan']
common_weapons['Narvaezan Maremma'] = common_weapons['Ispan']
common_weapons['Carrasquito'] = common_weapons['Ispan']
common_weapons['Renardois Folk'] = common_weapons['Ispan']
common_weapons['Bouchon'] = common_weapons['Ispan']
common_weapons['Montoya'] = common_weapons['Ispan']

alternate_origin_by_region = {
	'Savage Coast' : {
		'Ispan' : 'Espa',
		'Dunael' : 'Robrenn',
		'Belcadiz' : 'Torre\\\'oner'
	},
	'Thyatis' : {
		'Heldannic' : 'Hattian',
		'Caurenzan' : 'Kantrian',
	},
	'Isle of Dawn' : {
		'Heldannic' : 'Hattian',
	},
	'Karameikos' : {
		'Heldannic' : 'Thyatian',
		'Dunael' : 'Thyatian',
	},
	'Glantri' : {
		'Heldannic' : 'Aalbanese',
		'Traladaran' : 'Boldavian',
	},
        'Hule' : {
                'Traladaran' : 'Olgarian',  
        },
}


# Some basic functions; possibly move somewhere else
def init_config(_freq):
	global freq
	if _freq=='variant' : freq = variant_freq
	elif _freq=='exponential' : freq = exponential_freq
	elif _freq=='linear' : freq = linear_freq
	elif _freq=='quadratic' : freq = quadratic_freq
	else : freq = default_freq
	print ('Frequency method set to', freq)

def class_selector(race, origin, region) :
	def_classes = classes_by_origin['Thyatian']
	if race in [ 'Dwarf', 'Elf', 'Halfling' ] : 
		def_classes = classes_by_origin[race]
	classes = classes_by_origin.get(origin, def_classes)	
	res = sum([ [ c ] * freq[classes[c]] for c in classes ],[])
	if region == 'Glantri' : 
		for c in [ 'Cleric', 'Druid', 'Shaman' ] :
			while res.count(c) > 1 : res.remove(c)
	return res
	

def get_origin_name(region, origin):
	try : return alternate_origin_by_region[region][origin]
	except KeyError : return origin

def align_selector(race, origin) :	
	def_aligns = align_by_origin['Human']
	if race in [ 'Dwarf', 'Elf', 'Halfling' ] :
		def_aligns = align_by_origin[race]
	
	aligns = align_by_origin.get(origin, def_aligns)
	#print ('aligns for ' + race + ", " + origin)
	#print (aligns)
	return sum([ [ c ] * freq[aligns[c]] for c in aligns ],[])

	
def races_selector(region):
	return sum([ [ r ] * freq[races_by_region[region][r]] for r in races_by_region[region] ],[])

def origin_selector(region, race):
	return sum([ [ o ] * freq[ethnic_by_region[region][race][o]] for o in ethnic_by_region[region][race] ],[])

def languages(region):
	return sum([ list(ethnic_by_region[region][e].keys()) for e in ethnic_by_region[region]],[])

def ethnic_by_race(race):
	res = []
	for r in ethnic_by_region :
		try :
			res+=ethnic_by_region[r][race]
		except KeyError :
			pass
	return list(set(res))

def races() :
	res = []
	for r in races_by_region :
		res+=races_by_region[r]
	return list(set(res))

def get_adj(ab_scores, ability):
	score=ab_scores[ability]
	if score == 18 : return 3
	elif score > 15: return 2
	elif score > 12: return 1
	elif score > 8 : return 0
	elif score > 5 : return -1
	elif score > 3 : return -2
	else : return -3
	
if __name__ == '__main__' :
	rc = races()
	print (rc)
	for r in rc : 
		print (r, ethnic_by_race(r))
