#!/usr/bin/python

from random import choice
from dice import *

i_trait = {
 'Al Kalim' : { 'Dogmatic/Open-Minded' : 1, 'Honest/Deceitful' : 1, 'Forgiving/Vengeful' : -1, 'Generous/Greedy' : 1 },
 'Alphatia' : { 'Peaceful/Violent' : 3 } ,
 'Alphaks' : { 'Peaceful/Violent': -2, 'Courageous/Fearful': 3, 'Energetic/Lazy': 1 },
 'Asterius' : { 'Generous/Greedy' : -3 } ,
 'Chardastes' : { 'Generous/Greedy' : 1, 'Peaceful/Violent' : 1 } ,
 'Chernobog' : { 'Peaceful/Violent' : -3 } ,
 'Cretia' : { 'Courageous/Fearful' : 3, 'Energetic/Lazy' : 2, 'Honest/Deceitful' : -1 }, 
 'Demogorgon'  : { 'Dogmatic/Open-Minded' : 3, 'Courageous/Fearful' : 2, 'Energetic/Lazy' : 2 },
 'Diulanna' : { 'Energetic/Lazy' : 3, 'Courageous/Fearful' : 1, 'Cautious/Rash' : -1 } ,
 'Eyrindul' : { 'Dogmatic/Open-Minded' : -3, 'Cautious/Rash' : -1 } ,
 'Forsetta' : { 'Loyal/Unreliable' : 3, 'Dogmatic/Open-Minded' : 1, 'Honest/Deceitful' : 2 } ,
 'Frey' : { 'Loyal/Unreliable' : 1, 'Peaceful/Violent' : 2 } ,
 'Freyja' : { 'Loyal/Unreliable' : 1, 'Peaceful/Violent' : 2 } ,
 'Halav' : { 'Courageous/Fearful' : 2, 'Cautious/Rash' : 2, 'Peaceful/Violent' : -3 },
 'Hel' : { 'Forgiving/Vengeful' : -2, 'Cautious/Rash' : 3 } ,
 'Hymir' : { 'Cautious/Rash' : -3, 'Generous/Greedy' : -1 } ,
 'Idris' : { 'Cautious/Rash' : -3, 'Trusting/Suspicious' : -3, 'Dogmatic/Open-Minded' : 3 } ,
 'Ilsundal' : { 'Cautious/Rash' : 3, 'Loyal/Unreliable' : 1, 'Peaceful/Violent' : 1 } ,
 'Ixion' : { 'Energetic/Lazy' : 2, 'Courageous/Fearful' : 1, 'Loyal/Unreliable' : 1 } ,
 'Kagyar' : { 'Energetic/Lazy' : 2, 'Honest/Deceitful' : 1 }, 
 'Khoronus' : { 'Energetic/Lazy' : -1, 'Honest/Deceitful': 1, 'Forgiving/Vengeful' : 1 },
 'Koryis' : { 'Peaceful/Violent' : 3, 'Honest/Deceitful' : 1, 'Generous/Greedy' : 1 }, 
 'Leptar' : { 'Peaceful/Violent' : -3, 'Cautious/Rash' : -1, 'Forgiving/Vengeful' : -2 },
 'Loki' : { 'Honest/Deceitful' : -3, 'Dogmatic/Open-Minded' : -3 } ,
 'Lornasen' : {} ,
 'Masauwu' : { 'Honest/Deceitful' : -3, 'Dogmatic/Open-Minded' : -3, 'Cautious/Rash' : 3, 'Peaceful/Violent' : 2 } ,
 'Mealiden' : { 'Courageous/Fearful' : 2, 'Cautious/Rash' : -2, 'Generous/Greedy' : +1 },
 'Night Hunter' : { 'Peaceful/Violent' : -1, 'Courageous/Fearful' : 1 } ,
 'Nyx' : { 'Dogmatic/Open-Minded' : -2, 'Cautious/Rash' : 1 } ,
 'Odin' : { 'Peaceful/Violent' : -1, 'Courageous/Fearful' : 1 } ,
 'Orcus' : { 'Peaceful/Violent' : -2, 'Forgiving/Vengeful' : -1, 'Dogmatic/Open-Minded' : 2 },
 'Palartarkan' : { 'Cautious/Rash' : 1, 'Modest/Proud' : -1, 'Peaceful/Violent' : 1 } ,
 'Petra' : { 'Peaceful/Violent' : 1, 'Loyal/Unreliable': 2 },
 'Protius' : { 'Dogmatic/Open-Minded' : -1 } ,
 'Rathanos' : { 'Dogmatic/Open-Minded' : 2, 'Modest/Proud' : -3 } ,
 'Razud' : { 'Dogmatic/Open-Minded' : -1, 'Cautious/Rash' : 1, 'Trusting/Suspicious' : -1 } ,
 'Saimpt Malinois' : { 'Peaceful/Violent' : -1, 'Courageous/Fearful' : 1, 'Dogmatic/Open-Minded' : 1 } ,
 'Saimpt Ralon' : { 'Peaceful/Violent' : 1, 'Loyal/Unreliable': 2 },
 'Skauf-Halli' : { 'Dogmatic/Open-Minded' : -3 } ,
 'Skuld' : { 'Energetic/Lazy' : -1 } ,
 'Tarastia' : { 'Loyal/Unreliable' : 3 } ,
 'The Twelve Watchers' : { 'Peaceful/Violent' : 1, 'Cautious/Rash' : 1 },
 'Terra' : { 'Loyal/Unreliable' : 1, 'Peaceful/Violent' : 1, },
 'Thor' : { 'Peaceful/Violent' : -6, 'Courageous/Fearful' : 3, 'Cautious/Rash': -3 } ,
 'Valerias' : { 'Peaceful/Violent' : 1, 'Generous/Greedy' : 1 } ,
 'Vanya' : { 'Forgiving/Vengeful' : -6 } ,
 'Volos' : { 'Cautious/Rash' : 1, 'Trusting/Suspicious' : -1 } ,
 'Volund' : { 'Forgiving/Vengeful' : -2, 'Generous/Greedy' : -2 } ,
 'Zirchev' : { 'Dogmatic/Open-Minded' : -3 } ,
}

