# import os

# class Config:
#     # Database configuration
#     SQLALCHEMY_DATABASE_URI = (
#         "mssql+pyodbc://sa:root@DESKTOP-SCN1CG5\\WPFSQLEXPRESS/apiitsthe1.id?"
#         "driver=ODBC+Driver+17+for+SQL+Server"
#     )
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SCHEMA_NAME = "[apiitsthe1.id].[itsthe1.id]"
#     BaseDirectoryPath = "C:/ITSthe1/WPF/Gates_API_Storage" 


import os

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://sa:root@DESKTOP-SCN1CG5\\WPFSQLEXPRESS/api_gates_itsthe1.id"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SCHEMA_NAME = "[api_gates_itsthe1.id].[itsthe1.id]"
    BaseDirectoryPath = "C:/ITSthe1/WPF/Gates_Storage"
    GOOGLE_TRANSLATOR_URL = os.getenv("GOOGLE_TRANSLATOR_URL", "https://google.com/transliterate/indic")
