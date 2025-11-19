from app.models import MainGuestChange
from app import db

def get_mainguestchange_data():
    try:
        # Query the Guest table
        mainguestchanges = MainGuestChange.query.all()

        # Convert the result to a list of dictionaries
        result = [
            {
                'Id': mainguestchange.Id,
                'FormerMainCheckinGuestId': mainguestchange.FormerMainCheckinGuestId,
                'NewMainCheckinGuestId': mainguestchange.NewMainCheckinGuestId,
                'CheckinId': mainguestchange.CheckinId,
                'EffectiveDateTime': mainguestchange.EffectiveDateTime,
                'AddedAt': mainguestchange.AddedAt,
                'AddedFrom': mainguestchange.AddedFrom,
                'LogId': mainguestchange.LogId,
                
            }
            for mainguestchange in mainguestchanges
        ]

        return result

    except Exception as e:
        return {"error": str(e)}