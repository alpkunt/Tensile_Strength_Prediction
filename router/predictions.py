from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import CompositionRequest, UserBase
from db.database import get_db
from db import db_predictions

from enum import Enum
from auth.oauth2 import get_current_user

class ModelName(str, Enum):
    RandomForest = "RF"
    XGB = "XGB"
    LGBM = "LGBM"
    HGBR = "HGBR"
    PALA = "123"


router = APIRouter(
    prefix='/predictions',
    tags=['prediction models']
)


# @router.get("/chose_model/{model_name}")
# async def chose_model_and_predict(model_name: ModelName):
#     if model_name == ModelName.RandomForest:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
#     if model_name == ModelName.XGB:
#         return {"model_name": model_name, "message": "XGB FTW!"}
#     if model_name == ModelName.LGBM:
#         return {"model_name": model_name, "message": "LGBM FTW!"}
#     if model_name == ModelName.HGBR:
#         return {"model_name": model_name, "message": "HGBR FTW!"}
#

# model arttıkça if else sıkıntı bir dictionary oluştur,
# sonra bunu başka bir yerden çağırırsın! Cool olur! Ayrıca başka yeri güncellediğinde otomatik burasıda güncellenir
# very cool olur!

@router.post("/dictionary_selection/{model_name}")
async def chose_model_and_predict(model_name: ModelName,
                                  request: CompositionRequest,
                                  db: Session = Depends(get_db),
                                  current_user: UserBase = Depends(get_current_user)):
    info_dict = {
        "XGB": ModelName.XGB,  # buraya direk modelin tahmin sonucunu getirebilirim! Veri tabanına gitmeden!
        "LGBM": ModelName.LGBM,
        "HGBR": ModelName.HGBR,
        "RF": ModelName.RandomForest
    }
    # direk fonkisyonu call ettim! güzel oldu!

    chosen_model = info_dict.get(model_name, "Nothing selected!")

    return db_predictions.prediction_by_composition(chosen_model, request, db, current_user)

# birde class deneyelim!
