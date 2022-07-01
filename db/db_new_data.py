from db.models import New_UTS_Data
from schemas import CompRequest_New_data
from datetime import datetime, timezone

def get_utc_now_timestamp() -> datetime:
    return datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(tz=None)


def insert_new_uts_data(request : CompRequest_New_data, db):

    new_uts_data = New_UTS_Data(
        date= request.created_date,
        NT=request.NT,
        QT=request.QT,
        TT=request.TT,
        carbon=request.carbon,
        silicon=request.silicon,
        manganese=request.manganese,
        phosphorus=request.phosphorus,
        sulphur=request.sulphur,
        nickel=request.nickel,
        chromium=request.chromium,
        copper=request.copper,
        molybdenum=request.molybdenum
    )
    db.add(new_uts_data)
    db.commit()
    db.refresh(new_uts_data)
    return new_uts_data



