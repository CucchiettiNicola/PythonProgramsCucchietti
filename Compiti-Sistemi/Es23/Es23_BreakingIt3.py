#Giraudo Francesco Es.23 Breaking It 3
import sys

script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    raw_bytes = line.strip()
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

# open the file in read byte mode
languages = open("languages.txt", 'rb')

main(languages, input_encoding, error)