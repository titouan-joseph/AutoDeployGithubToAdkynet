import os
import pysftp

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
    sftp.mkdir("bot")
    for path in os.walk("bot"):
        for file in path[2]:
            localFile = os.path.join(os.getcwd(), path[0], file)
            remoteDirectory = os.path.join(os.sep,
                                           "bot",
                                           f"{os.sep}".join(path[0].split(os.sep)[1:]),
                                           file).replace(os.sep, "/")
            sftp.put(localFile, remoteDirectory)
            print("le repo a ete upload sur le serveur distant")
