# grpc-apm-example

* install your favorites Linux operating system
* install Protobuf
* install GRPC
* install GRPC language binging package: 
    * python-grpcio (Debian)
    * or via python3 using pip3: grpcio)

```
# clone apm repository
git clone https://github.com/frederic-loui/grpc-apm-example.git

# go into cloned directory
cd apm

# generate apm python bindings
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. apm.proto 
```
then you can fire a TMUX session in order to have 3 windows:
* APM server window
* APM client window
* TCPdump outfrom from client/server discussion

[[https://github.com/frederic-loui/grpc-apm-example/blob/main/apm.png|APM]]


