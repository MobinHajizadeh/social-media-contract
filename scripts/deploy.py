from brownie import Platform
from scripts.useful import get_account


def deploy_plt():
    account = get_account()
    plt = Platform.deploy({"from": account}, publish_source=True)
    print("contract deployed!")
    return plt


def main():
    deploy_plt()
