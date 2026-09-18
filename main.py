import pandas as pd
import numpy as np

data={
'Skill':['Python','Numpy','Pandas','MySql','Pytorch','Matplotlib'],        
'Required':[80,75,70,60,90,65]

}

df=pd.DataFrame(data)

print("\n---------------------------------------")
print("\n----------SKILLS GAP ANALYZER----------")
print("\n---------------------------------------")
print("\n Target Gap Career : AI/ML Engineer")
print("\n Enter your Skill Level from 0-100 ")

my_skills=[]
for skill in df["Skill"]:
    level=float(input (f"How good  are you at {skill} : "))
    my_skills.append(level)


my_skills=np.array(my_skills)
required=np.array(df["Required"])

gap=required - my_skills
gap=np.maximum(gap,0)

df["My_level"]= my_skills
df["Gap"]= gap


print("\n======================================")
print("\n------------MY RESULT-----------------")
print("\n======================================")
print(df)


print("\nSkills I need to improve:")

for i in range(len(df)):

    if df["Gap"][i] > 0:
        print(
            f"- {df['Skill'][i]} "
            f"(Need {df['Gap'][i]:.0f}% more)"
        )


print("\n---------------------------------------")
print("       Done! Keep learning 🚀           ")
print("-----------------------------------------")







