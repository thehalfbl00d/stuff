from app import app, db, Hospital, Ambulance
from werkzeug.security import generate_password_hash

def init_db():
    with app.app_context():
        # Drop all tables
        db.drop_all()
        # Create all tables
        db.create_all()

        # Add a sample hospital
        hospital = Hospital(
            name='St. James Hospital',
            latitude=53.3419,
            longitude=-6.2967,
            email='admin@stjames.ie',
            password=generate_password_hash('password123')
        )
        db.session.add(hospital)
        db.session.commit()  # Commit to get the hospital ID

        # Add sample ambulances
        ambulances = [
            Ambulance(
                vehicle_number='AMB001',
                latitude=53.3498,
                longitude=-6.2603,
                status='available',
                hospital_id=hospital.id  # Use the actual hospital ID
            ),
            Ambulance(
                vehicle_number='AMB002',
                latitude=53.3458,
                longitude=-6.2575,
                status='available',
                hospital_id=hospital.id  # Use the actual hospital ID
            )
        ]
        
        for ambulance in ambulances:
            db.session.add(ambulance)
        
        db.session.commit()

if __name__ == '__main__':
    init_db()
    print("Database initialized with sample data!")
