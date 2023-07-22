sh= input ('enter an hour')
sr= input ('enter a rate')
fh= float(sh)
fr= float(sr)
if fh>40:
 print ("overtime")
 reg=fr*fh
 otp=(fr-40.0)-(fr*0.5)
 print(reg, otp)
 xp= reg+otp
else:
    print('regular') 
    xp=fr*fh
print('pay', xp)
