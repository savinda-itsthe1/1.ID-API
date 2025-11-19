from app.models import Checkout
from app import db

def get_checkout_data():
    try:
        # Query the Checkout table
        checkouts = Checkout.query.all()

        # Convert the result to a list of dictionaries
        result = [
            {
                'Id': checkout.Id,
                'CheckoutDate': checkout.CheckoutDate.isoformat() if checkout.CheckoutDate else None,
                'ChargeExtra': checkout.ChargeExtra,
                'AddedAt': checkout.AddedAt.isoformat() if checkout.AddedAt else None,
                'AddedFrom': checkout.AddedFrom,
                'CheckinId': checkout.CheckinId,
                'CancellationReasonId': checkout.CancellationReasonId,
                'CheckoutTypeId': checkout.CheckoutTypeId,
            }
            for checkout in checkouts
        ]

        return result

    except Exception as e:
        return {"error": str(e)}