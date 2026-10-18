import random
import time
dkp=["Epic:siva siahaan","Epic:harvey moeis","Rare:sjamsul nursalim","Rare:surya darmadi","Uncommon:honggo wedratno","Uncommon:adam damiri & sonny widjaja","Common:benny tjokrosaputro & heru hidayat","Common:johnny g plate"]

dbp=["Epic:dewa 19","Epic:sheila on 7","Epic:noah(dulu peterpan)","Rare:slank","Rare:juicy luicy","Rare:kangen band","Rare:feast","Uncommon:sukatani"]

dmp=["Epic:mie ayam","Epic:rendang","Epic:bakso","Rare:sate","Rare:nasi goreng","Rare:gado gado","Uncommon:martabak manis/terang bulan","Uncommon:bubur ayam"]

dap=["Legendary:raffi ahmad","Legendary:rhoma irama","Epic:sule","Epic:reza rahardian","Epic:deddy corbuzier","Rare:ayu ting ting","Rare:baim wong","Rare:atta halilintar"]

dsp=["Legendary:sendal emak","Legendary:ikat pinggang bapak","Epic:sapu lidi emak","Epic:keris","Epic:badik","Epic:celurit","Rare:parang","Rare:golok"]

dmrp=["Legendary:reza arap",'Legendary:aloy & niko','Legendary:jot','Legendary: garry','Epic:vconk','Epic:yuka','Epic:tepe & ibot','Rare:markam']

dhp=["Mythical:kuntilanak",'Mythical:pocong','Legendary:genderuwo','Legendary:tuyul','Legendary:kuyang','Epic:sundel bolong','Epic:wewe gombel','Epic:banaspati']

d9p=["Mythical:robert budi hartono", "Mythical:michael bambang hartono", "Mythical:oey tiong ham", "Legendary:prajogo pangestu", "Legendary:low tuck kwong", "Legendary:eka tjipta widjaja", "Legendary:liem sioe liong", "Epic:anthoni salim", "Epic:chairul tanjung"]

dmhp=["Mythical:dollar",'Mythical:ongkir luar pulau jawa','Mythical:kejujuran pejabat','Legendary:pajak bea cukai','Legendary:anggaran MBG(makanan beracun gratis)','Legendary:anggaran kopdes','Epic:pertamax','Epic:biaya sogokan pejabat']

d4p=['Divine:ybrap','Divine:tierison','Mythical:king aloy','Mythical:bravyson','Mythical:garry ang','Mythical:yukatheo','Legendary:teguh prakoso','Legendary:ibot','Legendary:niko junius']

dpp = ["Divine:jenderal sudirman", "Divine:pangeran diponegoro", "Mythical:bung tomo", "Mythical:patimura", "Mythical:tuanku imam bonjol", "Mythical:cut nyak dhien", "Legendary:raden ajeng kartini", "Legendary:ki hadjar dewantara"]

dprp = ["Divine:b.j. habibie", "Divine:susilo bambang yudhoyono", "Divine:soekarno", "Divine:abdurrahman wahid", "Mythical:joko widodo", "Mythical:soeharto", "Mythical:megawati soekarnoputri", "Mythical:prabowo subianto"]




pkp=[2.5,5,10,12.5,15,15,20,20]
pkp2=[3,7,12,15,15,15,15,18]
pkp3  = [4, 6, 10, 12, 15, 17, 18, 18]
pkp4  = [5, 7, 11, 12, 14, 16, 17.5, 17.5]
pkp5  = [6, 8, 12, 12.5, 14, 15.5, 16, 16]
pkp6  = [7, 9, 12.5, 13, 13.5, 15, 15, 15]
pkp7  = [8, 10, 13, 13, 13, 14.5, 14.5, 14]
pkp8  = [9, 11, 13.5, 13, 12.5, 14, 13.5, 13.5]
pkp9  = [10, 12, 14, 13, 12, 13.5, 13, 12.5]
pkp10 = [11, 13, 14, 13, 11.5, 13, 12.5, 12]
pkp11 = [12, 14, 14, 13, 11, 12.5, 12, 11.5]
pkp12 = [13, 14.5, 14, 13, 10.5, 12, 11.5, 11]
pkp13 = [14, 15, 14, 12.5, 10, 11.5, 11, 10.5]
pkp14 = [15, 15.5, 14, 12, 9.5, 11, 10.5, 10]
pkp15 = [16, 16, 14, 11.5, 9, 10.5, 10, 9]
pkp16 = [17, 16.5, 14, 11, 8.5, 10, 9.5, 8.5]
pkp17 = [18, 17, 14, 10.5, 8, 9.5, 9, 8]
pkp18 = [19, 17.5, 14, 10, 7.5, 9, 8.5, 7.5]
pkp19 = [20, 18, 14, 9.5, 7, 8.5, 8, 7]
pkp20 = [21, 18.5, 14, 9, 6.5, 8, 7.5, 6.5]
pkp21 = [22, 19, 14, 8.5, 6, 7.5, 7, 6]
pkp22 = [23, 19.5, 14, 8, 5.5, 7, 6.5, 5.5]
pkp23 = [24, 20, 14, 7.5, 5, 6.5, 6, 5]
pkp24 = [25, 20.5, 14, 7, 4.5, 6, 5.5, 4.5]
pkp25 = [26, 21, 14, 6.5, 4, 5.5, 5, 4]


pbp=[2.5,5,10,12.5,15,15,20,20]
pbp2=[3,7,12,15,15,15,15,18]
pbp3  = [4, 6, 10, 12, 15, 17, 18, 18]
pbp4  = [5, 7, 11, 12, 14, 16, 17.5, 17.5]
pbp5  = [6, 8, 12, 12.5, 14, 15.5, 16, 16]
pbp6  = [7, 9, 12.5, 13, 13.5, 15, 15, 15]
pbp7  = [8, 10, 13, 13, 13, 14.5, 14.5, 14]
pbp8  = [9, 11, 13.5, 13, 12.5, 14, 13.5, 13.5]
pbp9  = [10, 12, 14, 13, 12, 13.5, 13, 12.5]
pbp10 = [11, 13, 14, 13, 11.5, 13, 12.5, 12]
pbp11 = [12, 14, 14, 13, 11, 12.5, 12, 11.5]
pbp12 = [13, 14.5, 14, 13, 10.5, 12, 11.5, 11]
pbp13 = [14, 15, 14, 12.5, 10, 11.5, 11, 10.5]
pbp14 = [15, 15.5, 14, 12, 9.5, 11, 10.5, 10]
pbp15 = [16, 16, 14, 11.5, 9, 10.5, 10, 9]
pbp16 = [17, 16.5, 14, 11, 8.5, 10, 9.5, 8.5]
pbp17 = [18, 17, 14, 10.5, 8, 9.5, 9, 8]
pbp18 = [19, 17.5, 14, 10, 7.5, 9, 8.5, 7.5]
pbp19 = [20, 18, 14, 9.5, 7, 8.5, 8, 7]
pbp20 = [21, 18.5, 14, 9, 6.5, 8, 7.5, 6.5]
pbp21 = [22, 19, 14, 8.5, 6, 7.5, 7, 6]
pbp22 = [23, 19.5, 14, 8, 5.5, 7, 6.5, 5.5]
pbp23 = [24, 20, 14, 7.5, 5, 6.5, 6, 5]
pbp24 = [25, 20.5, 14, 7, 4.5, 6, 5.5, 4.5]
pbp25 = [26, 21, 14, 6.5, 4, 5.5, 5, 4]

pmp=[2.5,5,10,12.5,15,15,20,20]
pmp2=[3,7,12,15,15,15,15,18]
pmp3  = [4, 6, 10, 12, 15, 17, 18, 18]
pmp4  = [5, 7, 11, 12, 14, 16, 17.5, 17.5]
pmp5  = [6, 8, 12, 12.5, 14, 15.5, 16, 16]
pmp6  = [7, 9, 12.5, 13, 13.5, 15, 15, 15]
pmp7  = [8, 10, 13, 13, 13, 14.5, 14.5, 14]
pmp8  = [9, 11, 13.5, 13, 12.5, 14, 13.5, 13.5]
pmp9  = [10, 12, 14, 13, 12, 13.5, 13, 12.5]
pmp10 = [11, 13, 14, 13, 11.5, 13, 12.5, 12]
pmp11 = [12, 14, 14, 13, 11, 12.5, 12, 11.5]
pmp12 = [13, 14.5, 14, 13, 10.5, 12, 11.5, 11]
pmp13 = [14, 15, 14, 12.5, 10, 11.5, 11, 10.5]
pmp14 = [15, 15.5, 14, 12, 9.5, 11, 10.5, 10]
pmp15 = [16, 16, 14, 11.5, 9, 10.5, 10, 9]
pmp16 = [17, 16.5, 14, 11, 8.5, 10, 9.5, 8.5]
pmp17 = [18, 17, 14, 10.5, 8, 9.5, 9, 8]
pmp18 = [19, 17.5, 14, 10, 7.5, 9, 8.5, 7.5]
pmp19 = [20, 18, 14, 9.5, 7, 8.5, 8, 7]
pmp20 = [21, 18.5, 14, 9, 6.5, 8, 7.5, 6.5]
pmp21 = [22, 19, 14, 8.5, 6, 7.5, 7, 6]
pmp22 = [23, 19.5, 14, 8, 5.5, 7, 6.5, 5.5]
pmp23 = [24, 20, 14, 7.5, 5, 6.5, 6, 5]
pmp24 = [25, 20.5, 14, 7, 4.5, 6, 5.5, 4.5]
pmp25 = [26, 21, 14, 6.5, 4, 5.5, 5, 4]

