This repository contains pre-compiled Wasm contracts whose main purpose is to provide VALID deploys of big size.

### Generating data

Running `./gen.sh` will generate a collection of `data_XXXXX_bytes` files that contain strings in base64 that are increasing in size.

### Preparing the contract

`main.rs` file was modified so that `ARG_MESSAGE` contains a template placeholder `$CONTENT` that can be replaced using `replace.py`.

`python replace.py main.rs data_1000_bytes main.rs` will substitute `$CONTENT` with a content of `data_1000_bytes` file.
