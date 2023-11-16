# Legacy API extension for the oobabooga Text Generation Web UI

This is an extension for the [Text Generation Web UI](
https://github.com/oobabooga/text-generation-webui) to
provide support for the legacy API which has been replaced
by the Open AI compatible API.

Many applications still rely on the legacy API in order
to function correctly and the developers of those
applications need to be given sufficient time to migrate
to the new Open AI compatible AI.  This extension provides
the legacy API for those developers so that they can
successfully migrate their applications to the new API.

## Installation

### My RunPod Template

This extension is already installed in [my template](
https://runpod.io/gsc?template=el5m58e1to&ref=2xxro4sy)
on RunPod, so you don't need to install anything if you
use my template.

### TheBloke's RunPod Template

1. Install the extension
    ```bash
    cd  /workspace/text-generation-webui
    git clone --depth=1 https://github.com/ashleykleynhans/oobabooga-legacy-api-extension.git extensions/api
    pip3 install -r extensions/api/requirements.txt
    ```
2. Edit the startup script
    ```bash
   vim /workspace/run-text-generation-webui.sh
    ```
    Change line 6 (ARGS) as follows:
    ```bash
   ARGS=("$@" --listen --api --extensions api --api-port 5000 --api-blocking-port 6000 --api-streaming-port 6005)
    ```
   * `--api` starts the OpenAI compatible API.
   * `--extensions api` enables the legacy API extension.
   * `--api-port 5000` sets the port for the OpenAI compatible API to 5000.
   * `--api-blocking-port 6000` sets the port for the legacy REST API to 6000.
   * `--api-streaming-port 6005` sets the port for the legacy WebSockets API to 6005.
3. Edit your pod and add HTTP ports 6000 and 6005 and click `Save`.
4. You can now connect to the legacy REST API on HTTP port 6000 and the legacy
   WebSockets API on port 6005.