i_druid = set([ 'Frey', 'Freyja', 'Night Hunter', 'Skauf-Halli', 'Zirchev' ])
i_unusual = set([ 'Idris' ])
i_thyatis = set([ 'Ixion', 'Tarastia', 'Valerias', 'Protius', 'Odin', 'Thor', 'Asterius' ])
i_heldann = set([ 'Thor', 'Odin', 'Frey', 'Freyja', 'Hel', 'Loki', 'Forsetta', 'Hymir', 'Skuld', 'Protius' ])
i_ochalean = set(['Baxian Shendao', 'Jade Temple of Ochalea', 'Order of the Shadow Court', 'Circle of Heaven and Earth', 'Mystic Way of Order' ])
i_ochalean_lupin = set([ 'Warmasters of the Five Directions', 'Night Hunter', 'Skauf-Halli', 'Thor' ]) | i_ochalean
i_renardois = set([ 'Night Hunter', 'Skauf-Halli', 'Saimpt C\\\'ebard', 'Saimpt M\^atin', 'Saimpt Ralon', 'Saimpt Malinois' ])
i_ispan = set([ 'Thor', 'Valerias', 'Vanya', 'Masauwu', 'Mealiden' ])
i_bellayne = set([ 'Kayar', 'Tarastia', 'Vanya', 'Ordana', 'Calitha' ])

