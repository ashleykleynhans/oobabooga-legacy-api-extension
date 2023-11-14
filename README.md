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

These instructions are specific to RunPod

```bash
cd  /workspace/text-generation-webui
git clone --depth=1 https://github.com/ashleykleynhans/oobabooga-legacy-api-extension.git extensions/api
source /workspace/venv/bin/activate
pip3 install -r extensions/api/requirements.txt
```
