class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

class Singa(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, cakar, mengaum):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.cakar = cakar
        self.mengaum = mengaum

    def berburu(self):
        print(f"Singa Sedang Berburu Menggunakan", self.cakar ,"dan langsung", self.mengaum)
    

Singa = Singa("Singa", "Daging", "hidup", "Beranak", "Cakar", "Mengaum")
Singa.berburu()

