from app.models import Checkin
from app import db

def get_checkin_data():
    try:
        # Query the Checkin table
        checkins = Checkin.query.all()

        # Convert the result to a list of dictionaries
        result = [
            {
                'Id': checkin.Id,
                'CheckinUID': checkin.CheckinUID,
                'RoomNumber': checkin.RoomNumber,
                'CheckinDate': checkin.CheckinDate.isoformat() if checkin.CheckinDate else None,
                'IsActive': checkin.IsActive,
                'ChargeExtra': checkin.ChargeExtra,
                'IsFeeUpdated': checkin.IsFeeUpdated,
                'TDFee': checkin.TDFee,
                'AddedAt': checkin.AddedAt.isoformat() if checkin.AddedAt else None,
                'AddedFrom': checkin.AddedFrom,
                'CheckinTypeId': checkin.CheckinTypeId,
                'PaymentId': checkin.PaymentId,
                'ChildEscortCount': checkin.ChildEscortCount,
                'AdultEscortCount': checkin.AdultEscortCount,
            }
            for checkin in checkins
        ]

        return result

    except Exception as e:
        return {"error": str(e)}
    


from .validators import (
    is_valid_email, is_valid_string, is_alphanumeric, has_extra_spaces,
    has_more_names, has_arabic_characters_only, is_future_date
)

def validate_guest(guest):
    """Validate guest details."""
    errors = {}

    if not is_valid_string(guest.get("FirstName", "")):
        errors["FirstName"] = "First Name should only contain English letters and spaces."
    elif has_extra_spaces(guest["FirstName"]):
        errors["FirstName"] = "There are multiple spaces in between words."
    # elif has_more_names(guest["FirstName"]):
    #     errors["FirstName"] = "Please enter less than 4 names for the First Name."

    if not is_valid_string(guest.get("LastName", "")):
        errors["LastName"] = "Last Name should only contain English letters and spaces."
    elif has_extra_spaces(guest["LastName"]):
        errors["LastName"] = "There are multiple spaces in between words."
    # elif has_more_names(guest["LastName"]):
    #     errors["LastName"] = "Please enter less than 4 names for the Last Name."

    if not has_arabic_characters_only(guest.get("ArabicName", "")):
        errors["ArabicName"] = "Arabic Name should only contain Arabic characters."

    if guest.get("Email") and not is_valid_email(guest["Email"]):
        errors["Email"] = "The Email Address is Invalid."

    if not is_alphanumeric(guest.get("DocumentNumber", "")):
        errors["DocumentNumber"] = "The document number contains invalid characters or spaces."

    if guest.get("BirthPlace"):
        if " " in guest["BirthPlace"]:
            errors["BirthPlace"] = "Place of Birth cannot contain spaces."
        elif not guest["BirthPlace"].isalpha():
            errors["BirthPlace"] = "Place of Birth can only contain letters."

    if guest.get("Mobile") and not guest["Mobile"].isdigit():
        errors["Mobile"] = "Mobile Number should only contain numeric characters."


    return errors

    