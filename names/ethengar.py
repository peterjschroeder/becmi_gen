#!/usr/bin/python

male_names = ["Abaka" ,"Abakan" ,"Abushka" ,"Akbalik" ,"Akbar" ,"Akov" ,"Aksinya" ,"Anaktai" ,"Arghun" ,"Arik" ,"Atika" ,"Babar" ,"Baidu" ,"Batu" ,"Barak" ,"Basl" ,"Bektor" ,"Berke" ,"Boga" ,"Buka" ,"Chagatai" ,"Chibai" ,"Chimei" ,"Cudga" ,"Dasadas" ,"Degke" ,"Duttai" ,"Essen" ,"Ethenor" ,"Gaidu" ,"Gakadu" ,"Ghazan" ,"Gokti" ,"Grokat" ,"Hatu" ,"Huaji" ,"Hulagu" ,"Jagatai" ,"Jamuga" ,"Jebe" ,"Juchi" ,"Kadan" ,"Kaidu" ,"Kaikhatu" ,"Kaunchi" ,"Kashin" ,"Kassar" ,"Kahak" ,"Khabul" ,"Knyuk" ,"Kogatai" ,"Kogotal" ,"Koja" ,"Kublai" ,"Kuyuk" ,"Mangu" ,"Madutai" ,"Makbai" ,"Medu" ,"Mongke" ,"Mongu" ,"Morkatal" ,"Muhuli" ,"Nargabai" ,"Nayan" ,"Noghai" ,"Noyon" ,"Numughan" ,"Ogodai" ,"Oktai" ,"Orkajin" ,"Ortu" ,"Potor" ,"Subuta" ,"Taranis" ,"Telek" ,"Temujin" ,"Temur" ,"Toktai" ,"Tuda" ,"Tulabugha" ,"Tuli" ,"Ulatai" ,"Ulgata" ,"Vasilas" ,"Yagatu" ,"Yamun" ,"Yatak" ,"Yestai" ,"Yesugai"]

female_names = ["Abbuka" ,"Kowlesin" ,"Temulin" ,"Actacta" ,"Kwelon" ,"Tena" ,"Actun-tai" ,"Lassick" ,"Tessia" ,"Ai-Bantu" ,"Lisai" ,"Trungpa" ,"Ari-Ki" ,"Loi-Tan" ,"Una" ,"Arika" ,"Loubai" ,"Uiska" ,"Astuni" ,"Lowelon" ,"Ullai" ,"Babari" ,"Mahka" ,"Vilma" ,"Beckga" ,"Maklai" ,"Voltai" ,"Bulagan" ,"Mostan" ,"Voxila" ,"Erikai" ,"Octosis" ,"Essie" ,"Oruni" ,"Goihan" ,"Otebu" ,"Gossick" ,"Ottai" ,"Gurricktai" ,"Pabulai" ,"Gwendai" ,"Patai" ,"Kacdan" ,"SanJin" ,"Kadran-Tal" ,"Sempura" ,"Kacrick" ,"Sicontai" ,"Kashinai" ,"Sirona" ,"Kassiri" ,"Situ" ,"Kokachin" ,"Solei" ,"Kostin" ,"Talia"]


from random import choice

def get_name(gender='m'):
	if gender == 'm' : return choice(male_names)+ ' of Clan '+choice(male_names)
	else : return choice(female_names)+ ' of Clan '+choice(female_names)

if __name__ == '__main__' :
	print (get_name())

