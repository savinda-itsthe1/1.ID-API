from app.models import Room
from app import db

def get_room_data():
    try:
        # Query the Guest table
        rooms = Room.query.all()

        # Convert the result to a list of dictionaries
        result = [
            {
                'Id': room.Id,
                'RoomNumber': room.RoomNumber,
                'BedCount': room.BedCount,
                'IsChecked': room.IsChecked,
                'CheckinId': room.CheckinId,
                'IsWaitingRoom': room.IsWaitingRoom,
                'IsActive': room.IsActive,
                
            }
            for room in rooms
        ]

        return result

    except Exception as e:
        return {"error": str(e)}