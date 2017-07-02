import sys, getopt

from scapy.layers.inet import IP, ICMP, send

def main(argv):
    protocol = 'ICMP' # default
    ipv4_address_dst = ''
    message = ''
    key = ''

    try:
        console_msg = 'stegoping.py -d <ipv4 address dst> -k <key> -m <message>'
        options, args = getopt.getopt(argv, "hd:k:m:")

        if not options and not args:
            print console_msg
            sys.exit(2)
        else:
            for opt, arg in options:
                if opt == '-h' or opt == '-help':
                    print console_msg
                    sys.exit(2)

                if opt in ('-d'):
                    ipv4_address_dst = arg
                elif opt in ('-k'):
                    key = arg
                elif opt in ('-m'):
                    message = arg
    except getopt.GetoptError:
        print console_msg
        sys.exit(2)

    send_data_over_ICMP(ipv4_address_dst, key, message)

def send_data_over_ICMP(ipv4_address_dst, key, message):
    send(IP(dst=ipv4_address_dst) / ICMP() / encoder(key, message))
    #send(IP(dst=ipv4_address_dst) / ICMP() / message)

def encoder(key, message):
    """Vigenere coder
    
    :param key: key
    :param message: plain text
    :return: cipher text
    """
    cipher_text = ''

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    key = key.lower()
    message = message.lower()

    count_key = 0
    count_message = 0
    while count_message < len(message):
        if count_key >= len(key):
            count_key = 0

        index_next_letter = alphabet.index(message[count_message]) + alphabet.index(key[count_key])

        if index_next_letter >= len(alphabet):
            index_next_letter = index_next_letter - len(alphabet)

        cipher_text += alphabet[index_next_letter]

        count_key += 1
        count_message += 1

    return cipher_text

if __name__ == '__main__':
    main(sys.argv[1:])
