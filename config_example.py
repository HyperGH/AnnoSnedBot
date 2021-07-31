'''
Configuration file example for the Discord bot Sned.
The actual configuration is read from 'config.py', which must exist.
'''

config = {
    'token': 'oh no I leaked my token', #Bot's token
    #Postgres dsn for the database, must have {db_name} when addressing the database name
    'postgres_dsn': 'postgres://postgres:my_password_here@1.2.3.4:5432/{db_name}', 
    'ipc_secret': 'oh no I leaked my ipc secret', #IPC secret (optional)
    'experimental': False, #Controls debugging mode
}