by_origin = {
    'Dwarf' : set([ 'Chernobog', 'Kagyar', 'Volund' ]),
    'Elf' : set([ 'Ilsundal', 'Lornasen', 'Eiryndul' ]),
    'Heldanner' : i_heldann,
    'Alphatian' : set([ 'Alphatia', 'Palartarkan', 'Koryis', 'Razud', 'Ixion', 'Rathanos' ]),
    'Vatski/Vrodniki' : set([ 'Ixion', 'Chernobog', 'Volos', 'Thor', 'Odin', 'Frey', 'Freyja' ]),
    'Thyatian' : i_thyatis,
    'Heldannic' :  set([ 'Vanya' ]),
    'Dunael' : set([ 'Diulanna', 'Odin', 'Frey', 'Freyja', 'Thor', 'Zirchev', 'Asterius', 'Kagyar', 'Faunus', 'Ordana' ]),
    'Ochalean' : i_ochalean | set([ 'Koryis', 'Skauf-Halli', 'Valerias', 'Diulanna', 'Tarastia', 'Nyx', 'Chernobog', 'Chardastes', 'Ixion', 'Zirchev', 'Protius' ]),
    'Alasiyan' : set([ 'Al Kalim' ]),
    'Foxfolk' : i_druid,
    'Heldann Shepherd' : i_heldann | i_druid,
    'Snoutzer' : i_heldann | i_druid,
    'Shar-Pei' : i_ochalean_lupin,
    'Ochalean Houndling' : i_ochalean_lupin,
    'Ochalean Crested' : i_ochalean_lupin,
    'Chow Chow' : i_ochalean_lupin,
    'Doggerman' : i_thyatis,
    'Mastiff' : i_thyatis,
    'Beagle' : i_thyatis,
    'Das Hund' : i_thyatis,
    'Mongrel Lupin' : i_thyatis,
    'Nithian Rambler' : set([ 'Pflarr', 'Chernobog' ]),
    'Fennec' : set([ 'Al Kalim' ]),
    'Halfling' : set(['Hin High Heroes']),
    'Mountain Rakasta' : set(['Druidism', 'Shamanism']),
    'Pardasta' : set(['Druidism', 'Shamanism'])|i_ochalean,
    'Traladaran' : set([ 'Halav', 'Petra', 'Zirchev', 'Chardastes', 'Cult of Halav', 'Church of Traladara', 'Orcus', 'Dark Triad' ]),
    'Glantri' : set([ 'Rad' ]),
    'Flaem' : set([ 'Rad', 'Alphaks' ]),
    'Verdan' : i_ispan,
    'Ispan' : i_ispan | set(['Ixion']),
    'Carrasquito' : i_ispan,
    'Narvaezan Maremma' : i_ispan | set(['Ixion']),
    'Slagovici Gonic' : set(['Halav']),
    'Zvornikian Sentinel' : set(['Halav']),
    'Renardois Folk' : i_renardois,
    'Bouchon' : i_renardois,
    'Papillon': i_renardois,
    'Bellaynish' : i_bellayne,
    'Eusdrian': i_heldann | set(['Ilsundal','Eyrindul']),
    'Ethengar' : set([ 'Terra', 'Ixion', 'Kagyar', 'Cretia' ]),
    'Daro' : set([ 'Asterius', 'Ixion', 'Valerias', 'Chardastes', 'Khoronus', 'Odin', 'Church of Darokin', 'Church of Universal Harmony', 'Eternal Truth', 'Augrism', 'The Twelve Watchers' ]),
    'Hulean' : set([ 'Loki', 'Faunus', 'Hel', 'Valerias', 'Rathanos', 'Orcus', 'Talitha', 'Masauwu', 'Pearl', 'Chernobog', 'Alphaks', ]),
    'Alfheim' : set([ 'Ilsundal', 'Mealiden', ]),
    'Ierendi' : set([ 'Protius' ]),
    'Atruaghin' : set([ 'Atzanteotl', 'Danel Tigerstripes', 'Atruaghin', 'Mahmatti Running Elk', 'Tahkati Stormtamer', 'Hattani Stoneclaw', 'Ahmanni Turtlerider', 'Druidism']),
    'Moadreg' : set([ 'Kagyar', 'Angrboda', 'Belnos',  'The Dreamer', 'Garal Glitterlode', 'Khoronus', 'Skuld', 'Slizzark', 'Stodos', 'Zugzul']),
}

