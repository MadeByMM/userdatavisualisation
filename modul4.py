import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = [1,2,3,4] #værdier til 4 punkter
b = [1.2,3,8.5,16.3] #værdier til 4 punkter
#c = [.1*x for x in range(0,50)] #skaber 50 punkter mellem 0 og 5
c = np.linspace(-6, 6, 500) #skaber 500 punkter mellem -6 og 6

coef = np.polyfit(a,b,2) #skaber koefficienter til en linje
poly1d_fn = np.poly1d(coef) #skaber en funktion ud fra koefficienterne

plt.plot(a,b,'ro', c, poly1d_fn(c), 'k', markersize=10, linewidth = 2) #plotter punkterne og linjen 
#ro = røde prikker, k = sort linje, markersize = størrelse på prikker, linewidth = tykkelse på linje
plt.xlim(-6,6) #sætter grænser for x-aksen
plt.ylim(0,20) #sætter grænser for y-aksen

plt.title('En titel', fontsize=24, color='#22cdca') #sætter titel, fontsize = skriftstørrelse, color = skriftfarve
plt.grid() #sætter grid
plt.legend(['Punkter', 'Linje']) #sætter legend
plt.xlabel('x-akse', fontstyle='italic') #sætter x-akse label
plt.ylabel('y-akse') #sætter y-akse label

plt.show() #viser plot