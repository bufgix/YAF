from YAF import start_server, cleanup

import argparse
import signal


parser = argparse.ArgumentParser("YAF")
parser.add_argument('--no-ngrok', action='store_true',
                    help="Run flask server without ngrok")


if __name__ == '__main__':
    signal.signal(signal.SIGINT, cleanup)
    try:
        args = parser.parse_args()
        start_server(args)
    except Exception:
        pass
