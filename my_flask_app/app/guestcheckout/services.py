from app.models import CheckinGuest
from app import db

def get_guestcheckout_data():
    try:
        # Query the Checkout table
        guestcheckouts = CheckinGuest.query.all()

        # Convert the result to a list of dictionaries
        result = [
            {
                'Id': guestcheckout.Id,
                'CheckinDate': guestcheckout.CheckinDate.isoformat() if guestcheckout.CheckinDate else None,
                'IsMainGuest': guestcheckout.IsMainGuest,
                'GuestCode': guestcheckout.GuestCode,
                'GuestUID': guestcheckout.GuestUID,
                'CheckoutDate': guestcheckout.CheckoutDate.isoformat() if guestcheckout.CheckoutDate else None,
                'IsFirstGuest': guestcheckout.IsFirstGuest,
                'GuestId': guestcheckout.GuestId,
                'CheckinId': guestcheckout.CheckinId,
                'RelationshipName': guestcheckout.RelationshipName,
                'EscortTypeId': guestcheckout.EscortTypeId,
                'VisitPurposeId': guestcheckout.VisitPurposeId,
            }
            for guestcheckout in guestcheckouts
        ]

        return result

    except Exception as e:
        return {"error": str(e)}