pap=[2.5,5,10,12.5,15,15,20,20]
pap2=[3,7,12,15,15,15,15,18]
pap3  = [4, 6, 10, 12, 15, 17, 18, 18]
pap4  = [5, 7, 11, 12, 14, 16, 17.5, 17.5]
pap5  = [6, 8, 12, 12.5, 14, 15.5, 16, 16]
pap6  = [7, 9, 12.5, 13, 13.5, 15, 15, 15]
pap7  = [8, 10, 13, 13, 13, 14.5, 14.5, 14]
pap8  = [9, 11, 13.5, 13, 12.5, 14, 13.5, 13.5]
pap9  = [10, 12, 14, 13, 12, 13.5, 13, 12.5]
pap10 = [11, 13, 14, 13, 11.5, 13, 12.5, 12]
pap11 = [12, 14, 14, 13, 11, 12.5, 12, 11.5]
pap12 = [13, 14.5, 14, 13, 10.5, 12, 11.5, 11]
pap13 = [14, 15, 14, 12.5, 10, 11.5, 11, 10.5]
pap14 = [15, 15.5, 14, 12, 9.5, 11, 10.5, 10]
pap15 = [16, 16, 14, 11.5, 9, 10.5, 10, 9]
pap16 = [17, 16.5, 14, 11, 8.5, 10, 9.5, 8.5]
pap17 = [18, 17, 14, 10.5, 8, 9.5, 9, 8]
pap18 = [19, 17.5, 14, 10, 7.5, 9, 8.5, 7.5]
pap19 = [20, 18, 14, 9.5, 7, 8.5, 8, 7]
pap20 = [21, 18.5, 14, 9, 6.5, 8, 7.5, 6.5]
pap21 = [22, 19, 14, 8.5, 6, 7.5, 7, 6]
pap22 = [23, 19.5, 14, 8, 5.5, 7, 6.5, 5.5]
pap23 = [24, 20, 14, 7.5, 5, 6.5, 6, 5]
pap24 = [25, 20.5, 14, 7, 4.5, 6, 5.5, 4.5]
pap25 = [26, 21, 14, 6.5, 4, 5.5, 5, 4]

psp=[2.5,5,10,12.5,15,15,20,20]
psp2=[3,7,12,15,15,15,15,18]
psp3  = [4, 6, 10, 12, 15, 17, 18, 18]
psp4  = [5, 7, 11, 12, 14, 16, 17.5, 17.5]
psp5  = [6, 8, 12, 12.5, 14, 15.5, 16, 16]
psp6  = [7, 9, 12.5, 13, 13.5, 15, 15, 15]
psp7  = [8, 10, 13, 13, 13, 14.5, 14.5, 14]
psp8  = [9, 11, 13.5, 13, 12.5, 14, 13.5, 13.5]
psp9  = [10, 12, 14, 13, 12, 13.5, 13, 12.5]
psp10 = [11, 13, 14, 13, 11.5, 13, 12.5, 12]
psp11 = [12, 14, 14, 13, 11, 12.5, 12, 11.5]
psp12 = [13, 14.5, 14, 13, 10.5, 12, 11.5, 11]
psp13 = [14, 15, 14, 12.5, 10, 11.5, 11, 10.5]
psp14 = [15, 15.5, 14, 12, 9.5, 11, 10.5, 10]
psp15 = [16, 16, 14, 11.5, 9, 10.5, 10, 9]
psp16 = [17, 16.5, 14, 11, 8.5, 10, 9.5, 8.5]
psp17 = [18, 17, 14, 10.5, 8, 9.5, 9, 8]
psp18 = [19, 17.5, 14, 10, 7.5, 9, 8.5, 7.5]
psp19 = [20, 18, 14, 9.5, 7, 8.5, 8, 7]
psp20 = [21, 18.5, 14, 9, 6.5, 8, 7.5, 6.5]
psp21 = [22, 19, 14, 8.5, 6, 7.5, 7, 6]
psp22 = [23, 19.5, 14, 8, 5.5, 7, 6.5, 5.5]
psp23 = [24, 20, 14, 7.5, 5, 6.5, 6, 5]
psp24 = [25, 20.5, 14, 7, 4.5, 6, 5.5, 4.5]
psp25 = [26, 21, 14, 6.5, 4, 5.5, 5, 4]

ptp=[0.5,3,10,10,10,15,15,15]
ptp2 = [1.54, 3.86, 10.36, 10, 10, 14.64, 14.14, 13.96]
ptp3 = [2.57, 4.71, 10.71, 10, 10, 14.29, 13.29, 12.93]
ptp4 = [3.61, 5.57, 11.07, 10, 10, 13.93, 12.43, 11.89]
ptp5 = [4.64, 6.43, 11.43, 10, 10, 13.57, 11.57, 10.86]
ptp6 = [5.68, 7.29, 11.79, 10, 10, 13.21, 10.71, 9.82]
ptp7 = [6.71, 8.14, 12.14, 10, 10, 12.86, 9.86, 8.79]
ptp8 = [7.75, 9, 12.5, 10, 10, 12.5, 9, 7.75]
ptp9 = [8.79, 9.86, 12.86, 10, 10, 12.14, 8.14, 6.71]
ptp10 = [9.82, 10.71, 13.21, 10, 10, 11.79, 7.29, 5.68]
ptp11 = [10.86, 11.57, 13.57, 10, 10, 11.43, 6.43, 4.64]
ptp12 = [11.89, 12.43, 13.93, 10, 10, 11.07, 5.57, 3.61]
ptp13 = [12.93, 13.29, 14.29, 10, 10, 10.71, 4.71, 2.57]
ptp14 = [13.96, 14.14, 14.64, 10, 10, 10.36, 3.86, 1.54]
ptp15 = [15, 15, 15, 10, 10, 10, 3, 0.5]
ptp16 = [16.04, 15.86, 15.36, 10, 10, 9.64, 2.14, 0.46]
ptp17 = [17.07, 16.71, 15.71, 10, 10, 8.93, 1.29, 0.42]
ptp18 = [18.11, 17.57, 16.07, 10, 10, 8.21, 0.43, 0.38]
ptp19 = [19.14, 18.43, 16.43, 10, 10, 7.5, 0.35, 0.34]
ptp20 = [20.18, 19.29, 16.79, 10, 10, 6.79, 0.31, 0.3]
ptp21 = [21.21, 20.14, 17.14, 10, 10, 6.07, 0.27, 0.26]
ptp22 = [22.25, 21, 17.5, 10, 10, 5.36, 0.23, 0.22]
ptp23 = [23.29, 21.86, 17.86, 10, 10, 4.64, 0.19, 0.18]
ptp24 = [24.32, 22.71, 18.21, 10, 10, 3.93, 0.15, 0.14]
ptp25 = [25.36, 23.57, 18.57, 10, 10, 3.21, 0.11, 0.1]

p9p = [0.5, 0.5, 3, 10, 10, 10, 15, 15, 15]
p9p2 = [1.2, 1.2, 3.86, 10.36, 10, 10, 14.64, 14.14, 13.96]
p9p3 = [1.9, 1.9, 4.71, 10.71, 10, 10, 14.29, 13.29, 12.93]
p9p4 = [2.6, 2.6, 5.57, 11.07, 10, 10, 13.93, 12.43, 11.89]
p9p5 = [3.3, 3.3, 6.43, 11.43, 10, 10, 13.57, 11.57, 10.86]
p9p6 = [4, 4, 7.29, 11.79, 10, 10, 13.21, 10.71, 9.82]
p9p7 = [4.7, 4.7, 8.14, 12.14, 10, 10, 12.86, 9.86, 8.79]
p9p8 = [5.4, 5.4, 9, 12.5, 10, 10, 12.5, 9, 7.75]
p9p9 = [6.1, 6.1, 9.86, 12.86, 10, 10, 12.14, 8.14, 6.71]
p9p10 = [6.8, 6.8, 10.71, 13.21, 10, 10, 11.79, 7.29, 5.68]
p9p11 = [7.5, 7.5, 11.57, 13.57, 10, 10, 11.43, 6.43, 4.64]
p9p12 = [8.2, 8.2, 12.43, 13.93, 10, 10, 11.07, 5.57, 3.61]
p9p13 = [8.9, 8.9, 13.29, 14.29, 10, 10, 10.71, 4.71, 2.57]
p9p14 = [9.6, 9.6, 14.14, 14.64, 10, 10, 10.36, 3.86, 1.54]
p9p15 = [10.3, 10.3, 15, 15, 10, 10, 10, 3, 0.5]
p9p16 = [11, 11, 15.86, 15.36, 10, 10, 9.64, 2.14, 0.46]
p9p17 = [11.7, 11.7, 16.71, 15.71, 10, 10, 8.93, 1.29, 0.42]
p9p18 = [12.4, 12.4, 17.57, 16.07, 10, 10, 8.21, 0.43, 0.38]
p9p19 = [13.1, 13.1, 18.43, 16.43, 10, 10, 7.5, 0.35, 0.34]
p9p20 = [13.8, 13.8, 19.29, 16.79, 10, 10, 6.79, 0.31, 0.3]
p9p21 = [14.5, 14.5, 20.14, 17.14, 10, 10, 6.07, 0.27, 0.26]
p9p22 = [15.2, 15.2, 21, 17.5, 10, 10, 5.36, 0.23, 0.22]
p9p23 = [15.9, 15.9, 21.86, 17.86, 10, 10, 4.64, 0.19, 0.18]
p9p24 = [16.6, 16.6, 22.71, 18.21, 10, 10, 3.93, 0.15, 0.14]
p9p25 = [17.3, 17.3, 23.57, 18.57, 10, 10, 3.21, 0.11, 0.1]

