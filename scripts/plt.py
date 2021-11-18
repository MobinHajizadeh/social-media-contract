from scripts.useful import get_account
from brownie import Platform
from scripts.ipfs import upload_to_ipfs

PLT = Platform[-1]
ACCOUNT = get_account()


def upload_to_plt(title, hash, description):
    PLT.uploadFile(title, hash, description, {"from": ACCOUNT})
    print("Uploaded successfully!")


def like(file_id):
    PLT.likeFile(file_id, {"from": ACCOUNT})
    print("Liked!")


def comment(file_id, text):
    PLT.addComment(file_id, text, {"from": ACCOUNT})
    print("Commnet added successfully!")


def main():
    hash = upload_to_ipfs("Hello PLT!!")
    title = "ETH"
    description = "Future, wait!!"
    upload_to_plt(title, hash, description)
