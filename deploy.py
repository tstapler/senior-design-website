#! /usr/bin/env python

# sftpclone can be imported into a custom Python script to deploy a
# static website to a web host where you only have stripped-down sftp
# access. The below is an example of a deployment script that keeps
# your username and password out of the shell history and uses an
# exclude file. In practice, one might have complex needs. For
# example, the website may be built from assets in multiple,
# separately managed directory trees on the local host. Using
# sftpclone programmatically with exclude files makes it easy to
# script one-step deployments for such situations.

import getpass
from sftpclone import sftpclone

def deploy_website():
    cloner = sftpclone.SFTPClone(
        './public',
        "may1705:{}@may1705.sd.ece.iastate.edu:./www".format(getpass.getpass())
    )
    cloner.run()

if __name__ == "__main__":
    deploy_website()