p4p = [0.2, 0.3, 0.5, 3, 10, 10, 10, 15, 15]
p4p2 = [0.5, 0.7, 1.2, 3.86, 10.36, 10, 10, 14.64, 14.14]
p4p3 = [0.8, 1.1, 1.9, 4.71, 10.71, 10, 10, 14.29, 13.29]
p4p4 = [1.1, 1.5, 2.6, 5.57, 11.07, 10, 10, 13.93, 12.43]
p4p5 = [1.4, 1.9, 3.3, 6.43, 11.43, 10, 10, 13.57, 11.57]
p4p6 = [1.7, 2.3, 4, 7.29, 11.79, 10, 10, 13.21, 10.71]
p4p7 = [2, 2.7, 4.7, 8.14, 12.14, 10, 10, 12.86, 9.86]
p4p8 = [2.3, 3.1, 5.4, 9, 12.5, 10, 10, 12.5, 9]
p4p9 = [2.6, 3.5, 6.1, 9.86, 12.86, 10, 10, 12.14, 8.14]
p4p10 = [2.9, 3.9, 6.8, 10.71, 13.21, 10, 10, 11.79, 7.29]
p4p11 = [3.2, 4.3, 7.5, 11.57, 13.57, 10, 10, 11.43, 6.43]
p4p12 = [3.5, 4.7, 8.2, 12.43, 13.93, 10, 10, 11.07, 5.57]
p4p13 = [3.8, 5.1, 8.9, 13.29, 14.29, 10, 10, 10.71, 4.71]
p4p14 = [4.1, 5.5, 9.6, 14.14, 14.64, 10, 10, 10.36, 3.86]
p4p15 = [4.4, 5.9, 10.3, 15, 15, 10, 10, 10, 3]
p4p16 = [4.7, 6.3, 11, 15.86, 15.36, 10, 10, 9.64, 2.14]
p4p17 = [5, 6.7, 11.7, 16.71, 15.71, 10, 10, 8.93, 1.29]
p4p18 = [5.3, 7.1, 12.4, 17.57, 16.07, 10, 10, 8.21, 0.43]
p4p19 = [5.6, 7.5, 13.1, 18.43, 16.43, 10, 10, 7.5, 0.35]
p4p20 = [5.9, 7.9, 13.8, 19.29, 16.79, 10, 10, 6.79, 0.31]
p4p21 = [6.2, 8.3, 14.5, 20.14, 17.14, 10, 10, 6.07, 0.27]
p4p22 = [6.5, 8.7, 15.2, 21, 17.5, 10, 10, 5.36, 0.23]
p4p23 = [6.8, 9.1, 15.9, 21.86, 17.86, 10, 10, 4.64, 0.19]
p4p24 = [7.1, 9.5, 16.6, 22.71, 18.21, 10, 10, 3.93, 0.15]
p4p25 = [7.4, 9.9, 17.3, 23.57, 18.57, 10, 10, 3.21, 0.11]

ppp = [0.2, 0.3, 0.5, 3, 10, 10, 15, 15]
ppp2 = [0.5, 0.7, 1.2, 3.86, 10.36, 10, 14.64, 14.14]
ppp3 = [0.8, 1.1, 1.9, 4.71, 10.71, 10, 14.29, 13.29]
ppp4 = [1.1, 1.5, 2.6, 5.57, 11.07, 10, 13.93, 12.43]
ppp5 = [1.4, 1.9, 3.3, 6.43, 11.43, 10, 13.57, 11.57]
ppp6 = [1.7, 2.3, 4, 7.29, 11.79, 10, 13.21, 10.71]
ppp7 = [2, 2.7, 4.7, 8.14, 12.14, 10, 12.86, 9.86]
ppp8 = [2.3, 3.1, 5.4, 9, 12.5, 10, 12.5, 9]
ppp9 = [2.6, 3.5, 6.1, 9.86, 12.86, 10, 12.14, 8.14]
ppp10 = [2.9, 3.9, 6.8, 10.71, 13.21, 10, 11.79, 7.29]
ppp11 = [3.2, 4.3, 7.5, 11.57, 13.57, 10, 11.43, 6.43]
ppp12 = [3.5, 4.7, 8.2, 12.43, 13.93, 10, 11.07, 5.57]
ppp13 = [3.8, 5.1, 8.9, 13.29, 14.29, 10, 10.71, 4.71]
ppp14 = [4.1, 5.5, 9.6, 14.14, 14.64, 10, 10.36, 3.86]
ppp15 = [4.4, 5.9, 10.3, 15, 15, 10, 10, 3]
ppp16 = [4.7, 6.3, 11, 15.86, 15.36, 10, 10, 2.14]
ppp17 = [5, 6.7, 11.7, 16.71, 15.71, 10, 10, 1.29]
ppp18 = [5.3, 7.1, 12.4, 17.57, 16.07, 10, 10, 0.43]
ppp19 = [5.6, 7.5, 13.1, 18.43, 16.43, 10, 10, 0.35]
ppp20 = [5.9, 7.9, 13.8, 19.29, 16.79, 10, 10, 0.31]
ppp21 = [6.2, 8.3, 14.5, 20.14, 17.14, 10, 10, 0.27]
ppp22 = [6.5, 8.7, 15.2, 21, 17.5, 10, 10, 0.23]
ppp23 = [6.8, 9.1, 15.9, 21.86, 17.86, 10, 10, 0.19]
ppp24 = [7.1, 9.5, 16.6, 22.71, 18.21, 10, 10, 0.15]
ppp25 = [7.4, 9.9, 17.3, 23.57, 18.57, 10, 10, 0.1]

prp = [0.2, 0.3, 0.5, 3, 10, 10, 15, 15]
prp2 = [0.5, 0.7, 1.2, 3.86, 10.36, 11, 15.64, 12.14]
prp3 = [0.8, 1.1, 1.9, 4.71, 10.71, 12, 16.29, 10.29]
prp4 = [1.1, 1.5, 2.6, 5.57, 11.07, 13, 16.93, 8.43]
prp5 = [1.4, 1.9, 3.3, 6.43, 11.43, 14, 17.57, 6.57]
prp6 = [1.7, 2.3, 4, 7.29, 11.79, 15, 18.21, 4.71]
prp7 = [2, 2.7, 4.7, 8.14, 12.14, 16, 18.86, 2.86]
prp8 = [2.3, 3.1, 5.4, 9, 12.5, 17, 19.5, 1]
prp9 = [2.6, 3.5, 6.1, 9.86, 12.86, 18, 20.14, 0.8]
prp10 = [2.9, 3.9, 6.8, 10.71, 13.21, 19, 20.79, 0.6]
prp11 = [3.2, 4.3, 7.5, 11.57, 13.57, 20, 21.43, 0.4]
prp12 = [3.5, 4.7, 8.2, 12.43, 13.93, 21, 22.07, 0.2]
prp13 = [3.8, 5.1, 8.9, 13.29, 14.29, 22, 22.71, 0.1]
prp14 = [4.1, 5.5, 9.6, 14.14, 14.64, 23, 23.36, 0.05]
prp15 = [5, 6, 11, 16, 16, 24, 24, 0.01]
prp16 = [5.3, 6.4, 11.5, 16.5, 16.5, 24.5, 24.5, 0.005]
prp17 = [5.6, 6.8, 12, 17, 17, 25, 25, 0.002]
prp18 = [5.9, 7.2, 12.5, 17.5, 17.5, 25.5, 25.5, 0.001]
prp19 = [6.2, 7.6, 13, 18, 18, 26, 26, 0.0005]
prp20 = [6.5, 8, 13.5, 18.5, 18.5, 26.5, 26.5, 0.0001]
prp21 = [6.8, 8.4, 14, 19, 19, 27, 27, 0.00005]
prp22 = [7.1, 8.8, 14.5, 19.5, 19.5, 27.5, 27.5, 0.00001]
prp23 = [7.4, 9.2, 15, 20, 20, 28, 28, 0.000005]
prp24 = [7.7, 9.6, 15.5, 20.5, 20.5, 28.5, 28.5, 0.000001]
prp25 = [8, 10, 16, 21, 21, 29, 29, 0]

bl={
    "kp":{
        1:pkp,
        2:pkp2,
        3:pkp3,
        4: pkp4,
        5: pkp5,
        6: pkp6,
        7: pkp7,
        8: pkp8,
        9: pkp9,
        10: pkp10,
        11: pkp11,
        12: pkp12,
        13: pkp13,
        14: pkp14,
        15: pkp15,
        16: pkp16,
        17: pkp17,
        18: pkp18,
        19: pkp19,
        20: pkp20,
        21: pkp21,
        22: pkp22,
        23: pkp23,
        24: pkp24,
        25: pkp25

    },
    "bp":{
        1:pbp,
        2:pbp2,
        3:pbp3,
        4: pbp4,
        5: pbp5,
        6: pbp6,
        7: pbp7,
        8: pbp8,
        9: pbp9,
        10: pbp10,
        11: pbp11,
        12: pbp12,
        13: pbp13,
        14: pbp14,
        15: pbp15,
        16: pbp16,
        17: pbp17,
        18: pbp18,
        19: pbp19,
        20: pbp20,
        21: pbp21,
        22: pbp22,
        23: pbp23,
        24: pbp24,
        25: pbp25

    },
    "mp":{
        1:pmp,
        2:pmp2,
        3:pmp3,
        4: pmp4,
        5: pmp5,
        6: pmp6,
        7: pmp7,
        8: pmp8,
        9: pmp9,
        10: pmp10,
        11: pmp11,
        12: pmp12,
        13: pmp13,
        14: pmp14,
        15: pmp15,
        16: pmp16,
        17: pmp17,
        18: pmp18,
        19: pmp19,
        20: pmp20,
        21: pmp21,
        22: pmp22,
        23: pmp23,
        24: pmp24,
        25: pmp25

    },
    "ap":{
        1:pap,
        2:pap2,
        3:pap3,
        4: pap4,
        5: pap5,
        6: pap6,
        7: pap7,
        8: pap8,
        9: pap9,
        10: pap10,
        11: pap11,
        12: pap12,
        13: pap13,
        14: pap14,
        15: pap15,
        16: pap16,
        17: pap17,
        18: pap18,
        19: pap19,
        20: pap20,
        21: pap21,
        22: pap22,
        23: pap23,
        24: pap24,
        25: pap25

    },
    "sp":{
        1:psp,
        2:psp2,
        3:psp3,
        4: psp4,
        5: psp5,
        6: psp6,
        7: psp7,
        8: psp8,
        9: psp9,
        10: psp10,
        11: psp11,
        12: psp12,
        13: psp13,
        14: psp14,
        15: psp15,
        16: psp16,
        17: psp17,
        18: psp18,
        19: psp19,
        20: psp20,
        21: psp21,
        22: psp22,
        23: psp23,
        24: psp24,
        25: psp25

    },
    "tp":   {
        1: ptp,
        2: ptp2,
        3: ptp3,
        4: ptp4,
        5: ptp5,
        6: ptp6,
        7: ptp7,
        8: ptp8,
        9: ptp9,
        10: ptp10,
        11: ptp11,
        12: ptp12,
        13: ptp13,
        14: ptp14,
        15: ptp15,
        16: ptp16,
        17: ptp17,
        18: ptp18,
        19: ptp19,
        20: ptp20,
        21: ptp21,
        22: ptp22,
        23: ptp23,
        24: ptp24,
        25: ptp25

    },
    "9p":{
        1: p9p,
        2: p9p2,
        3: p9p3,
        4: p9p4,
        5: p9p5,
        6: p9p6,
        7: p9p7,
        8: p9p8,
        9: p9p9,
        10: p9p10,
        11: p9p11,
        12: p9p12,
        13: p9p13,
        14: p9p14,
        15: p9p15,
        16: p9p16,
        17: p9p17,
        18: p9p18,
        19: p9p19,
        20: p9p20,
        21: p9p21,
        22: p9p22,
        23: p9p23,
        24: p9p24,
        25: p9p25
    },
    "4p": {
      1: p4p,
      2: p4p2,
      3: p4p3,
      4: p4p4,
      5: p4p5,
      6: p4p6,
      7: p4p7,
      8: p4p8,
      9: p4p9,
      10: p4p10,
      11: p4p11,
      12: p4p12,
      13: p4p13,
      14: p4p14,
      15: p4p15,
      16: p4p16,
      17: p4p17,
      18: p4p18,
      19: p4p19,
      20: p4p20,
      21: p4p21,
      22: p4p22,
      23: p4p23,
      24: p4p24,
      25: p4p25

    },
    "pp": {
      1: ppp,
      2: ppp2,
      3: ppp3,
      4: ppp4,
      5: ppp5,
      6: ppp6,
      7: ppp7,
      8: ppp8,
      9: ppp9,
      10: ppp10,
      11: ppp11,
      12: ppp12,
      13: ppp13,
      14: ppp14,
      15: ppp15
    },
    "rp": {
      1: prp,
      2: prp2,
      3: prp3,
      4: prp4,
      5: prp5,
      6: prp6,
      7: prp7,
      8: prp8,
      9: prp9,
      10: prp10,
      11: prp11,
      12: prp12,
      13: prp13,
      14: prp14,
      15: prp15
    }                 
}
desil = {
    1: 1,
    2: 0.95,
    3: 0.9,
    4: 0.85,
    5: 0.8,
    6: 0.75,
    7: 0.7,
    8: 0.65,
    9: 0.6,
    10: 0.5
}

