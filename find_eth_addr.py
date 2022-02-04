from eth_account import Account
import secrets, sys

words = 'words.txt'                           # txt file that contains all words wanted to be found in the address

print('=' * (80-14))

while True:
    try:
        priv = secrets.token_hex(32)          # generated 32 bytes of hexadecimal data
        private_key = "0x" + priv             # added 0x to look like a private key  
        acct = Account.from_key(private_key)

        with open(words, 'r') as file:            # opens given txt file 
            for line in file:                     # checks each line in file   

                wordsize = len(line.rstrip())        # variable of total size(characters) of the words given in each line 
                max = wordsize + 2                      # index for starting position at the beginning of the address
                #min = 42 - wordsize                    # index for starting position at the end of the address
                print('\r' + acct.address, end='')

                if acct.address[2:max] == line.rstrip():# and acct.address[min:42] == line.rstrip():        # used when using the words given to the  
                                                                                                            # end of wallet                    

                    combined = 'Ethereum address found\n' + str(acct.address) + '\n' + str(private_key) + '=' * (80-14)
                    print('')
                    print(combined)

                    with open("eth_addrs.txt", "a") as file_object:      # appends addresses that matches conditionsin txt file 
                        file_object.write('\n' + acct.address + '\n' + private_key + '\n' + ('=' * (80-14)))

    except KeyboardInterrupt:
        sys.exit()

print('=' * (80-14))