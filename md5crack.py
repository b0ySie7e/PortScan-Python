import hashlib
import argparse

def md5_cracker(md5_hash, wordlist, print_all=False):
    try:
        with open(wordlist, 'r', encoding='utf-8') as file:
            for line in file:
                candidate = line.strip()
                if hashlib.md5(candidate.encode('utf-8')).hexdigest() == md5_hash:
                    print(f"MD5 hash successfully cracked: {md5_hash} -> {candidate}")
                    if not print_all:
                        return  
            if print_all:
                print("Hash no encontrado en el diccionario.")
            else:
                print("Hash no encontrado en el diccionario. Intenta con un diccionario más grande o diferente.")
    except FileNotFoundError:
        print(f"Error: No se puede encontrar el archivo {wordlist}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def main():
    parser = argparse.ArgumentParser(description='MD5 Cracker')
    parser.add_argument('-md5', dest='hash', help='MD5 hash', required=True)
    parser.add_argument('-w', dest='wordlist', help='Wordlist file', required=True)
    parser.add_argument('--all', action='store_true', help='Print all matching passwords')

    parsed_args = parser.parse_args()
    md5_cracker(parsed_args.hash, parsed_args.wordlist, parsed_args.all)

if __name__ == '__main__':
    main()