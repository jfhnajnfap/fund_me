from brownie import FundMe, MockV3Aggregator, network, config
from . import helpful_scripts

LOCAL_BLOCKCHAIN_ENVIRONMENTS = helpful_scripts.LOCAL_BLOCKCHAIN_ENVIRONMENTS


def get_account():
    return helpful_scripts.get_account()


def deploy_fund_me():
    account = get_account()
    # pass price feed address

    # if in presisten network use associated adress
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_adress = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        helpful_scripts.deploy_mocks()
        price_feed_adress = MockV3Aggregator[-1].address

    # otherwise, deploy mocks
    fund_me = FundMe.deploy(
        price_feed_adress,
        {"from": account},
        # publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
