from app.models import GuestDocumentImage
from app import db

def get_guestdocumentimage_data():
    try:
        # Query the Guest table
        guestdocumentimages = GuestDocumentImage.query.all()

        # Convert the result to a list of dictionaries
        result = [
            {
                'DocumentId': guestdocumentimage.DocumentId,
                'GuestId': guestdocumentimage.GuestId,
                'DocumentUID': guestdocumentimage.DocumentUID,
                'AttachmentCode': guestdocumentimage.AttachmentCode,
                'FileName': guestdocumentimage.FileName,
                'FileSizeKB': guestdocumentimage.FileSizeKB,
                'ImageData': guestdocumentimage.ImageData,
                'UploadedAt': guestdocumentimage.UploadedAt,
            }
            for guestdocumentimage in guestdocumentimages
        ]

        return result

    except Exception as e:
        return {"error": str(e)}