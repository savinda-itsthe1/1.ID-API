from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

# Initialize extensions
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.schema = app.config['SCHEMA_NAME']

    # Initialize extensions with the app
    db.init_app(app)

    # Register blueprints
    from app.checkin.routes import checkin_bp
    from app.checkout.routes import checkout_bp
    from app.roomchange.routes import roomchange_bp
    from app.accessibilitytype.routes import accessibilitytype_bp
    from app.cancellationreason.routes import cancellationreason_bp
    from app.cardtype.routes import cardtype_bp
    from app.checkinguest.routes import checkinguest_bp
    from app.checkintype.routes import checkintype_bp
    from app.checkouttype.routes import checkouttype_bp
    from app.country.routes import country_bp
    from app.documenttype.routes import documenttype_bp
    from app.dtcmaction.routes import dtcmaction_bp
    from app.emirate.routes import emirate_bp
    from app.escorttype.routes import escorttype_bp
    from app.guest.routes import guest_bp
    from app.guestattachment.routes import guestattachment_bp
    from app.guestversion.routes import guestversion_bp
    from app.log.routes import log_bp
    from app.mainguestchange.routes import mainguestchange_bp
    from app.payment.routes import payment_bp
    from app.paymenttype.routes import paymenttype_bp
    from app.relationship.routes import relationship_bp
    from app.room.routes import room_bp
    from app.visitpurpose.routes import visitpurpose_bp
    from app.guestcheckout.routes import guestcheckout_bp
    from app.checkincancellation.routes import checkincancellation_bp
    

    
    

    app.register_blueprint(checkin_bp)
    app.register_blueprint(checkout_bp)
    app.register_blueprint(roomchange_bp)
    app.register_blueprint(accessibilitytype_bp)
    app.register_blueprint(cancellationreason_bp)
    app.register_blueprint(cardtype_bp)
    app.register_blueprint(checkinguest_bp)
    app.register_blueprint(checkintype_bp)
    app.register_blueprint(checkouttype_bp)
    app.register_blueprint(country_bp)
    app.register_blueprint(documenttype_bp)
    app.register_blueprint(dtcmaction_bp)
    app.register_blueprint(emirate_bp)
    app.register_blueprint(escorttype_bp)
    app.register_blueprint(guest_bp)
    app.register_blueprint(guestattachment_bp)
    app.register_blueprint(guestversion_bp)
    app.register_blueprint(log_bp)
    app.register_blueprint(mainguestchange_bp)
    app.register_blueprint(payment_bp)
    app.register_blueprint(paymenttype_bp)
    app.register_blueprint(relationship_bp)
    app.register_blueprint(room_bp)
    app.register_blueprint(visitpurpose_bp)
    app.register_blueprint(guestcheckout_bp)
    app.register_blueprint(checkincancellation_bp)

    return app