# stegoping
Chat over ICMP (Echo request).

The messages are encrypted with Vigenère cipher, for more details about it, [click here](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

## Installation
This project needs:

```
python 2.7
scapy 2.3.3
```

This project has a "requirements.txt" (pip) file for easy installations of needed dependencies.

```
pip install -r requirements.txt
```

## Usage

There will be two endpoints, one listening as a server and another will be the active sender. The communication will be one-way only.

Receiver:
```
python receiver.py -i <interface name> -k <key>
```

i.e.:

```
receiver.py -i 192.168.1.5 -k snake
```

Sender:
```
stegoping.py -d <ipv4 address dst> -k <key> -m <message>
```

i.e.:

```
stegoping.py -d 192.168.1.5 -k snake -m helloworld
```

## Tips
Remember you must run it with privileges.

## Limitations

Puff... a lots.

 * Not spaces allowed, only single words.

## License

Do not worry about it. :)
