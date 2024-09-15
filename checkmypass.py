import requests
import hashlib
import sys

def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}")
    return  res

def get_password_leaks_count(hashes,hash_to_check):
    hashes = (line.split(":") for line in hashes.splitlines())
    print(hashes)
    for h,count in hashes:
        if h == hash_to_check:
            return count
    return 0   

def pwned_api_check_password(password):
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char,tail = sha1password[:5],sha1password[5:]
    hashes = request_api_data(first5_char)
    return get_password_leaks_count(hashes.text,tail)


def main():
    
    if(len(sys.argv) < 2):
        print("Usage: python tester.py <password>")
        sys.exit(1)
        
    list_password = sys.argv[1::]

    for password in list_password:
        count = pwned_api_check_password(password)
        if count:
            print(f"{password} was found {count} times... you should probably change your password!")
        else:
            print(f"{password} was NOT found. Carry on!")

if __name__ == '__main__':
    main()