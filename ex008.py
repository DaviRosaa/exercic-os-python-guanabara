m=(float(input("Quantos metros quer converter em centímetros e milímetros? km, hm e dm")))
c=int(m*100)
mi=int(m*1000)
km=float(m/1000)
hm=float(m/100)
dm=float(m/10)
print(f"\033[35m{m}\033[m equivale a \033[35m{c}\033[m centimetros e \033[35m{mi}\033[m a milimetros, em kilometros \033[36m{km:.2f}\033[m em hectometros "
      f"e \033[36m{hm:.2f}\033[m e em decimetros \033[36m{dm:.2f}\033[m ")