pantheon = {
    'Norwold' : set(['Druidism', 'Heldann Sidhr', 'Mos Thyaticum']),
    'Thyatis' : set(['Mos Thyaticum']),
    'Ylaruam' : set(['Eternal Truth', 'Magian Fire Worshippers']),
    'Isle of Dawn' : set(['Druidism', 'Heldann Sidhr', 'Mos Thyaticum']),
    'Alphatia' : set(['Pantheon of the Seven']),
    'Karameikos' : set([ 'Church of Karameikos', 'Church of Traladara', 'Cult of Halav', 'Gens Caelenes', 'Dark Triad' ]),
    'Glantri' : set([ 'Temple of Rad' ]),
    'Savage Coast' : set([ 'Druidism', 'Iglesia de Narvaez' ]),
    'Rockhome' : set([]),
        'Darokin' : set([ 'Church of Darokin', 'Eternal Truth', 'Church of Universal Harmony', 'Augrism', ]),
        'Hule' : set([ 'Temple of Chaos', 'Way of Law', 'Druidism' ]),
        'Alfheim' : set([]),
        'Ierendi' : set([ 'People\'s Temple of Ierendi', 'Eternal Truth' ]),
    'Shimmering Lands' : set(['The Ancients', 'Cult of Dominion', 'Oracles', 'Silver and Gold', 'Fiery Forge', 'Way of the Stone']),
}

philosophy = {
    'Chaotic' : set(['Philosophy of Chaos']),
    'Lawful'  : set(['Philosophy of Law']),
    'Neutral' : set(['Philosophy of Neutrality']), 
}

i_lawful = set([ 'Atruaghin', 'Ahmanni Turtlerider', 'Tahkati Stormtamer', 'Hattani Stoneclaw', 'Augrism', 'Church of Darokin', 'Church of Universal Harmony', 'Temple of Rad', 'Al Kalim', 'Alphatia', 'Rad', 'Asterius', 'Diulanna', 'Forsetta', 'Frey', 'Freyja', 'Hel', 'Terra', 'Ilsundal', 'Ixion', 'Kagyar', 'Night Hunter', 'Nyx', 'Odin', 'Razud', 'Skauf-Halli', 'Tarastia', 'Thor', 'Valerias', 'Vanya', 'Volund', 'Philosophy of Law', 'Shamanism', 'Mos Thyaticum', 'Heldann Sidhr', 'Hin High Heroes', 'Chardastes', 'Koryis', 'Eternal Truth', 'Jade Temple of Ochalea', 'Mystic Way of Order', 'Pantheon of the Seven', 'Church of Karameikos', 'Church of Traladara', 'Halav', 'Petra', 'Mealiden', 'Iglesia de Narvaez', 'Saimpt Malinois', 'Saimpt M\^atin', 'Saimpt Ralon', 'Saimpt Cl\\\'ebard', 'Way of Law' ])
i_neutral = set([ 'Skuld', 'Atruaghin', 'Ahmanni Turtlerider', 'Tahkati Stormtamer', 'Mahmatti Running Elk', 'People\'s Temple of Ierendi', 'Khoronus', 'The Twelve Watchers', 'Augrism', 'Church of Darokin', 'Church of Universal Harmony', 'Temple of Rad', 'Alphatia', 'Asterius', 'Rad', 'Chardastes', 'Diulanna', 'Eyrindul', 'Frey', 'Freyja', 'Hel', 'Hymir', 'Ixion', 'Loki', 'Lornasen', 'Night Hunter', 'Odin', 'Palartarkan', 'Protius', 'Rathanos', 'Razud', 'Skauf-Halli', 'Skuld', 'Thor', 'Valerias', 'Vanya', 'Volos', 'Volund', 'Zirchev', 'Druidism', 'Shamanism', 'Heldann Sidhr', 'Hin High Heroes', 'Nyx', 'Baxian Shendao', 'Jade Temple of Ochalea', 'Order of the Shadow Court', 'Circle of Heaven and Earth', 'Eternal Truth', 'Church of Traladara', 'Church of Karameikos', 'Petra', 'Ordana', 'Saimpt Ralon', 'Saimpt M\^atin', 'Faunus', 'Calitha' ])
i_chaotic = set([ 'Stodos', 'Slizzark', 'Atzanteotl', 'Danel Tigerstripes', 'Church of Darokin', 'Temple of Rad', 'Asterius', 'Chernobog', 'Eyrindul', 'Hel', 'Idris', 'Ixion', 'Loki', 'Night Hunter', 'Church of Karameikos', 'Cretia', 'Protius', 'Rathanos', 'Razud', 'Skauf-Halli', 'Valerias', 'Vanya', 'Volund', 'Philosophy of Chaos', 'Shamanism', 'Nyx', 'Order of the Shadow Court', 'Dark Triad', 'Cult of Halav', 'Gens Caelenes', 'Orcus', 'Demogorgon', 'Leptar', 'Alphaks', 'Masauwu', 'Saimpt Ralon', 'Faunus', 'Magian Fire Worshippers', 'Temple of Chaos' ])

