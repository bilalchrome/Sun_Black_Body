import matplotlib.pyplot as plt
import math as mt
import xlwt
planets=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
distances_from_sun=[57e9,108e9,150e9,228e9,779e9,1.43e12,2.88e12,4.5e12]
actual_temps = [700,742,285,243,163,133,76,70]
dia_sun=1.392e9
Tsun=5800
bltz=5.67e-8
epsln=1
q_sun=mt.pi*dia_sun**2*bltz*epsln*Tsun**4
temp_planets=[(q_sun/(4*mt.pi*bltz*d**2))**(1/4)for d in distances_from_sun]
plt.xlabel('Distance From Sun (m)',fontsize=14)
plt.ylabel('Temperature (K)',fontsize=14)
plt.title('Planet Temperatures wrt Distance From Sun',fontsize=16,y=1.03)
plt.xscale('log')
plt.subplot(111).spines['top'].set_visible(False)
plt.subplot(111).spines['right'].set_visible(False)
for label,x,y in zip(planets,distances_from_sun,actual_temps):
    if label == 'Mercury':
        plt.text(x-2000000000,y+30,label)
    elif label !='Uranus':
        plt.text(x,y+20,label)
    elif label == 'Uranus':
        plt.text(x-400000000000,y+30,label)
plt.plot(distances_from_sun,temp_planets,linewidth=2,color='#ffb861',label='Calculated Temperatures')
plt.scatter(distances_from_sun,actual_temps,color='#bdb0d0',label = 'Actual Temperatures')
plt.legend(frameon=False)
plt.savefig('Planet_Temps.png',dpi=800)
wb = xlwt.Workbook()
sheet1 = wb.add_sheet('Sheet1')
sheet1.write(0,0,'Planets')
sheet1.write(0,1,'Distance From Sun (m)')
sheet1.write(0,2,'Actual Temperature of Planets (k)')
sheet1.write(0,3,'Calculated Temperature of Planets (k)')
for i in range(0,len(planets)):
    sheet1.write(i+1,0,planets[i])
    sheet1.write(i+1,1,distances_from_sun[i])
    sheet1.write(i+1,2,actual_temps[i])
    sheet1.write(i+1,3,temp_planets[i])
#wb.save('/home/esther/Documents/LastProj.xls')
