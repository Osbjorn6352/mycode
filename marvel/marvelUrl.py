#!/usr/bin/env python3

import time
import hashlib

def main():
    with open("marvel.pub") as pubkey:
        pubkey = pubkey.read().rstrip('\n')
    
    with open("marvel.priv") as privkey:
        privkey = privkey.read().rstrip('\n')
    
    ts = str(time.time())

    combined = ts + privkey + pubkey


    #Print out what we have
    print("TIMESTAMP:", ts)
    print("PRIVATE:", privkey)
    print("PUBLIC:", pubkey)
    print("COMBINED STRING:", combined)

    combined = combined.encode("utf-8")

    combinedHash = hashlib.md5(combined)

    combinedHash = combinedHash.hexdigest()

    print("HASH:", combinedHash)

    url = f"http://gateway.marvel.com/v1/public/comics?ts={ts}&apikey={pubkey}&hash={combinedHash}"

    print(url)

if __name__ == '__main__':
    main()
