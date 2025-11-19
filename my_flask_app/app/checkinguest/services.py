from app.models import CheckinGuest
from app import db

def get_checkinguest_data():
    try:
        # Query the CheckinGuest table
        checkinguests = CheckinGuest.query.all()

        # Convert the result to a list of dictionaries
        result = [
            {
                'Id': checkinguest.Id,
                'CheckinDate': checkinguest.CheckinDate.isoformat() if checkinguest.CheckinDate else None,
                'IsMainGuest': checkinguest.IsMainGuest,
                'GuestCode': checkinguest.GuestCode,
                'GuestUID': checkinguest.GuestUID,
                'CheckoutDate': checkinguest.CheckoutDate.isoformat() if checkinguest.CheckoutDate else None,
                'IsFirstGuest': checkinguest.IsFirstGuest,
                'GuestId': checkinguest.GuestId,
                'CheckinId': checkinguest.CheckinId,
                'RelationshipName': checkinguest.RelationshipName,
                'EscortTypeId': checkinguest.EscortTypeId,
                'VisitPurposeId': checkinguest.VisitPurposeId,
            }
            for checkinguest in checkinguests
        ]

        return result

    except Exception as e:
        return {"error": str(e)}