# grpc-apm-example

* install your favorites Linux operating system
* install Protobuf
* install GRPC
* install GRPC language binging package: 
    * `python-grpcio` (Debian)
    * or via python3 using pip3: `grpcio`)

```
# clone apm repository
git clone https://github.com/frederic-loui/grpc-apm-example.git

# go into cloned directory
cd apm

# generate apm python bindings
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. apm.proto 
```
then you can fire a TMUX session in order to have 3 windows:
* `./apm_server.py` APM server window
* `./apm_client.py` APM client window
* `sudo tcpdump -nnvvXSs 1514 -i lo port 50051` TCPdump outfrom from client/server discussion

![APM](/apm.png)
