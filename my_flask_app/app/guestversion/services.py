from app.models import GuestVersion
from app import db

def get_guestversion_data():
    try:
        # Query the GuestVersion table
        guestversions = GuestVersion.query.all()

        # Convert the result to a list of dictionaries
        result = [
            {
                
                'FirstName': guestversion.FirstName,
                'LastName': guestversion.LastName,
                'ArabicFirstName': guestversion.ArabicFirstName,
                'ArabicLastName': guestversion.ArabicLastName,
                'Gender': guestversion.Gender,
                'BirthDate': guestversion.BirthDate,
                'ResidenceCountryPhone': guestversion.ResidenceCountryPhone,
                'MobileCode': guestversion.MobileCode,
                'MobileNumber': guestversion.MobileNumber,
                'Email': guestversion.Email,
                'RequiresAccessibilityJson': guestversion.RequiresAccessibilityJson,
                'CheckinId': guestversion.CheckinId,
                'DocumentNumber': guestversion.DocumentNumber,
                'NationalityId': guestversion.NationalityId,
                'EmirateId': guestversion.EmirateId,
                'CheckinDate': guestversion.CheckinDate,
                'CheckoutDate': guestversion.CheckoutDate,
                'IsMainGuest': guestversion.IsMainGuest,
                'GuestCode': guestversion.GuestCode,
                'GuestUID': guestversion.GuestUID,
                'GuestId': guestversion.GuestId,
                'RelationshipId': guestversion.RelationshipId,
                'EscortTypeId': guestversion.EscortTypeId,
                'VisitPurposeId': guestversion.VisitPurposeId,
                'ExpiryDate': guestversion.ExpiryDate,
                'IssueDate': guestversion.IssueDate,
                'DocumentTypeId': guestversion.DocumentTypeId,
                'LogId': guestversion.LogId,
                'CheckinGuestId': guestversion.CheckinGuestId,
                'BirthPlaceName': guestversion.BirthPlaceName,
                'ResidenceCountryTwoCode': guestversion.ResidenceCountryTwoCode,
                'IssueCountryTwoCode': guestversion.IssueCountryTwoCode,
                'AttachmentInfoListJson': guestversion.AttachmentInfoListJson,
                'CurrentMainCheckinGuestId': guestversion.CurrentMainCheckinGuestId,
            }
            for guestversion in guestversions
        ]

        return result

    except Exception as e:
        return {"error": str(e)}
