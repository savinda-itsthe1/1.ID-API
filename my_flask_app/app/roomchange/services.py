from app.models import RoomChange
from app import db

def get_roomchange_data():
    try:
        # Query the RoomChange table
        roomchanges = RoomChange.query.all()

        # Convert the result to a list of dictionaries
        result = [
            {
                'Id': roomchange.Id,
                'FromRoomNumber': roomchange.FromRoomNumber,
                'ToRoomNumber': roomchange.ToRoomNumber,
                'CheckinId': roomchange.CheckinId,
                'EffectiveDateTime': roomchange.EffectiveDateTime.isoformat() if roomchange.EffectiveDateTime else None,
                'AddedAt': roomchange.AddedAt.isoformat() if roomchange.AddedAt else None,
                'AddedFrom': roomchange.AddedFrom,
                'LogId': roomchange.LogId,
            }
            for roomchange in roomchanges
        ]

        return result

    except Exception as e:
        return {"error": str(e)}