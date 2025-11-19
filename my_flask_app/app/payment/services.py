from app.models import Payment
from app import db

def get_payment_data():
    try:
        # Query the Guest table
        payments = Payment.query.all()

        # Convert the result to a list of dictionaries
        result = [
            {
                'Id': payment.Id,
                'CardNumber': payment.CardNumber,
                'PaidAmount': payment.PaidAmount,
                'AddedAt': payment.AddedAt,
                'AddedFrom': payment.AddedFrom,
                'PaymentTypeId': payment.PaymentTypeId,
                'CardTypeId': payment.CardTypeId,
                
            }
            for payment in payments
        ]

        return result

    except Exception as e:
        return {"error": str(e)}