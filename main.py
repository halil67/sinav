import random
import pandas as pd
import numpy as np

female_names = [
    "Emma", "Olivia", "Ava", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia",
    "Harper", "Evelyn", "Abigail", "Emily", "Elizabeth", "Sofia", "Avery", "Ella",
    "Scarlett", "Grace", "Chloe", "Victoria", "Aria", "Lily", "Luna", "Zoe",
    "Hannah", "Madison", "Riley", "Eleanor", "Ellie", "Penelope", "Layla", "Nora",
    "Hazel", "Aubrey", "Camila", "Aurora", "Violet", "Nova", "Zara", "Stella",
    "Maya", "Lucy", "Savannah", "Audrey", "Brooklyn", "Bella", "Claire", "Skylar",
    "Leah", "Samantha", "Liam", "Grace", "Zoey", "Aaliyah", "Ellie", "Paisley",
    "Hailey", "Elena", "Natalie", "Liliana", "Faith", "Gabriella", "Addison"
]
last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
    "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
    "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Adams",
    "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts",
    "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz", "Edwards",
    "Collins", "Reyes", "Stewart", "Morris"
]
male_names = [
    "Liam", "Noah", "Ethan", "Oliver", "Aiden", "Muhammad", "Arjun", "Elijah",
    "William", "James", "Benjamin", "Lucas", "Mason", "Alexander", "Logan", "Daniel",
    "Michael", "Henry", "Jackson", "Sebastian", "Joseph", "David", "Matthew", "Samuel",
    "Carter", "Jayden", "John", "Owen", "Dylan", "Luke", "Gabriel", "Jack", "Nathan",
    "Isaac", "Eli", "Levi", "Andrew", "Ryan", "Anthony", "Christopher", "Charles",
    "Thomas", "Joshua", "Christian", "Hunter", "Connor", "Jonathan", "Aaron", "Caleb",
    "Ethan", "Nicholas", "Cameron", "Wyatt", "Jordan", "Jeremiah", "Colton", "Xavier",
    "Adrian", "Henry", "Leo"
]

def isim(cns):
    if cns=="E":
        return random.choice(male_names)
    if cns.upper()=="K":
        return random.choice(female_names)
def soyisim():
    return random.choice(last_names)

def tahmin(ssay):
    return random.randint(0,ssay)
ogrenciler={}
ogrenci={}
aln=["Say","Ea","Söz","Dil"]
alna=[30,50,10,10]
df_U=pd.DataFrame()
tercih_df=pd.DataFrame()

def ogrenci_Uret():
    i=0
    mtn,fzn,kmn,byn=0,0,0,0
    edn,tr1n,cg1n=0,0,0
    tr2n,cg2n,flsn,dnkn=0,0,0,0
    diln=0
    td=tahmin(40)
    ty=tahmin(40-td)
    tn=td-ty/4
    md=tahmin(40)
    my=tahmin(40-md)
    mn=md-my/4
    fd=tahmin(20)
    fy=tahmin(20-fd)
    fn=fd-fy/4
    sd=tahmin(20)
    sy=tahmin(20-sd)
    sn=sd-sy/4
    alan=random.choices(aln,weights=alna)[0]
    if alan=="Say":
        mtd=tahmin(40)
        mty=tahmin(40-mtd)
        mtn=mtd-mty/4
        
        fzd=tahmin(14)
        fzy=tahmin(14-fzd)
        fzn=mtd-mty/4
        
        kmd=tahmin(13)
        kmy=tahmin(13-kmd)
        kmn=kmd-kmy/4
        
        byd=tahmin(13)
        byy=tahmin(13-byd)
        byn=byd-byy/4
        
    if alan=="Ea":
        mtd=tahmin(40)
        mty=tahmin(40-mtd)
        mtn=mtd-mty/4
        
        edd=tahmin(24)
        edy=tahmin(24-edd)
        edn=edd-edy/4
        
        tr1d=tahmin(10)
        tr1y=tahmin(10-tr1d)
        tr1n=tr1d-tr1y/4
        
        cg1d=tahmin(6)
        cg1y=tahmin(6-cg1d)
        cg1n=cg1d-cg1y/4
    
    if alan=="Dil":
        dild=tahmin(80)
        dily=tahmin(80-dild)
        diln=dild-dily/4
    
    if alan=="Söz":
        
        edd=tahmin(24)
        edy=tahmin(24-edd)
        edn=edd-edy/4
        
        tr2d=tahmin(11)
        tr2y=tahmin(11-tr2d)
        tr2n=tr2d-tr2y/4
        
        cg2d=tahmin(11)
        cg2y=tahmin(11-cg1d)
        cg2n=cg1d-cg1y/4
        
        flsd=tahmin(12)
        flsy=tahmin(12-flsd)
        flsn=flsd-flsy/4
        
        dnkd=tahmin(6)
        dnky=tahmin(6-dnkd)
        dnkn=dnkd-dnky/4

    c=random.choice("EK")
    ogrenci = {
        "id": 1 + i,
        "sex": c,
        "name": isim(c),
        "surname": soyisim(),
        "Alan":alan,
        "AOB":random.randint(50,100),
        "trkD": td,
        "trkY": ty,
        "trkN": tn,
        "matD": md,
        "matY": my,
        "matN": mn,
        "fenD": fd,
        "fenY": fy,
        "fenN": fn,
        "sosD": sd,
        "sosY": sy,
        "sosN": sn,
        "Mt2N":mtn,
        "Fz2N":fzn,
        "Km2N":kmn,
        "By2N":byn,
        "EdbN":edn,
        "Tr1N":tr1n,
        "Cg1N":cg1n,
        "Tr2N":tr2n,
        "Cg2N":cg2n,
        "FlsN":flsn,
        "DnkN":dnkn,
        "DilN":diln
    }
    ogrenciler[1 + i] = ogrenci

