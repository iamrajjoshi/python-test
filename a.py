import sentry_sdk

sentry_sdk.init(
    dsn="https://f42656d409c912a82021ba1399731c0d@raj-dev.ngrok.io/15",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
)

division = 1/0