dj = {
    1: 1.0, 
    2: 1.15, 
    3: 1.3, 
    4: 1.45, 
    5: 1.6, 
    6: 1.75, 
    7: 1.9, 
    8: 2.05, 
    9: 2.2, 
    10: 2.35
}

inventory = {}
inventory2 = {}
inventory3 = {}
inventory4 = {}
R3 = 0
A = 7
S = 13
SA = 19
lt1 = 4500
lt2 = 6000
lt3 = 10000
lt4 = 13000
lt5 = 16000
lt6 = 20000
h1 = 350
h2 = 500
h3 = 800
h4 = 1000
h5 = 1250
h6 = 1750
h7 = 2500
h8 = 3500
h9 = 5000
h10 = 10000
h11 = 15000
h12 = 25000

k = random.randint(350,1000)

ml1 = 100
ml2 = 250
ml3 = 500
ml4 = 550
ml5 = 600
ml7 = 650
ml8 = 700
ml9 = 850
ml10 = 1000
ml11 = 1250
ml12 = 1500

lvl = 1
xp = 0
luck = 1
ds=1
mep=100

ha1 = int(h1 * desil[ds])
ha2 = int(h2 * desil[ds])
ha3 = int(h3 * desil[ds])
ha4 = int(h4 * desil[ds])
ha5 = int(h5 * desil[ds])
ha6 = int(h6 * desil[ds])
ha7 = int(h7 * desil[ds])
ha8 = int(h8 * desil[ds])
ha9 = int(h9 * desil[ds])
ha10 = int(h10 * desil[ds])
ha11 = int(h11 * desil[ds])
ha12 = int(h12 * desil[ds])

lbt1 = int(lt1 * desil[ds])
lbt2 = int(lt2 * desil[ds])
lbt3 = int(lt3 * desil[ds])
lbt4 = int(lt4 * desil[ds])
lbt5 = int(lt5 * desil[ds])
lbt6 = int(lt6 * desil[ds])

