class Hayvanlar():

    def __init__(self,bacak_sayiyi,solunum_turu,beslenme_tarzi,evcillik,yenilebilirlik):

        self.bacak_sayisi=bacak_sayiyi
        self.solunum_turu=solunum_turu
        self.beslenem_tarzi=beslenme_tarzi
        self.evcillik=evcillik
        self.yenilebilirlik=yenilebilirlik



class Dogs(Hayvanlar):

    def __init__(self,bacak_sayiyi,solunum_turu,beslenme_tarzi,evcillik,yenilebilirlik,hız):

        super.__init__(bacak_sayiyi,solunum_turu,beslenme_tarzi,evcillik,yenilebilirlik)

        self.hız=hız

    def ögren1(self):

        print("Köpeğiniz saatte {} hızla koşabilmektedir.".format(hız))





class Birds(Hayvanlar):

    def __init__(self,bacak_sayiyi,solunum_turu,beslenme_tarzi,evcillik,yenilebilirlik,yükseklik):

        super.__init__(bacak_sayiyi,solunum_turu,beslenme_tarzi,evcillik,yenilebilirlik)

        self.yükseklik=yükseklik






class Fishes(Hayvanlar):

    def __init__(self,bacak_sayiyi,solunum_turu,beslenme_tarzi,evcillik,yenilebilirlik,yüzgeç):

        super.__init__(bacak_sayiyi,solunum_turu,beslenme_tarzi,evcillik,yenilebilirlik)

        self.yüzgeç=yüzgeç


kopek1=Dogs(4,"Akciğer","Etçil","Evet","Hayır",40)
print(kopek1.yenilebilirlik)

