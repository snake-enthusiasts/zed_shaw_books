from sys import argv

text = ""
if len(argv) > 3:
    print("Jest większa")
    for i in range(1, len(argv) - 1):
        if argv[i] != '>':
            source_file = open(argv[i])
            text = source_file.read()
            print(text)
        else:
            output_file = open(argv[i+1], 'w')
            output_file.write(text)
else:
    print("Number of arguments is too small.")

print(argv)
