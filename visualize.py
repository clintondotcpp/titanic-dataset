import matplotlib.pyplot as plt
import seaborn as sns
import data_exploration as de

#Check missing values
sns.heatmap(de.data.isnull(), cbar=False, cmap='viridis')
plt.show()

#Visualize survival rate by gender
sns.countplot(x='Sex', hue='Survived', data=de.data)
plt.title('Survival Rate by Gender')
plt.show()

#Visualize survival rate by class
sns.countplot(x='Pclass', hue='Survived', data=de.data)
plt.title('Survival Rate by Class')
plt.show()