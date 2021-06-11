import matplotlib.pyplot as plt
import pandas as pd
   
Data = {'Country': ['Luxembourg', 'Macao','Norway','Ireland','Qatar','Iceland' ' ', 'USA'],
        'GDP_Per_Capita': [113197,83717,77976,77771,69688,67037,65112]
       }
df = pd.DataFrame(Data,columns=['Country','GDP_Per_Capita'])

New_Colors = ['green','red','blue','orange','teal','purple','green']
plt.bar(df['Country'], df['GDP_Per_Capita'], color=New_Colors)
plt.title('Top Seven GDP Per Capita', fontsize=12)
plt.xlabel('Country', fontsize=14)
plt.ylabel('GDP Per Capita', fontsize=14)
plt.grid(True)
plt.show()
