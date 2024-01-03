import time

import extensions.api.blocking_api as blocking_api
import extensions.api.streaming_api as streaming_api
from modules import shared
from modules.logging_colors import logger


def setup():
    logger.warning("\nThe legacy API has been replaced with the OpenAI compatible API on November 13th.\nPlease switch to the new API as soon as possible.\nFor documentation on the new API, consult:\nhttps://github.com/oobabooga/text-generation-webui/wiki/12-%E2%80%90-OpenAI-API")
    blocking_api.start_server(6050, share=shared.args.public_api, tunnel_id=shared.args.public_api_id)
    if shared.args.public_api:
        time.sleep(5)

    streaming_api.start_server(6055, share=shared.args.public_api, tunnel_id=shared.args.public_api_id)
