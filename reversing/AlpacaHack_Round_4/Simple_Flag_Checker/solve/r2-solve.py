import r2pipe
import string

flag_len = 49
break_addr = 0x1a2f
known_flag = 'Alpaca{'
program_path = './checker'

def is_correct_letter(current_len, r2):
    for _ in range(current_len):
        r2.cmd("dc")
    eax = int(r2.cmd("dr eax"), 16)

    if eax == 0:
        return True
    else:
        return False

def r2_run_with_stdin(flag):
    profile = """#!/usr/bin/rarun2\nprogram={}\nstdin="{}" """.format(program_path, flag)
    
    with open('profile.rr2', 'w') as f:
        f.write(profile)

    r2 = r2pipe.open(program_path, flags=['-e', 'dbg.profile=profile.rr2', '-2'])
    r2.cmd("db {}".format(break_addr))
    r2.cmd("doo")

    return r2

while len(known_flag) != flag_len:
    found = False

    for letter in string.printable[:-5]:
        current_flag = known_flag + letter
        r = r2_run_with_stdin(current_flag)

        if is_correct_letter(len(current_flag), r):
            known_flag += letter
            print("current flag = {}".format(current_flag))
            found = True
            break

    if not found:
        print("FAILED TO FIND FLAG")
        break

if found:
    print("FLAG FOUND: {}".format(known_flag))