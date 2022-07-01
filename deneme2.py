from enum import Enum


class ModelName(str, Enum):
    RandomForest = "RF"
    XGB = "XGB"
    LGBM = "LGBM"
    HGBR = "HGBR"

def x(chosen_item : ModelName):

    info_dict = {
        "XGB" : ModelName.XGB,
        "LGBM" : ModelName.LGBM
    }
    return info_dict.get(chosen_item, "Mothing selected!")


isimler = ["alper", "Olha"]
numaralar = [1,2]

# eğer zip kullandıysan liste constructor ile unzip te yapılıyor!
a = list(zip(isimler, numaralar))
print("Hey :",a)
isimler2, numarala2 =zip(*a)
print("Hoy :", [isimler2], [numarala2])


