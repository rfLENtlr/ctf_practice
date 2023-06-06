import angr
import sys
import claripy

input_file_path = './chall.baby'
flag_length = 35
known_string = 'SECCON{'
FIND_ADDR = 0x12c2
AVOID_ADDR = 0x1273


proj = angr.Project(input_file_path, main_opts={'base_addr': 0x00})
known_chars = [claripy.BVV((known_string[i]))
               for i in range(len(known_string))]
flag_chars = [claripy.BVS(f"flag_{i}", 8)
              for i in range(flag_length - len(known_string))]
flag = claripy.Concat(*known_chars + flag_chars)
state = proj.factory.full_init_state(args=[input_file_path, flag])
sim_manager = proj.factory.simulation_manager(state)
sim_manager.explore(find=FIND_ADDR, avoid=AVOID_ADDR)

if(len(sim_manager.found) > 0):
    print(sim_manager.found[0].solver.eval(flag, cast_to=bytes))