import matplotlib.pyplot as plt
from IPython.display import Image
from IPython.core.display import HTML
def numerico(x):
    if x:
        return 1
    else: return 0

def representacionGrafica(df,col1,col2,titulo,x):
	if col1=="Legendary":
		df["LegendaryNum"]=df["Legendary"].apply(numerico)
		col1="LegendaryNum"
	my_plot=df.plot(col1,col2,kind="scatter",title=titulo)
	plt.savefig('figura{}.png'.format(x))
	plt.show()