by_alignment = {
    'Chaotic' : i_chaotic,
    'Lawful'  : i_lawful,
    'Neutral' : i_neutral, 
}

by_region = {
    'Norwold' : set([ 'Alphatia', 'Asterius', 'Chernobog', 'Diulanna', 'Eyrindul', 'Forsetta', 'Frey', 'Freyja', 'Hel', 'Hymir', 'Idris', 'Ilsundal', 'Ixion', 'Kagyar', 'Loki', 'Lornasen', 'Night Hunter', 'Nyx', 'Odin', 'Palartarkan', 'Protius', 'Rathanos', 'Razud', 'Skauf-Halli', 'Skuld', 'Tarastia', 'Thor', 'Valerias', 'Volos', 'Volund', 'Zirchev', 'Heldann Sidhr', 'Alphaks', 'Mos Thyaticum', 'Hin High Heroes', 'Shamanism', 'Druidism', 'Philosophy of Law', 'Philosophy of Chaos', 'Philosophy of Neutrality' ]),
    'Thyatis' : set([ 'Asterius', 'Chernobog', 'Diulanna', 'Ilsundal', 'Ixion', 'Kagyar', 'Loki', 'Night Hunter', 'Nyx', 'Odin', 'Protius', 'Skauf-Halli', 'Tarastia', 'Thor', 'Valerias', 'Zirchev', 'Mos Thyaticum', 'Philosophy of Law', 'Philosophy of Chaos', 'Philosophy of Neutrality', 'Koryis', 'Chardastes', 'Baxian Shendao', 'Jade Temple of Ochalea', 'Alphaks' ]),
    'Ylaruam' : set([ 'Magian Fire Worshippers', 'Eternal Truth', 'Philosophy of Law', 'Philosophy of Chaos', 'Philosophy of Neutrality', 'Kagyar', 'Al Kalim', 'Odin', 'Pflarr' ]),
    'Alphatia' : set([ 'Alphatia', 'Chernobog', 'Diulanna', 'Eyrindul', 'Frey', 'Freyja', 'Hel', 'Ixion', 'Kagyar', 'Koryis', 'Night Hunter', 'Nyx', 'Odin', 'Palartarkan', 'Rathanos', 'Razud', 'Thor', 'Heldann Sidhr', 'Hin High Heroes', 'Druidism', 'Philosophy of Law', 'Philosophy of Chaos', 'Philosophy of Neutrality' ]),
    'Isle of Dawn' : set([ 'Alphatia', 'Asterius', 'Diulanna', 'Eyrindul', 'Forsetta', 'Frey', 'Freyja', 'Hel', 'Hymir', 'Ilsundal', 'Ixion', 'Kagyar', 'Loki', 'Nyx', 'Odin', 'Palartarkan', 'Protius', 'Rathanos', 'Razud', 'Skuld', 'Tarastia', 'Thor', 'Valerias', 'Volund', 'Zirchev', 'Heldann Sidhr', 'Mos Thyaticum', 'Shamanism', 'Druidism', 'Philosophy of Law', 'Philosophy of Chaos', 'Philosophy of Neutrality', 'Alphaks' ]),
    'Karameikos' : set([ 'Church of Karameikos', 'Church of Traladara', 'Cult of Halav', 'Chardastes', 'Halav', 'Petra', 'Zirchev', 'Valerias', 'Asterius', 'Kagyar', 'Ilsundal', 'Tarastia', 'Vanya', 'Orcus', 'Demogorgon', 'Leptar', 'Dark Triad', 'Gens Caelenes', 'Nyx' ]),
    'Glantri' : set([ 'Rad', 'Philosophy of Chaos', 'Philosophy of Law', 'Philosophy of Neutrality', 'Razud' ]),
    'Ethengar Khanate' : set([ 'Terra', 'Ixion', 'Kagyar', 'Cretia' ]),
    'Savage Coast' : set([ 'Hel',  'Nyx', 'Ilsundal', 'Eyrindul', 'Frey', 'Freyja', 'Loki', 'Thor', 'Valerias', 'Vanya', 'Ixion', 'Halav', 'Tarastia', 'Skauf-Halli', 'Night Hunter', 'Asterius', 'Calitha', 'Saimpt C\\\'ebard', 'Saimpt M\^atin', 'Saimpt Ralon', 'Saimpt Malinois', 'Mealiden', 'Masauwu', 'Odin', 'Iglesia de Narvaez', 'Faunus', 'Kagyar', 'Diulanna', 'Ordana' ]),
    'Rockhome' : set([ 'Kagyar', 'Philosophy of Law', 'Philosophy of Neutrality', 'Philosophy of Chaos', 'Chernobog', 'Al Kalim', 'Eternal Truth', 'Heldann Sidhr' ]),
        'Darokin' : set([ 'Asterius', 'Philosophy of Law', 'Philosophy of Neutrality', 'Philosophy of Chaos', 'Church of Darokin', 'Eternal Truth', 'Koryis', 'The Twelve Watchers', 'Khoronus', 'Church of Universal Harmony', 'Kagyar', 'Augrism', 'Ixion', 'Chardastes', 'Odin', 'Valerias' ]),
        'Hule' : set([ 'Way of Law', 'Temple of Chaos', 'Druidism', 'Philosophy of Law', 'Philosophy of Chaos', 'Philosophy of Neutrality', 'Loki', 'Faunus', 'Hel', 'Valerias', 'Rathanos', 'Orcus', 'Talitha', 'Masauwu', 'Pearl', 'Chernobog', 'Alphaks', ]),
        'Alfheim' : set([ 'Ilsundal', 'Mealiden', 'Church of Thyatis', 'Church of Darokin', 'Druidism', 'Philosophy of Law', 'Philosophy of Chaos', 'Philosophy of Neutrality' ]),
        'Ierendi' : set([ 'Protius', 'People\'s Temple of Ierendi', 'Eternal Truth', 'Druidism', 'Philosophy of Law', 'Philosophy of Chaos', 'Philosophy of Neutrality']),
        'Atruaghin Clans' : set([ 'Atzanteotl', 'Danel Tigerstripes', 'Atruaghin', 'Mahmatti Running Elk', 'Tahkati Stormtamer', 'Hattani Stoneclaw', 'Ahmanni Turtlerider', 'Druidism']),
    'Shimmering Lands' : set([ 'Kagyar', 'Angrboda', 'Belnos',  'The Dreamer', 'Garal Glitterlode', 'Khoronus', 'Skuld', 'Slizzark', 'Stodos', 'Zugzul']) | pantheon['Shimmering Lands'],
}

