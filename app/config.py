class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:yourpassword@localhost/studyapp"
    SECRET_KEY = "polaris402"