for i in range(0,100000):
    ogrenci_Uret
df=pd.DataFrame(ogrenciler).T
print("Öğrenciler Tanımlandı")

def puan_heapla():
    df["TopN"]=df["trkN"]+df["matN"]+df["fenN"]+df["sosN"]
    df["TyT_Puan"]=df["trkN"]*3.3+df["matN"]*3.3+df["fenN"]*3.4+df["sosN"]*3.4+df["AOB"]*.6+100
    df=df.sort_values(by="TyT_Puan",ascending=False)
    df["Tyt_Sıra"] = range(1, len(df) + 1)
    print("Tyt Hesaplandı")
    tytp=df["trkN"]*1.32+df["matN"]*1.32+df["fenN"]*1.36+df["sosN"]*1.36+100+df["AOB"]*.6
    df["AYT_Say_Puan"]=tytp+df["Mt2N"]*3+df["Fz2N"]*2.85+df["By2N"]*3.07+df["Km2N"]*3.02
    df=df.sort_values(by="AYT_Say_Puan",ascending=False)
    df["AYT_Say_Sıra"] = range(1, len(df) + 1)
    print("Ayt Sayısal Hesaplandı")
    df["AYT_EA_Puan"]=tytp+df["Mt2N"]*3 + df["EdbN"]*3 +df["Tr1N"]*2.8+df["Cg1N"]*3.33
    df=df.sort_values(by="AYT_EA_Puan",ascending=False)
    df["AYT_EA_Sıra"] = range(1, len(df) + 1)
    print("Ayt EA Hesaplandı")
    df["AYT_Söz_Puan"]=tytp+df["EdbN"]*3+df["Tr1N"]*2.8+df["Cg1N"]*3.33+df["Tr2N"]*2.91+df["Cg2N"]*2.91+df["FlsN"]*3+ df["DnkN"]*3.3
    df=df.sort_values(by="AYT_Söz_Puan",ascending=False)
    df["AYT_Söz_Sıra"] = range(1, len(df) + 1)
    print("Ayt Söz Hesaplandı")
    
    df["AYT_Dil_Puan"]=tytp+df["DilN"]*3
    df=df.sort_values(by="AYT_Dil_Puan",ascending=False)
    df["AYT_Dil_Sıra"] = range(1, len(df) + 1)
    print("Ayt Dil  Hesaplandı")
    df.to_csv('ogrenci.csv', index=False)
    print("Dosya Kaydedildi")

puan_heapla()

def Tablo4_oku():
    df_U=pd.read_csv("Tablo4.csv",encoding="utf-8",sep=';')
    df_U["B.SIRASI"]=df_U["B.SIRASI"].replace("...",0)
    df_U["B.SIRASI"]=df_U["B.SIRASI"].fillna(0)
    df_U[df_U["B.SIRASI"]==np.NaN]
    df_U["B.SIRASI"]=df_U["B.SIRASI"].astype("f")
    df_U.sort_values(by="B.SIRASI",ascending=True)