replace_by_origin = {
        'Heldanner' : {
                'Protius' : 'Spooming Nooga',
        },
    'Thyatian' : {
        'Chernobog' : 'Thanatos',
        'Ixion' : 'Solarios',
        'Tarastia' : 'Pax Bellanica',
        'Skauf-Halli' : 'Korotiku',
        'Thor' : 'Alcaeus',
    },
    'Ochalean' : {
        'Skauf-Halli' : 'Eight Tails Fox',
        'Night Hunter' : 'Shi Jielan',
        'Thor' : 'Shi Doushang',
        'Koryis' : 'Koru Yi-Si',
        'Chardastes' : 'Chang Dangsu',
        'Nyx' : 'Queen of the Shadow Court',
    },
    'Denwarf' : {
        'Chernobog' : 'Karr',
    },
    'Dunael' : {
        'Asterius' : 'Belnos',
        'Faunus' : 'Cernuinn',
        'Diulanna' : 'Arduinna',
        'Kagyar': 'Belsamas',
        'Odin' : 'Taranos',
        'Ordana' : 'Breig',
        'Thor' : 'Tuatis',
        'Zirchev' : 'Leug',
    },
    'Eusdrian' : {
        'Ilsundal' : 'Tiuz',
        'Eyrindul' : 'Eyris',
        'Thor' : 'Donar',
        'Odin' : 'Viuden',
        'Frey' : 'Fredar',
        'Freyja': 'Fredara',
        'Loki' : 'Lokar',
        'Nyx' : 'Nyt',
        'Hel' : 'Hela',
    },
    'Alphatian' : {
        'Chernobog' : 'Thanatos',
        'Skauf-Halli' : 'Korotiku', 
    },
    'Alasiyan' : {
        'Chernobog' : 'Thanatos',
        'Odin' : 'Zephyr',
        'Pflarr' : 'The Jackal',
                'Protius' : 'Old Man of the Sea',
    },
        'Ierendi' : {
                'Protius' : 'Old Man of the Sea',
        },
    'Vatski/Vrodniki' : {
        'Thor' : 'Perun',
        'Ixion' : 'Dazhbog',
        'Frey' : 'Yaro',
        'Freyja' : 'Yara',
        'Hel' : 'Mara',
        'Zirchev' : 'Eagle Spirit',
        'Night Hunter' : 'Wolf Spirit',
        'Simurg' : 'Semargl',
        'Terra' : 'Zemlya',
    },
    'Ispan' : {
        'Thor' : 'the General',
        'Tarastia' : 'the Judge',
        'Vanya' : 'Fa\~na',
        'Masauwu' : 'the Ambassador',
        'Mealiden' : 'Milan',
    },
    'Verdan' : {
        'Thor' : 'the General',
        'Tarastia' : 'the Judge',
        'Vanya' : 'Fanha',
        'Masauwu' : 'the Ambassador',
        'Mealiden' : 'Milan',
    },
    'Renardois Folk' : {
        'Skauf-Halli' : 'Saimpt R\\\'enard',
        'Night Hunter' : 'Saimpt Loup',
    },
    'Bellaynish' : {
        'Calitha' : 'Felidae',
        'Tarastia' : 'Pax Bellanica',
        'Ordana' : 'Tawnia',
        'Vanya' : 'Belbion',
    },
    'Ethengar' : {
        'Terra' : 'Yamuga the Yurt Dweller',
        'Ixion' : 'Tubak the Lawgiver',
        'Cretia' : 'Cretia the Lord of Chaos',
        'Kagyar' : 'Kazgar',
    },
        'Hulean' : {
                'Loki' : 'Bozdogan',
                'Valerias' : 'Sevigunesh',
                'Pearl' : 'Guzelik',
                'Faunus' : 'Eylenmek',
                'Thanatos' : 'Buyulome',
                'Orcus' : 'Savashan',
                'Talitha' : 'Yazabali',
                'Masauwu' : 'Yalanemek',
                'Rathanos' : 'Yangunesh',
                'Alphaks' : 'Veleketer',
        },
}
replace_by_origin['Bouchon']=replace_by_origin['Renardois Folk']
replace_by_origin['Papillon']=replace_by_origin['Renardois Folk']
replace_by_origin['Carrasquito']=replace_by_origin['Ispan']
replace_by_origin['Narvaezan Maremma']=replace_by_origin['Ispan']
replace_by_origin['Ispan Pistolero']=replace_by_origin['Ispan']


