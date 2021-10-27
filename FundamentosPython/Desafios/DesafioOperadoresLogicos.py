trabalho_terca = False
trabalho_quinta = False

tv_50 = trabalho_terca and trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta 
sorvete = tv_50 or tv_32
saude = not sorvete

print("TV 50: {} TV 32: {} SORVETE: {} SAUDE: {}".format(tv_50, tv_32, sorvete, saude))