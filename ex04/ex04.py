from sys import argv

"""
name, arg1, arg2, arg3 = argv
print(arg1, " ", arg2, " ", arg3)
"""
m_var = False
n_var = False
o_var = False
a_opt = "#"
b_opt = "#"
c_opt = "#"
it_is_option_arg = False

for i in range(1, len(argv)):
    if not(it_is_option_arg):
        if argv[i] == "-h" or argv[i] == "-help":
            print("Prosisz o pomoc. Brawo! Nie boisz się przyznać, że czegoś nie wiesz. ]:->")
        elif argv[i] == "-m":
            if not(m_var):
                m_var = True
            else:
                m_var = False
        elif argv[i] == "-n":
            if not(n_var):
                n_var = True
            else:
                n_var = False
        elif argv[i] == "-o":
            if not(o_var):
                o_var = True
            else:
                o_var = False
        elif argv[i] == "-a":
            if i < (len(argv) - 1):
                a_opt = argv[i + 1]
            else:
                print("Ther is a missing argument for the option a")
            it_is_option_arg = True
        elif argv[i] == "-b":
            if i < (len(argv) - 1):
                b_opt = argv[i + 1]
            else:
                print("Ther is a missing argument for the option b")
            it_is_option_arg = True
        elif argv[i] == "-c":
            if i < (len(argv) - 1):
                c_opt = argv[i + 1]
            else:
                print("Ther is a missing argument for the option c")
            it_is_option_arg = True
    else:
        it_is_option_arg = False

print("Stan flag - m: ", m_var, "n: ", n_var, "o: ", o_var)
print("Zmienne opcji: - a: ", a_opt, "b: ", b_opt, "c: ", c_opt)
