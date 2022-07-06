import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
 
 
#x=np.random.normal(35,1,10000)


#plt.hist(x, bins=100)
#plt.show()
##sns.histplot(x)
#plt.show()

#sns.displot(x,color="g",kde=True)
#plt.show()
np.random.seed(0)
veri=np.random.normal(35,2,40000)
print(veri)
veriz=stats.zscore(veri)
sns.displot(veriz, kde=True)

plt.title("Veri Dagilim Grafigi", fontsize=15, loc="right", c="r")
plt.xlabel("Veriler", fontsize=15, c="r")
plt.ylabel("Frekans", fontsize=15, c="r")
plt.xlim(-3,3)
plt.axvline(x=np.mean(veriz), linestyle="--", linewidth=2.5, label="Ortalama", c="r")

plt.axvline(x=np.mean(veriz)- np.std(veriz), linestyle="--", linewidth=2.5, label="1 Standart sapma", c="g")

plt.axvline(x=np.mean(veriz)+ np.std(veriz),linestyle="--", linewidth=2.5,  c="g")


plt.axvline(x=np.mean(veriz)- 2*np.std(veriz), linestyle="--", linewidth=2.5, label="2 Standart sapma", c="b")

plt.axvline(x=np.mean(veriz)+ 2*np.std(veriz),linestyle="--", linewidth=2.5,  c="b")

plt.legend()
plt.show()