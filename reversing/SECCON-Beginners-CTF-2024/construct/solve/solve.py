fragments = ["c0_d4yk261hbosje893w5igzfrvaumqlptx7n", "oxnske1cgaiylz0mwfv7p9r32h6qj8bt4d_u5", "lzau7rvb9qh5_1ops6jg3ykf8x0emtcind24w", "9_xva4uchnkyi6wb2ld507p8g3stfej1rzqmo", "r8x9wn65701zvbdfp4ioqc2hy_juegkmatls3", "tufij3cykhrsl841qo6_0dwg529zanmbpvxe7", "b0i21csjhqug_3erat9f6mx854pyol7zkvdwn", "17zv5h6wjgbqerastioc294n0lxu38fdk_ypm", "1cgovr4tzpnj29ay3_8wk7li6uqfmhe50bdsx", "3icj_go9qd0svxubefh14ktywpzma2l7nr685", "c7l9532k0avfxso4uzipd18egbnyw6rm_tqjh", "l8s0xb4i1frkv6a92j5eycng3mwpzduqth_7o", "l539rbmoifye0u6dj1pw8nqt_74sz2gkvaxch", "aj_d29wcrqiok53b7tyn0p6zvfh1lxgum48es", "3mq16t9yfs842cbvlw5j7k0prohengduzx_ai", "_k6nj8hyxvzcgr1bu2petf5qwl09ids!om347a"]

flag = []
for i in range(len(fragments)):
    flag.append(fragments[i][i*2])
    flag.append(fragments[i][i*2+1])

print("".join([str(x) for x in flag]))