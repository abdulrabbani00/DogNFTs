from scripts.helpful_scripts import (
    get_account,
    get_contract,
    OPENSEA_FORMAT,
    fund_with_link,
)
from brownie import AdvancedCollectible, config, network


def deploy_and_create():
    account = get_account()
    network_val = config["networks"][network.show_active()]
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        network_val["keyhash"],
        network_val["fee"],
        {"from": account},
    )
    fund_with_link(advanced_collectible.address)
    creating_tx = advanced_collectible.createCollectible({"from": account})
    creating_tx.wait(1)
    print("New token has been created")
    return advanced_collectible, creating_tx


def main():
    deploy_and_create()