Tablo4_oku()
def tercih_olustur():
    a=df[["id","Alan","Tyt_Sıra","AYT_Say_Sıra","AYT_EA_Sıra","AYT_Söz_Sıra","AYT_Dil_Sıra"]].values.tolist()
    c=0
    tercih_df = pd.DataFrame()
    for i in a:
        id=i[0]
        alan=i[1]
        tyt_sira=i[2]
        AYT_Say_Sıra=i[3]
        AYT_EA_Sıra=i[4]
        AYT_Söz_Sıra=i[5]
        AYT_Dil_Sıra=i[6]
        if alan=="Dil":
            bs=AYT_Dil_Sıra
        elif alan=="Söz":
            bs=AYT_Söz_Sıra
        elif alan=="Ea":
            bs=AYT_EA_Sıra
        else:
            bs=AYT_Say_Sıra
            
        if bs <=800: bs=800
        alt=bs*.9
        ust=bs*1.10
        if bs<=800:
            alt=1
            ust=bs
        
        b = df_U[(df_U["PAUNtÜRÜ"]==alan.upper())  & ((df_U["B.SIRASI"] >= alt) & (df_U["B.SIRASI"]<=ust))]
        #print(len(b),alt,ust,alan)
        if len(b)>0:
            if len(b)<24:
                n=len(b)
            else:
                n=random.randint(5,24)
            
            tercihler=b.sample(n)
            tercihler['Student_ID'] = id
            tercihler['Student_Alan'] = alan.upper()
            if alan=="Dil":
                tercihler['Sıra']=AYT_Dil_Sıra
            elif alan=="Söz":
                tercihler['Sıra']=AYT_Söz_Sıra
            elif alan=="Ea":
                tercihler['Sıra']=AYT_EA_Sıra
            else:
                tercihler['Sıra']=AYT_Say_Sıra
                
            tercihler["Tercih_Sıra"]=range(1,len(tercihler)+1)
                                    
            tercih_df = pd.concat([tercih_df, tercihler], ignore_index=True)
            
    tercih_df.to_csv(f'tercih.csv', index=False,sep=";")
    tercih_df= tercih_df.sort_values(by=["Tercih_Sıra","KODU","B.SIRASI"],ascending=True)
    tercih_df

tercih_olustur()
#tercih_df=tercih_df.sort_values(by=["Sıra","Tercih_Sıra"])
#boşlukları düzelt
tercih_df=tercih_df.reset_index(drop=True)
tercih_df=tercih_df.drop(index=range(64827,len(tercih_df)))
tercih_df
#hataları düzelt
tercih_df["durum"]=""
tercih_df["sayı"]=0
df_t=tercih_df.copy()

print(df_t["KODU"].isna().count())
df_t["KODU"]=df_t["KODU"].astype("string")
df_t["KODU"]=df_t["KODU"].str.replace(".0","")
df_t["KODU"].fillna(0)
df_t["KONT"]=df_t["KONT"].replace(" ","")
df_t["KONT"]=df_t["KONT"].astype("string")
def tercih_Yap():
    kodlar = df_t["KODU"].unique()
    for kod in kodlar:
        trc = df_t[df_t["KODU"] == kod]
        
        if len(trc)>0:
            kont=int(trc.iloc[0,8])
            unv=trc.iloc[0,1]
            bolum=trc.iloc[0,5]
            
        if kont==0:
            print(trc)
        trc=trc.head(kont+1)
        
        trc_indexes = trc.index
        yer=0
        for j, index in enumerate(trc_indexes):
            
            if j<int(kont):
                student_id = trc.loc[index, "Student_ID"]
                df_t.loc[(df_t["KODU"] == kod) & (df_t["Student_ID"] == student_id), "durum"] = "Yerleşti"
                df_t.loc[(df_t["KODU"] == kod) & (df_t["Student_ID"] == student_id), "sayı"] = j + 1
                rows_to_drop = df_t[(df_t["Student_ID"] == student_id) & (df_t["durum"] != "Yerleşti")].index
                df_t = df_t.drop(index=rows_to_drop)
                yer=j
                
            else:
                yer=j
                break
        print(f"Bölüm Kodu:{kod},{unv.strip()},{bolum.strip()}\nBaşvuru Sayısı:{len(trc)},Kontenjan:{kont},Yerleşen:{yer}")
        
    print(df_t)

tercih_Yap()
