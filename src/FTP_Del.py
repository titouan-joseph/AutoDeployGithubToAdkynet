import pysftp
import os

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

adkynetUsername = os.getenv("INPUT_ADKYNETUSERNAME")
adkynetPassword = os.getenv("INPUT_ADKYNETPASSWORD")
adkynetServerName = os.getenv("INPUT_ADKYNETSERVERNAME")
adkynetServerPort = os.getenv("INPUT_ADKYNETSERVERPORT")


with pysftp.Connection(host=adkynetServerName,
                       username=adkynetUsername,
                       password=adkynetPassword,
                       cnopts=cnopts,
                       port=int(adkynetServerPort)) as sftp:
    print("Connection succesfully stablished ... ")

    sftp.rmdir("bot")
    print("le repo distant a ete supprime")