def get_immortal(cclass, race, origin, alignment, region):
    if cclass == 'Forester' : return 'Ilsundal', i_trait['Ilsundal']
    if cclass == 'Shaman' : return 'Shamanism', {}
    if cclass == 'Shamani': return 'Atruaghin', {}
    # add immortals and pantheons available for the race/origin
    base_set = set([])
    try : base_set|= by_origin[origin]
    except KeyError : 
        try : base_set|= by_origin[race]
        except KeyError : 
            if region!='Glantri' : print (origin, race)
    try : base_set|= pantheon[region]
    except KeyError : print (region)
    # constrain by alignment and region
    base_set &= by_alignment[alignment]
    base_set &= by_region[region]
    # handle special cases
    if cclass=='Druid' : base_set &= i_druid|set(['Druidism'])
    # fix : if empty set, at least the aligned philosophy.
    if not len(base_set) or d10()==1 : base_set|=philosophy[alignment]
    # return selection and associated trait adjustments
    res = choice(list(base_set))
    try :   out = replace_by_origin[origin][res] 
    except KeyError : out = res
    try : return out, i_trait[res]
    except KeyError : return out, {}

if __name__ == '__main__' :
    from sys import argv
    if len(argv)<6:
        print ('Not enough arguments')
        print ('Usage: immortals class race origin alignment region')
    print (get_immortal(*argv[1:]))
