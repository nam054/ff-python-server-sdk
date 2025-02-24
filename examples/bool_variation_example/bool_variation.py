import time

from featureflags.evaluations.auth_target import Target
from featureflags.client import CfClient
from featureflags.util import log

def main():
    log.debug("Starting example")
    api_key = "Your API Key"
    client = CfClient(api_key)

    target = Target(identifier='harness')

    while True:
        result = client.bool_variation('identifier_of_your_bool_flag', target, False)
        log.debug("Result %s", result)
        time.sleep(10)

if __name__ == "__main__":
    main()
