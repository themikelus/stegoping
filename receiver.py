import sys, getopt

from scapy.layers.inet import IP, ICMP, send, sniff, Ether, Raw

def main(argv):
    protocol = 'ICMP'  # default
    interface_name = ''
    key = ''

    try:
        console_msg = 'receiver.py -i <interface name> -k <key>'
        options, args = getopt.getopt(argv, "hi:k:")

        if not options and not args:
            print console_msg
            sys.exit(2)
        else:
            for opt, arg in options:
                if opt == '-h' or opt == '-help':
                    print console_msg
                    sys.exit(2)

                if opt in ('-i'):
                    interface_name = arg
                elif opt in ('-k'):
                    key = arg
    except getopt.GetoptError:
        print console_msg
        sys.exit(2)

    collect_ICMP_packages(interface_name, key)

def collect_ICMP_packages(interface_name, key):
    print 'Collecting [ICMP Echo] messages...\n'

    sniff(filter='icmp', iface=interface_name, prn=lambda packet: get_details(key, packet))

def get_details(key, packet):
    if packet[ICMP].type == 8: # echo-message
        print 'src:{} --> dst:{} = {}'.format(packet[IP].src, packet[IP].dst, decoder(key, packet[Raw].load))

def decoder(key, cipher_message):
    """Vigenere decoder
    
    :param key: key
    :param message: cipher message
    :return: message
    """
    message = ''

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    key = key.lower()
    cipher_message = cipher_message.lower()

    count_key = 0
    count_message = 0
    while count_message < len(cipher_message):
        if count_key >= len(key):
            count_key = 0

        index_next_letter = alphabet.index(cipher_message[count_message]) - alphabet.index(key[count_key])

        if index_next_letter >= len(alphabet):
            index_next_letter = index_next_letter - len(alphabet)

        message += alphabet[index_next_letter]

        count_key += 1
        count_message += 1

    return message

if __name__ == '__main__':
    main(sys.argv[1:])
