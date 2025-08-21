import sentry_sdk

sentry_sdk.init(
    dsn="https://192e4802401292bfe5020bc1c67b6e02@raj-dev.ngrok.io/4509367780376576",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
)

# division = 1/0


def fail():
    raise Exception("test")


fail()

def validate_inventory(inventory: list[dict]):
    raise Exception("test")
    for item in inventory:
        if item["quantity"] < 0:
            raise Exception("Invalid inventory")


validate_inventory([{"quantity": 10}, {"quantity": -1}])