m=""
m2=""
m3=""
print(f"anda mempunyai uang sebesar ${k}")
while True:
    lvlm = lvl
    while xp >= mep:
        xp -= mep
        lvl += 1
        
        if lvl >=1000:
          lvl=1000
          xp="inf"
          m3="(max)"
          break
        mep = 100 + (lvl - 1) * 400   
        if lvl in [10,20,25,30,40,50,60,70,75,80,90,100,110,120,125,130,140,150,160,170,175,180,190,200]:
            luck += 1
            if luck >= 25 :
              luck = 25
              m="(max)"
            if ds==10:
              m2="(max)"
            
    if lvl > lvlm:             
        print(f'''anda naik ke level {lvl}
Stats:
luck:{luck}{m}    |     exp:{xp}/{mep}
desil:{ds}{m2}     |     level:{lvl}{m3}''')

    time.sleep(1)
    qw = input('''|shop|inventory|sell|
''').lower()
    
    if qw == "shop":
        shop=input('''|pack|potion|
'''.lower())
        if shop == "pack":
          while True:
            b=input('continue? (y/n)')
            if b=="n":
              break
            else:
              if lvl < 7:
                print(f'''ini dia list pack dan harganya(1-3):
harga|  nama pack   |rarity|
${ha1}  | 1. koruptor pack| RRR  |
${ha2}  | 2. band pack    | RRR  |
${ha3}  | 3. makanan pack | RRR  |
''')
              elif lvl < 13:
                print(f'''ini dia list pack dan harganya(1-6):
harga  |  nama pack   |rarity|
${ha1}  | 1. koruptor pack| RRR  |
${ha2}  | 2. band pack    | RRR  |
${ha3}  | 3. makanan pack | RRR  |
${ha4}  | 4. artis pack   | AR   |
${ha5}  | 5. senjata pack | AR   |
${ha6}  |6. marapthon pack| AR   |
''')
              elif lvl < 19:
                print(f'''ini dia list pack dan harganya(1-9):
harga  |  nama pack   |rarity|
${ha1}  | 1. koruptor pack| RRR  |
${ha2}  | 2. band pack    | RRR  |
${ha3}  | 3. makanan pack | RRR  |
${ha4}  | 4. artis pack   | AR   |
${ha5}  | 5. senjata pack | AR   |
${ha6}  |6. marapthon pack| AR   |
${ha7}  | 7. hantu pack   | SR   |
${ha8}  | 8. 9 naga pack  | SR   |
${ha9}  | 9. mahal pack   | SR   |
''')
              else: 
                print(f'''ini dia list pack dan harganya(1-12):
harga  |  nama pack   |rarity|
${ha1}  | 1. koruptor pack| RRR  |
${ha2}  | 2. band pack    | RRR  |
${ha3}  | 3. makanan pack | RRR  |
${ha4}  | 4. artis pack   | AR   |
${ha5}  | 5. senjata pack | AR   |
${ha6}  |6. marapthon pack| AR   |
${ha7}  | 7. hantu pack   | SR   |
${ha8}  | 8. 9 naga pack  | SR   |
${ha9}  | 9. mahal pack   | SR   |
${ha10} | 10.A4A clan pack| SAR  |
${ha11} | 11.pahlawan pack| SAR  |
${ha12} | 12.presiden pack| SAR  |
''') 
# H         
            
              bp = input('mau beli pack yang mana? ').lower()
            
              if bp == "koruptor pack" or  bp == '1':
                  jpp=input('|  1X  |  10X  |  ALL  |'.lower())
                  if jpp == 'all':
                      if k >= ha1:
                          jbp= k // ha1
                          th= jbp * ha1
                          k = k% ha1
                          xp += jbp
                          print(f'anda membeli {jbp}X koruptor pack')
                          print(f'''uang -${th} uang anda sekarang ${k}''')
                          inventory2["koruptor pack"] = inventory2.get('koruptor pack',0) + jbp
                      else:
                          print(f'uang tidak mencukupi ${k}/${ha1}')
  # 100 + 186 + 260 + 299 + 347 + 399
                  elif jpp == "10x":
                      sh= ha1 * 10
                      if k >= sh:
                          k -= sh
                          xp += 10
                          print('10X koruptor pack dibeli')
                          print(f'''uang -${sh}
  uang sisa ${k}''')
                          inventory2["koruptor pack"]=inventory2.get('koruptor pack',0) + 10
                  elif jpp == "1x":  
                      if k >= ha1:
                          k -= ha1
                          xp += 1
                          print(f'uang -${ha1} uang sisa ${k} +1 koruptor pack')
                          inventory2["koruptor pack"] = inventory2.get("koruptor pack", 0) + 1
                      else:
                          print(f'uang anda tidak mencukupi ${k}/${ha1}')
                  
              elif bp == "band pack" or  bp == '2':
                  jpp=input('|  1X  |  10X  |  ALL  |'.lower())
                  if jpp == 'all':
                      if k >= ha2:
                          jbp= k // ha2
                          th= jbp * ha2
                          k = k% ha2
                          xp += jbp
                          print(f'anda membeli {jbp}X band pack')
                          print(f'''uang -${th} uang anda sekarang ${k}''')
                          inventory2["band pack"] = inventory2.get('band pack',0) + jbp
                      else:
                          print(f'uang tidak mencukupi ${k}/${ha2}')
                  elif jpp == "10x":
                      sh= ha2 * 10
                      if k >= sh:
  # ini easter cooked
                          k -= sh
                          xp += 10
                          print('10X band pack dibeli')
                          print(f'''uang -${sh}
  uang sisa ${k}''')
                          inventory2["band pack"]=inventory2.get('band pack',0) + 10
                  elif jpp == "1x":
                      if k >= ha2:
                          k -= ha2
                          xp += 1
                          print(f'uang -${ha2} uang sisa ${k} +1 band pack')
                          inventory2["band pack"] = inventory2.get("band pack", 0) + 1
                      else:
                          print(f'uang anda tidak mencukupi ${k}/${ha2}')
                  
              elif bp == "makanan pack" or  bp == '3':
                  jpp=input('|  1X  |  10X  |  ALL  |'.lower())
                  if jpp == 'all':
                      if k >= ha3:
                          jbp= k // ha3
                          th= jbp * ha3
                          k = k% ha3
                          xp += jbp
                          print(f'anda membeli {jbp}X makanan pack')
                          print(f'''uang -${th} uang anda sekarang ${k}''')
                          inventory2["makanan pack"] = inventory2.get('makanan pack',0) + jbp
  # ini easter pan
                      else:
                          print(f'uang tidak mencukupi ${k}/${ha3}')
                  elif jpp == "10x":
                      sh= ha3 * 10
                      if k >= sh:
                          k -= sh
                          xp += 10
                          print('10X makanan pack dibeli')
                          print(f'''uang -${sh}
  uang sisa ${k}''')
  # I
                          inventory2["makanan pack"]=inventory2.get('makanan pack',0) + 10
                  elif jpp == "1x":
                      if k >= ha3:
                          k -= ha3
                          xp += 1
                          print(f'uang -${ha3} uang sisa ${k} +1 makanan pack')
                          inventory2["makanan pack"] = inventory2.get("makanan pack", 0) + 1
                      else:
                          print(f'uang anda tidak mencukupi ${k}/${ha3}')
                  
              elif bp == "artis pack" or  bp == '4':
                  if lvl >= A:
                      jpp=input('|  1X  |  10X  |  ALL  |'.lower())
                      if jpp == 'all':
                          if k >= ha4:
                              jbp= k // ha4
                              th= jbp * ha4
                              k = k% ha4
                              xp += jbp
  # ini easter egg
                              print(f'anda membeli {jbp}X artis pack')
                              print(f'''uang -${th} uang anda sekarang ${k}''')
                              inventory2["artis pack"] = inventory2.get('artis pack',0) + jbp
                          else:
                              print(f'uang tidak mencukupi ${k}/${ha4}')
                      elif jpp == "10x":
                          sh= ha4 * 10
                          if k >= sh:
                              k -= sh
                              xp += 10
                              print('10X artis pack dibeli')
                              print(f'''uang -${sh}
  uang sisa ${k}''')
                              inventory2["artis pack"]=inventory2.get('artis pack',0) + 10
                      elif jpp == "1x":
                          if k >= ha4:
                              k -= ha4
                              xp += 1
                              print(f'uang -${ha4} uang sisa ${k} +1 artis pack')
                              inventory2["artis pack"] = inventory2.get("artis pack", 0) + 1
                          else:
                              print(f'uang anda tidak mencukupi ${k}/${ha4}')
                  else:
                      print(f'level tidak mencukupi level {lvl}/{A}')
  # 207 di 150 di 177 terus 249 di 150 juga di 177 lalu 207 yang udah di 150 dengan 249 yang juga sudah di 150 di taruh di 289 jadilah nazi goreng
              elif bp == "senjata pack" or  bp == '5':
                  if lvl >= A:
                      jpp=input('|  1X  |  10X  |  ALL  |'.lower())
                      if jpp == 'all':
                          if k >= ha5:
                              jbp= k // ha5
                              th= jbp * ha5
                              k = k% ha5
                              xp += jbp
                              print(f'anda membeli {jbp}X senjata pack')
                              print(f'''uang -${th} uang anda sekarang ${k}''')
                              inventory2["senjata pack"] = inventory2.get('senjata pack',0) + jbp
                          else:
                              print(f'uang tidak mencukupi ${k}/${ha5}')
                      elif jpp == "10x":
  # ini easter rice
                          sh= ha5 * 10
                          if k >= sh:
                              k -= sh
                              xp += 10
                              print('10X senjata pack dibeli')
                              print(f'''uang -${sh}
  uang sisa ${k}''')
                              inventory2["senjata pack"]=inventory2.get('senjata pack',0) + 10
                      elif jpp == "1x":
                          if k >= ha5:
                              k -= ha5
                              xp += 1
                              print(f'uang -${ha5} uang sisa ${k} +1 senjata pack')
                              inventory2["senjata pack"] = inventory2.get("senjata pack", 0) + 1
  # D
                          else:
                              print(f'uang anda tidak mencukupi ${k}/${ha5}')
                  else:
                      print(f'level tidak mencukupi level {lvl}/{A}')
                  
              elif bp == "marapthon pack" or  bp == '6':
                  if lvl >= A:
                      jpp=input('|  1X  |  10X  |  ALL  |'.lower())
                      if jpp == 'all':
                          if k >= ha6:
                              jbp= k // ha6
                              th= jbp * ha6
                              k = k% ha6
                              xp += jbp
                              print(f'anda membeli {jbp}X marapthon pack')
                              print(f'''uang -${th} uang anda sekarang ${k}''')
                              inventory2["marapthon pack"] = inventory2.get('marapthon pack',0) + jbp
                          else:
                              print(f'uang tidak mencukupi ${k}/${ha6}')
                      elif jpp == "10x":
                          sh= ha6 * 10
                          if k >= sh:
                              k -= sh
                              xp += 10
  # ini easter plate
                              print('10X marapthon pack dibeli')
                              print(f'''uang -${sh}
  uang sisa ${k}''')
                              inventory2["marapthon pack"]=inventory2.get('marapthon pack',0) + 10
                      elif jpp == "1x":
                          if k >= ha6:
                              k -= ha6
                              xp += 1
                              print(f'uang -${ha6} uang sisa ${k} +1 marapthon pack')
                              inventory2["marapthon pack"] = inventory2.get("marapthon pack", 0) + 1
                          else:
                              print(f'uang anda tidak mencukupi ${k}/${ha6}')
                  else:
                      print(f'level tidak mencukupi level {lvl}/{A}')
  # U
              elif bp == "hantu pack" or  bp == '7':
                  if lvl >= S: 
                      jpp=input('|  1X  |  10X  |  ALL  |'.lower())
                      if jpp == 'all':
                          if k >= ha7:
                              jbp= k // ha7
                              th= jbp * ha7
                              k = k% ha7
                              xp += jbp
                              print(f'anda membeli {jbp}X hantu pack')
                              print(f'''uang -${th} uang anda sekarang ${k}''')
                              inventory2["hantu pack"] = inventory2.get('hantu pack',0) + jbp
                          else:
                              print(f'uang tidak mencukupi ${k}/${ha7}')
                      elif jpp == "10x":
                          sh= ha7 * 10
                          if k >= sh:
                              k -= sh
                              xp += 10
                              print('10X hantu pack dibeli')
                              print(f'''uang -${sh}
  uang sisa ${k}''')
                              inventory2["hantu pack"]=inventory2.get('hantu pack',0) + 10
                      elif jpp == "1x":
                          if k >= ha7:
                              k -= ha7
                              xp += 1
                              print(f'uang -${ha7} uang sisa ${k} +1 hantu pack')
                              inventory2["hantu pack"] = inventory2.get("hantu pack", 0) + 1
                          else:
                              print(f'uang anda tidak mencukupi ${k}/${ha7}')
                  else:
                      print(f'level tidak mencukupi level {lvl}/{S}')
                  
              elif bp == "9 naga pack" or  bp == '8': 
                  if lvl >= S: 
                      jpp=input('|  1X  |  10X  |  ALL  |'.lower())
                      if jpp == 'all':
                          if k >= ha8:
                              jbp= k // ha8
                              th= jbp * ha8
                              k = k% ha8
                              xp += jbp
                              print(f'anda membeli {jbp}X 9 naga pack')
                              print(f'''uang -${th} uang anda sekarang ${k}''')
                              inventory2["9 naga pack"] = inventory2.get('9 naga pack',0) + jbp
                          else:
  # P
                              print(f'uang tidak mencukupi ${k}/${ha8}')
                      elif jpp == "10x":
                          sh= ha8 * 10
                          if k >= sh:
                              k -= sh
                              xp += 10
                              print('10X 9 naga pack dibeli')
                              print(f'''uang -${sh}
  uang sisa ${k}''')
                              inventory2["9 naga pack"]=inventory2.get('9 naga pack',0) + 10        
                      elif jpp == "1x":
                          if k >= ha8:
                              k -= ha8
                              xp += 1
                              print(f'uang -${ha8} uang sisa ${k} +1 9 naga pack')
                              inventory2["9 naga pack"] = inventory2.get("9 naga pack", 0) + 1
                          else:
                              print(f'uang anda tidak mencukupi ${k}/${ha8}')
                  else:
                      print(f'level tidak mencukupi level {lvl}/{S}')
  
              elif bp == "mahal pack" or  bp == '9':
                  if lvl >= S: 
                      jpp=input('|  1X  |  10X  |  ALL  |'.lower())
                      if jpp == 'all':
                          if k >= ha9:
                              jbp= k // ha9
                              th= jbp * ha9
                              k = k% ha9
                              xp += jbp
                              print(f'anda membeli {jbp}X mahal pack')
                              print(f'''uang -${th} uang anda sekarang ${k}''')
                              inventory2["mahal pack"] = inventory2.get('mahal pack',0) + jbp
                          else:
                              print(f'uang tidak mencukupi ${k}/${ha9}')
                      elif jpp == "10x":
                          sh= ha9 * 10
                          if k >= sh:
                              k -= sh
                              xp += 10
                              print('10X mahal pack dibeli')
                              print(f'''uang -${sh}
  uang sisa ${k}''')
                              inventory2["mahal pack"]=inventory2.get('mahal pack',0) + 10
                      elif jpp == "1x":
                          if k >= ha9:
                              k -= ha9
                              xp += 1
                              print(f'uang -${ha9} uang sisa ${k} +1 mahal pack')
                              inventory2["mahal pack"] = inventory2.get("mahal pack", 0) + 1
                          else:
  # JKW
                              print(f'uang anda tidak mencukupi ${k}/${ha9}')
                  else:
                      print(f'level tidak mencukupi level {lvl}/{S}')
                                              
              elif bp == "a4a clan pack" or  bp == '10':
                  if lvl >= SA:
                      jpp=input('|  1X  |  10X  |  ALL  |'.lower())
                      if jpp == 'all':
                          if k >= ha10:
                              jbp= k // ha10
                              th= jbp * ha10
                              k = k% ha10
                              xp += jbp
                              print(f'anda membeli {jbp}X A4A clan pack')
                              print(f'''uang -${th} uang anda sekarang ${k}''')
                              inventory2["A4A clan pack"] = inventory2.get('A4A clan pack',0) + jbp
                          else:
                              print(f'uang tidak mencukupi ${k}/${ha10}')
                      elif jpp == "10x":
                          sh= ha10 * 10
                          if k >= sh:
                              k -= sh
                              xp += 10
                              print('10X A4A clan pack dibeli')
                              print(f'''uang -${sh}
  uang sisa ${k}''')
                              inventory2["A4A clan pack"]=inventory2.get('A4A clan pack',0) + 10
                      elif jpp == "1x":
                          if k >= ha10:
                              k -= ha10
                              xp += 1
                              print(f'uang -${ha10} uang sisa ${k} +1 A4A clan pack')
                              inventory2["A4A clan pack"] = inventory2.get("A4A clan pack", 0) + 1
                          else:
                              print(f'uang anda tidak mencukupi ${k}/${h10}')
                  else:
                      print(f'level tidak mencukupi level {lvl}/{SA}')
                  
              elif bp == "pahlawan pack" or  bp == '11':
                  if lvl >= SA:
                      jpp=input('|  1X  |  10X  |  ALL  |'.lower())
                      if jpp == 'all':
                          if k >= ha11:
                              jbp= k // ha11
                              th= jbp * ha11
                              k = k% ha11
                              xp += jbp
                              print(f'anda membeli {jbp}X pahlawan pack')
                              print(f'''uang -${th} uang anda sekarang ${k}''')
                              inventory2["pahlawan pack"] = inventory2.get('pahlawan pack',0) + jbp
                          else:
                              print(f'uang tidak mencukupi ${k}/${ha11}')
                      elif jpp == "10x":
                          sh= ha11 * 10
                          if k >= sh:
                              k -= sh
                              xp += 10
                              print('10X pahlawan pack dibeli')
                              print(f'''uang -${sh}
  uang sisa ${k}''')
                              inventory2["pahlawan pack"]=inventory2.get('pahlawan pack',0) + 10
                      elif jpp == "1x":
                          if k >= ha11:
                              k -= ha11
                              xp += 1
                              print(f'uang -${ha11} uang sisa ${k} +1 pahlawan pack')
                              inventory2["pahlawan pack"] = inventory2.get("pahlawan pack", 0) + 1
                          else:
                              print(f'uang anda tidak mencukupi ${k}/${ha11}') 
                  else:
                      print(f'level tidak mencukupi level {lvl}/{SA}')
                  
              elif bp == "presiden pack" or  bp == '12': 
                  if lvl >= SA:
                      jpp=input('|  1X  |  10X  |  ALL  |'.lower())
                      if jpp == 'all':
                          if k >= ha12:
                              jbp= k // ha12
                              th= jbp * ha12
                              k = k% ha12
                              xp += jbp
                              print(f'anda membeli {jbp}X presiden pack')
                              print(f'''uang -${th} uang anda sekarang ${k}''')
                              inventory2["presiden pack"] = inventory2.get('presiden pack',0) + jbp
                          else:
                              print(f'uang tidak mencukupi ${k}/${ha12}')
                      elif jpp == "10x":
                          sh= ha12 * 10
                          if k >= sh:
                              k -= sh
                              xp += 10
                              print('10X presiden pack dibeli')
                              print(f'''uang -${sh}
  uang sisa ${k}''')
                              inventory2["presiden pack"]=inventory2.get('presiden pack',0) + 10
                      elif jpp == "1x":
                          if k >= ha12:
                              k -= ha12
                              xp += 1
                              print(f'uang -${ha12} uang sisa ${k} +1 presiden pack')
                              inventory2["presiden pack"] = inventory2.get("presiden pack", 0) + 1
                          else:
                              print(f'uang anda tidak mencukupi ${k}/${ha12}')
                  else:
                      print(f'level tidak mencukupi level {lvl}/{SA}')
                    
        elif shop == "potion":
          while True:
              b=input('continue? (y/n)')
              if b=="n":
                break
              else:
                if lvl > 6:
                  potion=input('''|luck boost|exp boost|money boost|'''.lower())
                  if potion == "luck boost":
                      if lvl > 6:
                        print(f'''
${lbt1}:1. luck boost T1
${lbt2}:2. luck boost T2'''.title())
                        
                      elif lvl > 12:
                        print(f'''
${lbt1}:1. luck boost T1
${lbt2}:2. luck boost T2
${lbt3}:3. luck boost T3
${lbt4}:4. luck boost T4'''.title())
                      elif lvl > 18:
                        print(f'''
${lbt1}:1. luck boost T1
${lbt2}:2. luck boost T2
${lbt3}:3. luck boost T3
${lbt4}:4. luck boost T4
${lbt5}:5. luck boost T5
${lbt6}:6. luck boost T6'''.title())
                      lbv=input('''mau beli yang mana?
'''.lower())
                      if lbv == "luck boost t1" or lbv == "1":
                          if 6 < lvl < 1000:
                              if k >= lbt1:
                                  time.sleep(1)
                                  print('luck boost T1 berhasil dibeli!')
                                  k -= lbt1
                                  xp += 1
                                  print(f'''uang - ${lbt1}
uang kamu sekarang ${k}''')
                                  inventory3["luck boost T1"]=inventory3.get("luck boost T1",0)+1
                              else:
                                  print(f'uang tidak mencukupi ${k}/${lbt1}')
                          else:
                              print(f'level tidak mencukupi {lvl}/{A}')
                      elif lbv == "luck boost t2" or lbv == "2":
                          if 6 < lvl < 13:
                              if k >= lbt2:
                                  time.sleep(1)
                                  print('luck boost T2 berhasil dibeli!')
                                  k -= lbt2
                                  xp += 1
                                  print(f'''uang - ${lbt2}
uang kamu sekarang ${k}''') 
                                  inventory3["luck boost T2"]=inventory3.get("luck boost T2",0) + 1
                              else:
                                  print(f'uang tidak mencukupi ${k}/${lbt2}')
                          else:
                              print(f'level tidak mencukupi {lvl}/{A}')
                      elif lbv == "luck boost t3" or lbv == "3":
                          if 13 < lvl <19:
                              if k >= lbt3:
                                  time.sleep(1)
                                  print('luck boost T3 berhasil dibeli!')
                                  k -= lbt3
                                  xp += 1
                                  print(f'''uang - ${lbt3}
uang kamu sekarang ${k}''') 
                                  inventory3["luck boost T3"]=inventory3.get("luck boost T3",0) + 1
                              else:
                                  print(f'uang tidak mencukupi ${k}/${lbt3}')
                          else:
                              print(f'level tidak mencukupi {lvl}/{S}')
                      elif lbv == "luck boost t4" or lbv == "4":
                          if 13 < lvl <19:
                              if k >= lbt4:
                                  time.sleep(1)
                                  print('luck boost T4 berhasil dibeli!')
                                  k -= lbt4
                                  xp += 1
                                  print(f'''uang - ${lbt4}
uang kamu sekarang ${k}''') 
                                  inventory3["luck boost T4"]=inventory3.get("luck boost T4",0) + 1
                              else:
                                  print(f'uang tidak mencukupi ${k}/${lbt4}')
                          else:
                              print(f'level tidak mencukupi {lvl}/{S}')
                      elif lbv == "luck boost t5" or lbv == "5":
                          if lvl > 18:
                              if k >= lbt5:
                                  time.sleep(1)
                                  print('luck boost T5 berhasil dibeli!')
                                  k -= lbt5
                                  xp += 1
                                  print(f'''uang -${lbt5}
uang kamu sekarang ${k}''')
                                  inventory3["luck boost T5"]=inventory3.get("luck boost T5",0) + 1
                              else:
                                  print(f'uang tidak mencukupi ${k}/${lbt5}')
                          else:
                              print(f'level tidak mecukupi {lvl}/{SA}')
                      elif lbv == "luck boost t6" or lbv == "6":
                          if lvl > 18:
                              if k >= lbt6:
                                  time.sleep(1)
                                  print('luck boost T6 berhasil dibeli!')
                                  k -= lbt6
                                  xp += 1
                                  print(f'''uang -${lbt6}
uang kamu sekarang ${k}''')
                                  inventory3["luck boost T6"]=inventory3.get("luck boost T6",0) + 1
                              else:
                                  print(f'uang tidak mencukupi ${k}/${lbt6}')
                          else:
                              print(f'level tidak mecukupi {lvl}/{SA}')
                else:
                    time.sleep(0.5)
                    print(f'''terkunci
level anda tidak mencukupi :lvl {lvl}/5''')
                    break
          
    elif qw == "inventory":
        inv=input('|pack|card|potion|artifact|')
        if inv == "pack":
            for np,j in inventory2.items():
                if j > 0:
                    print(f'{np} : {j}X')
            i=input('|back|open|')
            if i == "back":
                continue
            elif i == "open":
                bp = input('''yang mana?
''')
                if bp == "koruptor pack":
                    if inventory2.get("koruptor pack",0)>0:
                        jbp = input('|1X|10X|all|')
                        if jbp == "1x":
                            inventory2["koruptor pack"] -= 1
                            if 1 <= luck <= 25:
                                bs=bl["kp"][luck]
                                h = random.choices(dkp, weights=bs, k=1)
                                hd = h[0]
                                print(f'kamu dapat: {hd}')
                                inventory[hd] = inventory.get(hd, 0) + 1

                                    
                        elif jbp == "10x":
                            if inventory2.get("koruptor pack",0)>=10:
                                rh={}
                                for _ in range(10):
                                    if 1 <= luck <= 25:
                                        bs=bl["kp"][luck]
                                        h = random.choices(dkp, weights=bs, k=1)
                                        hd = h[0]
                                        rh[hd]=rh.get(hd,0)+1
                                        inventory[hd] = inventory.get(hd, 0) + 10
                                        inventory2['koruptor pack']=inventory2.get('koruptor pack',0) - 10
                                for k,j in rh.items():
                                    print(f'{j}X {k}')
                                
                        elif jbp == "all":
                            tp=inventory2.get('koruptor pack',0)
                            if tp >= 0:
                                rh={}
                                while tp >0:
                                    if 1 <= luck <= 25:
                                        bs=bl["kp"][luck]
                                        h=random.choices(dkp,weights=bs,k=1)
                                        hd=h[0]
                                        rh[hd]=rh.get(hd,0)+1
                                        inventory[hd]=inventory.get(hd,0)+1
                                        tp -= 1
                                        inventory2["koruptor pack"]=0 
                                for k,j in rh.items():
                                    time.sleep(0.1)
                                    print(f'{j}X {k}')
                                                
                elif bp == "band pack":
                    if inventory2.get("band pack", 0) > 0:
                        jbp = input('|1X|10X|all|')
                        if jbp == "1x":
                            inventory2["band pack"] -= 1
                            if 1 <= luck <= 25:
                                bs = bl["bp"][luck]
                                h = random.choices(dbp, weights=bs, k=1)
                                hd = h[0]
                                print(f'kamu dapat: {hd}')
                                inventory[hd] = inventory.get(hd, 0) + 1

                        elif jbp == "10x":
                            if inventory2.get("band pack", 0) >= 10:
                                rh = {}
                                for _ in range(10):
                                    if 1 <= luck <= 25:
                                        bs = bl["bp"][luck]
                                        h = random.choices(dbp, weights=bs, k=1)
                                        hd = h[0]
                                        rh[hd] = rh.get(hd, 0) + 1
                                        inventory[hd] = inventory.get(hd, 0) + 1
                                        inventory2['band pack'] = inventory2.get('band pack', 0) - 10
                                for k, j in rh.items():
                                    print(f'{j}X {k}')
                            else:
                                print(f'pack tidak mencukupi')

                        elif jbp == "all":
                            tp = inventory2.get('band pack', 0)
                            if tp > 0:
                                rh = {}
                                while tp > 0:
                                    if 1 <= luck <= 25:
                                        bs = bl["bp"][luck]
                                        h = random.choices(dbp, weights=bs, k=1)
                                        hd = h[0]
                                        rh[hd] = rh.get(hd, 0) + 1
                                        inventory[hd] = inventory.get(hd, 0) + 1
                                        tp -= 1
                                        inventory2["band pack"] = 0 
                                for k, j in rh.items():
                                    time.sleep(0.1)
                                    print(f'{j}X {k}')

                elif bp == "makanan pack":
                    if inventory2.get("makanan pack", 0) > 0:
                        jbp = input('|1X|10X|all|')
                        if jbp == "1x":
                            inventory2["makanan pack"] -= 1
                            if 1 <= luck <= 25:
                                bs = bl["mp"][luck]
                                h = random.choices(dmp, weights=bs, k=1)
                                hd = h[0]
                                print(f'kamu dapat: {hd}')
                                inventory[hd] = inventory.get(hd, 0) + 1

                        elif jbp == "10x":
                            if inventory2.get("makanan pack", 0) >= 10:
                                rh = {}
                                for _ in range(10):
                                    if 1 <= luck <= 25:
                                        bs = bl["mp"][luck]
                                        h = random.choices(dmp, weights=bs, k=1)
                                        hd = h[0]
                                        rh[hd] = rh.get(hd, 0) + 1
                                        inventory[hd] = inventory.get(hd, 0) + 1
                                        inventory2['makanan pack'] = inventory2.get('makanan pack', 0) - 10
                                for k, j in rh.items():
                                    print(f'{j}X {k}')
                            else:
                                print(f'pack tidak mencukupi')

                        elif jbp == "all":
                            tp = inventory2.get('makanan pack', 0)
                            if tp > 0:
                                rh = {}
                                while tp > 0:
                                    if 1 <= luck <= 25:
                                        bs = bl["mp"][luck]
                                        h = random.choices(dmp, weights=bs, k=1)
                                        hd = h[0]
                                        rh[hd] = rh.get(hd, 0) + 1
                                        inventory[hd] = inventory.get(hd, 0) + 1
                                        tp -= 1
                                        inventory2["makanan pack"] = 0 
                                for k, j in rh.items():
                                    time.sleep(0.1)
                                    print(f'{j}X {k}')

                elif bp == "artis pack":
                    if inventory2.get("artis pack", 0) > 0:
                        jbp = input('|1X|10X|all|')
                        if jbp == "1x":
                            inventory2["artis pack"] -= 1
                            if 1 <= luck <= 25:
                                bs = bl["ap"][luck]
                                h = random.choices(dap, weights=bs, k=1)
                                hd = h[0]
                                print(f'kamu dapat: {hd}')
                                inventory[hd] = inventory.get(hd, 0) + 1

                        elif jbp == "10x":
                            if inventory2.get("artis pack", 0) >= 10:
                                rh = {}
                                for _ in range(10):
                                    if 1 <= luck <= 25:
                                        bs = bl["ap"][luck]
                                        h = random.choices(dap, weights=bs, k=1)
                                        hd = h[0]
                                        rh[hd] = rh.get(hd, 0) + 1
                                        inventory[hd] = inventory.get(hd, 0) + 1
                                inventory2['artis pack'] = inventory2.get('artis pack', 0) - 10
                                for k, j in rh.items():
                                    print(f'{j}X {k}')
                            else:
                                print(f'pack tidak mencukupi')

                        elif jbp == "all":
                            tp = inventory2.get('artis pack', 0)
                            if tp > 0:
                                rh = {}
                                while tp > 0:
                                    if 1 <= luck <= 25:
                                        bs = bl["ap"][luck]
                                        h = random.choices(dap, weights=bs, k=1)
                                        hd = h[0]
                                        rh[hd] = rh.get(hd, 0) + 1
                                        inventory[hd] = inventory.get(hd, 0) + 1
                                    tp -= 1
                                inventory2["artis pack"] = 0 
                                for k, j in rh.items():
                                    time.sleep(0.1)
                                    print(f'{j}X {k}')

                elif bp == "senjata pack":
                    if inventory2.get("senjata pack", 0) > 0:
                        jbp = input('|1X|10X|all|')
                        if jbp == "1x":
                            inventory2["senjata pack"] -= 1
                            if 1 <= luck <= 25:
                                bs = bl["sp"][luck]
                                h = random.choices(dsp, weights=bs, k=1)
                                hd = h[0]
                                print(f'kamu dapat: {hd}')
                                inventory[hd] = inventory.get(hd, 0) + 1

                        elif jbp == "10x":
                            if inventory2.get("senjata pack", 0) >= 10:
                                rh = {}
                                for _ in range(10):
                                    if 1 <= luck <= 25:
                                        bs = bl["sp"][luck]
                                        h = random.choices(dsp, weights=bs, k=1)
                                        hd = h[0]
                                        rh[hd] = rh.get(hd, 0) + 1
                                        inventory[hd] = inventory.get(hd, 0) + 1
                                inventory2['senjata pack'] = inventory2.get('senjata pack', 0) - 10
                                for k, j in rh.items():
                                    print(f'{j}X {k}')
                            else:
                                print(f'pack tidak mencukupi')

                        elif jbp == "all":
                            tp = inventory2.get('senjata pack', 0)
                            if tp > 0:
                                rh = {}
                                while tp > 0:
                                    if 1 <= luck <= 15:
                                        bs = bl["sp"][luck]
                                        h = random.choices(dsp, weights=bs, k=1)
                                        hd = h[0]
                                        rh[hd] = rh.get(hd, 0) + 1
                                        inventory[hd] = inventory.get(hd, 0) + 1
                                    tp -= 1
                                inventory2["senjata pack"] = 0 
                                for k, j in rh.items():
                                    time.sleep(0.1)
                                    print(f'{j}X {k}')

                elif bp == "marapthon pack":
                    if inventory2.get("marapthon pack", 0) > 0:
                        jbp = input('|1X|10X|all|')
                        if jbp == "1x":
                            inventory2["marapthon pack"] -= 1
                            if 1 <= luck <= 25:
                                bs = bl["sp"][luck]
                                h = random.choices(dmrp, weights=bs, k=1)
                                hd = h[0]
                                print(f'kamu dapat: {hd}')
                                inventory[hd] = inventory.get(hd, 0) + 1

                        elif jbp == "10x":
                            if inventory2.get("marapthon pack", 0) >= 10:
                                rh = {}
                                for _ in range(10):
                                    if 1 <= luck <= 25:
                                        bs = bl["sp"][luck]
                                        h = random.choices(dmrp, weights=bs, k=1)
                                        hd = h[0]
                                        rh[hd] = rh.get(hd, 0) + 1
                                        inventory[hd] = inventory.get(hd, 0) + 1
                                inventory2['marapthon pack'] = inventory2.get('marapthon pack', 0) - 10
                                for k, j in rh.items():
                                    print(f'{j}X {k}')
                            else:
                                print(f'pack tidak mencukupi')

                        elif jbp == "all":
                            tp = inventory2.get('marapthon pack', 0)
                            if tp > 0:
                                rh = {}
                                while tp > 0:
                                    if 1 <= luck <= 25:
                                        bs = bl["sp"][luck]
                                        h = random.choices(dmrp, weights=bs, k=1)
                                        hd = h[0]
                                        rh[hd] = rh.get(hd, 0) + 1
                                        inventory[hd] = inventory.get(hd, 0) + 1
                                    tp -= 1
                                inventory2["marapthon pack"] = 0 
                                for k, j in rh.items():
                                    time.sleep(0.1)
                                    print(f'{j}X {k}')
                                                            
                elif bp == "hantu pack":
                    if inventory2.get("hantu pack", 0) > 0:
                        jbp = input('|1X|10X|all|')
                        if jbp == "1x":
                            inventory2["hantu pack"] -= 1
                            if 1 <= luck <= 25:
                                bs = bl["tp"][luck]
                                h = random.choices(dhp, weights=bs, k=1)
                                hd = h[0]
                                print(f'kamu dapat: {hd}')
                                inventory[hd] = inventory.get(hd, 0) + 1

                        elif jbp == "10x":
                            if inventory2.get("hantu pack", 0) >= 10:
                                rh = {}
                                for _ in range(10):
                                    if 1 <= luck <= 25:
                                        bs = bl["tp"][luck]
                                        h = random.choices(dhp, weights=bs, k=1)
                                        hd = h[0]
                                        rh[hd] = rh.get(hd, 0) + 1
                                        inventory[hd] = inventory.get(hd, 0) + 1
                                inventory2['hantu pack'] = inventory2.get('hantu pack', 0) - 10
                                for k, j in rh.items():
                                    print(f'{j}X {k}')
                            else:
                                print(f'pack tidak mencukupi')

                        elif jbp == "all":
                            tp_count = inventory2.get('hantu pack', 0)
                            if tp_count > 0:
                                rh = {}
                                while tp_count > 0:
                                    if 1 <= luck <= 25:
                                        bs = bl["tp"][luck]
                                        h = random.choices(dhp, weights=bs, k=1)
                                        hd = h[0]
                                        rh[hd] = rh.get(hd, 0) + 1
                                        inventory[hd] = inventory.get(hd, 0) + 1
                                    tp_count -= 1
                                inventory2["hantu pack"] = 0 
                                for k, j in rh.items():
                                    time.sleep(0.1)
                                    print(f'{j}X {k}')


                elif bp == "9 naga pack":
                    if inventory2.get("9 naga pack", 0) > 0:
                        jbp = input('|1X|10X|all|')
                        if jbp == "1x":
                            inventory2["9 naga pack"] -= 1
                            if 1 <= luck <= 25:
                                bs = bl["9p"][luck]
                                h = random.choices(d9p, weights=bs, k=1)
                                hd = h[0]
                                print(f'kamu dapat: {hd}')
                                inventory[hd] = inventory.get(hd, 0) + 1

                        elif jbp == "10x":
                            if inventory2.get("9 naga pack", 0) >= 10:
                                rh = {}
                                for _ in range(10):
                                    if 1 <= luck <= 25:
                                        bs = bl["9p"][luck]
                                        h = random.choices(d9p, weights=bs, k=1)
                                        hd = h[0]
                                        rh[hd] = rh.get(hd, 0) + 1
                                        inventory[hd] = inventory.get(hd, 0) + 1
                                inventory2['9 naga pack'] = inventory2.get('9 naga pack', 0) - 10
                                for k, j in rh.items():
                                    print(f'{j}X {k}')
                            else:
                                print(f'pack tidak mencukupi')

                        elif jbp == "all":
                            p9p_count = inventory2.get('9 naga pack', 0)
                            if p9p_count > 0:
                                rh = {}
                                while p9p_count > 0:
                                    if 1 <= luck <= 25:
                                        bs = bl["9p"][luck]
                                        h = random.choices(d9p, weights=bs, k=1)
                                        hd = h[0]
                                        rh[hd] = rh.get(hd, 0) + 1
                                        inventory[hd] = inventory.get(hd, 0) + 1
                                    p9p_count -= 1
                                inventory2["9 naga pack"] = 0 
                                for k, j in rh.items():
                                    time.sleep(0.1)
                                    print(f'{j}X {k}')


                elif bp == "mahal pack":
                    if inventory2.get("mahal pack", 0) > 0:
                        jbp = input('|1X|10X|all|')
                        if jbp == "1x":
                            inventory2["mahal pack"] -= 1
                            if 1 <= luck <= 25:
                                bs = bl["tp"][luck]
                                h = random.choices(dmhp, weights=bs, k=1)
                                hd = h[0]  
                                print(f'kamu dapat: {hd}')
                                inventory[hd] = inventory.get(hd, 0) + 1

                        elif jbp == "10x":
                            if inventory2.get("mahal pack", 0) >= 10:
                                rh = {}
                                for _ in range(10):
                                    if 1 <= luck <= 25:
                                        bs = bl["tp"][luck]
                                        h = random.choices(dmhp, weights=bs, k=1)
                                        hd = h[0]  
                                        rh[hd] = rh.get(hd, 0) + 1
                                        inventory[hd] = inventory.get(hd, 0) + 1
                                inventory2['mahal pack'] = inventory2.get('mahal pack', 0) - 10
                                for k, j in rh.items():
                                    print(f'{j}X {k}')
                            else:
                                print(f'pack tidak mencukupi')

                        elif jbp == "all":
                            tp_count = inventory2.get('mahal pack', 0)
                            if tp_count > 0:
                                rh = {}
                                while tp_count > 0:
                                    if 1 <= luck <= 25:
                                        bs = bl["tp"][luck]
                                        h = random.choices(dmhp, weights=bs, k=1)
                                        hd = h[0] 
                                        rh[hd] = rh.get(hd, 0) + 1
                                        inventory[hd] = inventory.get(hd, 0) + 1
                                    tp_count -= 1
                                inventory2["mahal pack"] = 0 
                                for k, j in rh.items():
                                    time.sleep(0.1)
                                    print(f'{j}X {k}')

                elif bp == "A4A clan":
                    if inventory2.get("A4A clan", 0) > 0:
                        jbp = input('|1X|10X|all|')
                        if jbp == "1x":
                            inventory2["A4A clan"] -= 1
                            if 1 <= luck <= 25:
                                bs = bl["4p"][luck]
                                h = random.choices(d4p, weights=bs, k=1)
                                hd = h[0]  
                                print(f'kamu dapat: {hd}')
                                inventory[hd] = inventory.get(hd, 0) + 1

                        elif jbp == "10x":
                            if inventory2.get("A4A clan", 0) >= 10:
                                rh = {}
                                for _ in range(10):
                                    if 1 <= luck <= 25:
                                        bs = bl["4p"][luck]
                                        h = random.choices(d4p, weights=bs, k=1)
                                        hd = h[0] 
                                        rh[hd] = rh.get(hd, 0) + 1
                                        inventory[hd] = inventory.get(hd, 0) + 1
                                inventory2['A4A clan'] = inventory2.get('A4A clan', 0) - 10
                                for k, j in rh.items():
                                    print(f'{j}X {k}')
                            else:
                                print(f'pack tidak mencukupi')

                        elif jbp == "all":
                            tp_count = inventory2.get('A4A clan', 0)
                            if tp_count > 0:
                                rh = {}
                                while tp_count > 0:
                                    if 1 <= luck <= 25:
                                        bs = bl["4p"][luck]
                                        h = random.choices(d4p, weights=bs, k=1)
                                        hd = h[0] 
                                        rh[hd] = rh.get(hd, 0) + 1
                                        inventory[hd] = inventory.get(hd, 0) + 1
                                    tp_count -= 1
                                inventory2["A4A clan"] = 0 
                                for k, j in rh.items():
                                    time.sleep(0.1)
                                    print(f'{j}X {k}')

                elif bp == "pahlawan pack":
                    if inventory2.get("pahlawan pack", 0) > 0:
                        jbp = input('|1X|10X|all|')
                        if jbp == "1x":
                            inventory2["pahlawan pack"] -= 1
                            if 1 <= luck <= 25:
                                bs = bl["pp"][luck]
                                h = random.choices(dpp, weights=bs, k=1)
                                hd = h[0]
                                print(f'kamu dapat: {hd}')
                                inventory[hd] = inventory.get(hd, 0) + 1

                        elif jbp == "10x":
                            if inventory2.get("pahlawan pack", 0) >= 10:
                                rh = {}
                                for _ in range(10):
                                    if 1 <= luck <= 25:
                                        bs = bl["pp"][luck]
                                        h = random.choices(dpp, weights=bs, k=1)
                                        hd = h[0]
                                        rh[hd] = rh.get(hd, 0) + 1
                                        inventory[hd] = inventory.get(hd, 0) + 1
                                inventory2['pahlawan pack'] = inventory2.get('pahlawan pack', 0) - 10
                                for k, j in rh.items():
                                    print(f'{j}X {k}')
                            else:
                                print(f'pack tidak mencukupi')

                        elif jbp == "all":
                            ppp_count = inventory2.get('pahlawan pack', 0)
                            if ppp_count > 0:
                                rh = {}
                                while ppp_count > 0:
                                    if 1 <= luck <= 25:
                                        bs = bl["pp"][luck]
                                        h = random.choices(dpp, weights=bs, k=1)
                                        hd = h[0]
                                        rh[hd] = rh.get(hd, 0) + 1
                                        inventory[hd] = inventory.get(hd, 0) + 1
                                    ppp_count -= 1
                                inventory2["pahlawan pack"] = 0 
                                for k, j in rh.items():
                                    time.sleep(0.1)
                                    print(f'{j}X {k}')

                elif bp == "presiden pack":
                    if inventory2.get("presiden pack", 0) > 0:
                        jbp = input('|1X|10X|all|')
                        if jbp == "1x":
                            inventory2["presiden pack"] -= 1
                            if 1 <= luck <= 25:
                                bs = bl["rp"][luck]
                                h = random.choices(dprp, weights=bs, k=1)
                                hd = h[0]
                                print(f'kamu dapat: {hd}')
                                inventory[hd] = inventory.get(hd, 0) + 1

                        elif jbp == "10x":
                            if inventory2.get("presiden pack", 0) >= 10:
                                rh = {}
                                for _ in range(10):
                                    if 1 <= luck <= 25:
                                        bs = bl["rp"][luck]
                                        h = random.choices(dprp, weights=bs, k=1)
                                        hd = h[0]
                                        rh[hd] = rh.get(hd, 0) + 1
                                        inventory[hd] = inventory.get(hd, 0) + 1
                                inventory2['presiden pack'] = inventory2.get('presiden pack', 0) - 10
                                for k, j in rh.items():
                                    print(f'{j}X {k}')
                            else:
                                print(f'pack tidak mencukupi')

                        elif jbp == "all":
                            tp_count = inventory2.get('presiden pack', 0)
                            if tp_count > 0:
                                rh = {}
                                while tp_count > 0:
                                    if 1 <= luck <= 25:
                                        bs = bl["rp"][luck]
                                        h = random.choices(dprp, weights=bs, k=1)
                                        hd = h[0]
                                        rh[hd] = rh.get(hd, 0) + 1
                                        inventory[hd] = inventory.get(hd, 0) + 1
                                    tp_count -= 1
                                inventory2["presiden pack"] = 0 
                                for k, j in rh.items():
                                    time.sleep(0.1)
                                    print(f'{j}X {k}')


