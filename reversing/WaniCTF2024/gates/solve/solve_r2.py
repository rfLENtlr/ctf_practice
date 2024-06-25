import r2pipe
import string

flag_len = 32
break_addr = 0x000010e3
known_flag = 'FLAG{' + 'A' * 26 + '}\n'

def is_correct_letter(index, r2):
    r2.cmd("dc")
    rax = r2.cmd("pv1 @rax+{}".format(hex(index * 0x10)))
    rdx = r2.cmd("pv1 @rdx+{}".format(hex(index * 0x1)))    

    if rax == rdx:
        return True
    else:
        return False

def r2_run_with_stdin(flag):
    profile = """#!/usr/bin/rarun2\nprogram=./gates\nstdin="{}" """.format(flag)
    
    with open('profile.rr2', 'w') as f:
        f.write(profile)

    r2 = r2pipe.open('gates', flags=['-e', 'dbg.profile=profile.rr2', '-2'])
    r2.cmd("db {}".format(break_addr))
    r2.cmd("doo")
    return r2



for i in range(5, flag_len-1, 1):
    for letter in string.printable[:-5]:
        tmp = known_flag[:i] + letter + known_flag[i+1:]
        r = r2_run_with_stdin(tmp)

        if is_correct_letter(i, r):
            known_flag = tmp
            print("current flag = {}".format(tmp))
            break