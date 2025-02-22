class Config:
    # MySQL configurations
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''  # Set your MySQL password here
    MYSQL_DB = 'ambulance_service'
    
    # Flask configurations
    SECRET_KEY = 'your-secret-key-here'  # Change this in production
    
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
