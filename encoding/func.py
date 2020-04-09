import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

# main(languages, encoding, error)

### Example of what is happening in above functions
## When you have bytes and need a string, DECODE BYTES
## When you have strings and need bytes, ENCODE STRINGS
utfstring = "日本語"
utfrawbytes = b'\xe6\x97\xa5\xe6\x9c\xac\xe8\xaa\x9e'
print(utfstring.encode(encoding="utf8"))
print(utfrawbytes.decode(encoding="utf8"))
