from app.models import Log
from app import db

def get_log_data():
    try:
        # Query the Guest table
        logs = Log.query.all()

        # Convert the result to a list of dictionaries
        result = [
            {
                'Id': log.Id,
                'AddedAt': log.AddedAt,
                'RoomNumber': log.RoomNumber,
                'RequestType': log.RequestType,
                'DtcmStatus': log.DtcmStatus,
                'CidStatus': log.CidStatus,
                'CheckinUID': log.CheckinUID,
                'PayloadIdentifier': log.PayloadIdentifier,
                'Error': log.Error,
                'CheckinGuestId': log.CheckinGuestId,
                'CheckinId': log.CheckinId,
                
            }
            for log in logs
        ]

        return result

    except Exception as e:
        return {"error": str(e)}