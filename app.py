# step 1 : load  imporatant modules
import pandas  as pd
import numpy as np.
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
import streamlit as st 
# this streamlit is for  web based application project


#  Web page Code
st.title("HEALTH INSURANCE PREDICTION")
img_url = "https://cdn.zeebiz.com/sites/default/files/2026/03/09/401943-health-insurance.png"
st.image(img_url)

# LOAD DATA  and ML MODEL PART
# step 2 : load insurance data
url ="https://raw.githubusercontent.com/ankitmisk/UIT-data/refs/heads/main/Insurance.csv"
df = pd.read_csv(url)


# step 3 : EDA : Exploratary data analysis
df.drop("Customer_ID", axis = 1, inplace = True)

df['Previous_Insurance'] = df['Previous_Insurance'].map({'No':0,"Yes":1})
df['Insurance_Bought'] = df['Insurance_Bought'].map({'No':0, "Yes":1})

# step 4 : Divide dataset into features and targe
X = df.iloc[:,:-1]
y = df.iloc[:,-1]

# Step 5: Divide data into Training & testing part
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=42, test_size=0.3)

# step 6: Train Model
model = LogisticRegression()
model.fit(X_train,y_train)


# show data sample
st.write(df.head))
#create side bar for user input form 
st.sidebar.titte("Fill Customer Detrails")
st.sidebar.image(img_url)

for index, col_name in enumerate(X.columns):
  min_v = X[col_name].min()
  max_v = X[col_name].max()
  if col_name !="Previous_Insurance":
    value = st.sidebar.slider(f"Select value for {col_name}",
                              min_value = min_v,
                              max_value = min_v)

else:
 value = st.sidebar.number_input (f"Select value for {col_name}: (0:No, 1: yes):")

all_ans.append(value)

ud = {j:all_ans[i] for i,j in enumerate(X.columns)}
user_df = pd.DataFrame(all_ans, columns = X.columns)
st.write(user_df)

#============================Predicition================================
if st.button("Click to Predict:"):
  with  st.spinner("Prediciting.."):
    import time 
    time.sleep
    time.sleep(2)
    final_ans = model.predict([all_ans])[0] 
    if final ans==0: 
    st.info(" ❎Customer will not Buy the Insurance ❎ ") 
else:
  st.success ("✅ Customer will buy the Insurance✅ ")



