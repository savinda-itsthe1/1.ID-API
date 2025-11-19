from app.models import GuestAttachment
from app import db

def get_guestattachment_data():
    try:
        # Query the GuestAttachment table
        guestattachments = GuestAttachment.query.all()

        # Convert the result to a list of dictionaries
        result = [
            {
                'Id': guestattachment.Id,
                'ExpiryDate': guestattachment.ExpiryDate.isoformat() if guestattachment.ExpiryDate else None,
                'IssueDate': guestattachment.IssueDate.isoformat() if guestattachment.IssueDate else None,
                'AttachmentInfoListJson': guestattachment.AttachmentInfoListJson,
                'DocumentTypeId': guestattachment.DocumentTypeId,
                'IssueCountryId': guestattachment.IssueCountryId,
                'GuestId': guestattachment.GuestId,
            }
            for guestattachment in guestattachments
        ]

        return result

    except Exception as e:
        return {"error": str(e)}