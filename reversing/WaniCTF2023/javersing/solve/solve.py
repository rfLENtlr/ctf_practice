encoded_flag = "Fcn_yDlvaGpj_Logi}eias{iaeAm_s"

# flagを適当な30文字にしておく
flag = 'A' * 30
flag_list = list(flag)

# デコード処理
for i in range(0,30):
    flag_list[i*7%30] = encoded_flag[i]

# list to str
print("".join(flag_list))