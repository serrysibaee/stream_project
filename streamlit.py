
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import plotly.express as px 
from PIL import Image


st.set_page_config(page_title="Coupon chose",page_icon=":bar_chart:",
                    layout='wide')

st.title("SAS coupon")
#st.markdown("file:///C:/Users/serry/Downloads/ascii-art.html")
imge = Image.open("C:/Users/serry/Desktop/DataScience/projects/images/title.PNG")

st.image(imge)
df = pd.read_csv("incr.csv")

# drop the null and nearly null values
df.drop(['car'], axis=1, inplace=True)
df.dropna(inplace=True)

# show the data frame 
#st.dataframe(df)


# ---- SIDEBAR ----

st.sidebar.header("Please Filter Here:")

destination = st.sidebar.multiselect(
    "Select the destination:",
    options=df["destination"].unique(),
    default=df["destination"].unique()
)



passanger = st.sidebar.multiselect(
    "Select the passanger:",
    options=df["passanger"].unique(),
    default=df["passanger"].unique()
)



weather = st.sidebar.multiselect(
    "Select the weather:",
    options=df["weather"].unique(),
    default=df["weather"].unique()
)


time = st.sidebar.multiselect(
    "Select the time:",
    options=df["time"].unique(),
    default=df["time"].unique()
)




coupon = st.sidebar.multiselect(
    "Select the coupon:",
    options=df["coupon"].unique(),
    default=df["coupon"].unique()
)

expiration = st.sidebar.multiselect(
    "Select the expiration:",
    options=df["expiration"].unique(),
    default=df["expiration"].unique()
)

gender = st.sidebar.multiselect(
    "Select the gender:",
    options=df["gender"].unique(),
    default=df["gender"].unique()
)


maritalStatus = st.sidebar.multiselect(
    "Select the maritalStatus:",
    options=df["maritalStatus"].unique(),
    default=df["maritalStatus"].unique()
)


education = st.sidebar.multiselect(
    "Select the education:",
    options=df["education"].unique(),
    default=df["education"].unique()
)


occupation = st.sidebar.multiselect(
    "Select the occupation:",
    options=df["occupation"].unique(),
    default=df["occupation"].unique()
)

income = st.sidebar.multiselect(
    "Select the income:",
    options=df["income"].unique(),
    default=df["income"].unique()
)

Bar = st.sidebar.multiselect(
    "Select the Bar:",
    options=df["Bar"].unique(),
    default=df["Bar"].unique()
)

CoffeeHouse = st.sidebar.multiselect(
    "Select the CoffeeHouse:",
    options=df["CoffeeHouse"].unique(),
    default=df["CoffeeHouse"].unique()
)

CarryAway = st.sidebar.multiselect(
    "Select the CarryAway:",
    options=df["CarryAway"].unique(),
    default=df["CarryAway"].unique()
) 


### making the new data frame from selection 
df_selection = df.query(
 "destination == @destination & passanger == @passanger & weather == @weather & time == @time & coupon == @coupon & expiration == @expiration & gender == @gender & maritalStatus == @maritalStatus & education == @education & occupation == @occupation & income == @income & Bar == @Bar & CoffeeHouse == @CoffeeHouse & CarryAway == @CarryAway"
   )



st.dataframe(df_selection)

#MAIN Page stat
st.title("Some Statistic information about the Acceptance and each Atribute")
#st.markdown("##")

#avr_age = round(df["age"].mean(),2)
##avr_temp = round(df["temperature"].mean(),2)
#left_column, middle_column, right_column = st.columns(3)

#fig_income_dir2 = px.scatter(income_dir2, x=income_dir2.index,y="Y",title="Acceptance By the income (PLOT)",template='plotly_white')

#st.plotly_chart(fig_income_dir2)

#income_dir3 = (df_selection.groupby(by="income").sum()[['Y']])

#fig_income_dir3 = px.pie(income_dir3, names=income_dir3.index,values="Y",title="Acceptance By the income (PIE CHART)")

#st.plotly_chart(fig_income_dir3)


# Build the visuals 
##
## need to focus on the accpetence of the coupons so use all with Y in the first place 
edu_dir = (df_selection.groupby(by=["education"]).sum()[["Y"]])

fig_edu_dir = px.bar(edu_dir,x='Y',y=edu_dir.index,orientation='h',title='Acceptance with education',template='plotly_white')

st.plotly_chart(fig_edu_dir)

fig_edu_dir3 = px.pie(edu_dir, names=edu_dir.index,values="Y",title="Acceptance By education (PIE CHART)")
st.plotly_chart(fig_edu_dir3)

## names of the build by: destination, passanger, weather,time
## coupon, expiratoin, gender, maritalStatus, occupation
## income, 


# By distination
dest_dir = (df_selection.groupby(by="destination").sum()[['Y']]).sort_values(by="Y")

fig_dest_dir = px.bar(dest_dir, x='Y', y=dest_dir.index,orientation="h",title="Acceptance with destination",template='plotly_white')

st.plotly_chart(fig_dest_dir)

fig_dest_dir2 = px.pie(dest_dir, names=dest_dir.index,values="Y",title="Acceptance By destination (PIE CHART)")
st.plotly_chart(fig_dest_dir2)






# By Passanger
pass_dir = (df_selection.groupby(by="passanger").sum()[['Y']])

fig_pass_dir = px.bar(pass_dir, x="Y",y=pass_dir.index, orientation="h",title="Acceptance with passanger type",template='plotly_white')

st.plotly_chart(fig_pass_dir)

fig_pass_dir2 = px.pie(pass_dir, names=pass_dir.index,values="Y",title="Acceptance By passanger (PIE CHART)")
st.plotly_chart(fig_pass_dir2)

# By Weather

weath_dir = (df_selection.groupby(by="weather").sum()[['Y']])

fig_weath_dir = px.bar(weath_dir, x="Y",y=weath_dir.index, orientation="h",title="Acceptance with weather type",template='plotly_white')

st.plotly_chart(fig_weath_dir)

fig_weath_dir2 = px.pie(weath_dir, names=weath_dir.index,values="Y",title="Acceptance By Weather (PIE CHART)")
st.plotly_chart(fig_weath_dir2)

# By time

time_dir = (df_selection.groupby(by="time").sum()[['Y']])

fig_time_dir = px.bar(time_dir, x="Y",y=time_dir.index, orientation="h",title="Acceptance with TIME type",template='plotly_white')

st.plotly_chart(fig_time_dir)

fig_time_dir2 = px.pie(time_dir, names=time_dir.index,values="Y",title="Acceptance By Time (PIE CHART)")
st.plotly_chart(fig_time_dir2)

# BY coupon

coupon_dir = (df_selection.groupby(by="coupon").sum()[['Y']])

fig_coupon_dir = px.bar(coupon_dir, x="Y",y=coupon_dir.index, orientation="h",title="Acceptance with The coupon type",template='plotly_white')

st.plotly_chart(fig_coupon_dir)

fig_coupon_dir2 = px.pie(coupon_dir, names=coupon_dir.index,values="Y",title="Acceptance By Coupon (PIE CHART)")
st.plotly_chart(fig_coupon_dir2)

# By expiratoin

expa_dir = (df_selection.groupby(by="expiration").sum()[['Y']])

fig_expa_dir = px.bar(expa_dir, x="Y",y=expa_dir.index, orientation="h",title="Acceptance with The expiration",template='plotly_white')

st.plotly_chart(fig_expa_dir)


fig_expa_dir2 = px.pie(expa_dir, names=expa_dir.index,values="Y",title="Acceptance By expiration (PIE CHART)")
st.plotly_chart(fig_expa_dir2)


# By gender

gender_dir = (df_selection.groupby(by="gender").sum()[['Y']])

fig_gender_dir = px.bar(gender_dir, x="Y",y=gender_dir.index, orientation="h",title="Acceptance with The gender",template='plotly_white',barmode='group')

st.plotly_chart(fig_gender_dir)

fig_gender_dir2 = px.pie(gender_dir, names=gender_dir.index,values="Y",title="Acceptance By gender (PIE CHART)")
st.plotly_chart(fig_gender_dir2)


#maritalStatus, occupation
## income, 


# By marital Status

maritalStatus_dir = (df_selection.groupby(by="maritalStatus").sum()[['Y']])

fig_marstat_dir = px.bar(maritalStatus_dir, x="Y",y=maritalStatus_dir.index, orientation="h",title="Acceptance with The Marital Status",template='plotly_white',barmode='group')

st.plotly_chart(fig_marstat_dir)

fig_marstat_dir2 = px.pie(maritalStatus_dir, names=maritalStatus_dir.index,values="Y",title="Acceptance By Status (PIE CHART)")
st.plotly_chart(fig_marstat_dir2)


# By Occupation

occ_dir = (df_selection.groupby(by="occupation").sum()[['Y']])

fig_occ_dir = px.bar(occ_dir, x="Y",y=occ_dir.index, orientation="h",title="Acceptance By the occupation",template='plotly_white',barmode='group')

st.plotly_chart(fig_occ_dir)

occ_dir = (df_selection.groupby(by="occupation").sum()[['Y']])

fig_occ_dir = px.scatter(occ_dir, x="Y",y=occ_dir.index, orientation="h",title="Acceptance By the occupation (PLOT)",template='plotly_white')

st.plotly_chart(fig_occ_dir)

fig_occ_dir2 = px.pie(occ_dir,names=occ_dir.index,values="Y",title="Acceptance By the occupation (PIE CHART)")

st.plotly_chart(fig_occ_dir2)


# By income 

income_dir = (df_selection.groupby(by="income").sum()[['Y']])

fig_income_dir = px.bar(income_dir, x="Y",y=income_dir.index,title="Acceptance By the income",template='plotly_white',barmode='group')

st.plotly_chart(fig_income_dir)

income_dir2 = (df_selection.groupby(by="income").sum()[['Y']])

fig_income_dir2 = px.scatter(income_dir2, x=income_dir2.index,y="Y",title="Acceptance By the income (PLOT)",template='plotly_white')

st.plotly_chart(fig_income_dir2)

income_dir3 = (df_selection.groupby(by="income").sum()[['Y']])

fig_income_dir3 = px.pie(income_dir3, names=income_dir3.index,values="Y",title="Acceptance By the income (PIE CHART)")

st.plotly_chart(fig_income_dir3)


img = Image.open("C:/Users/serry/Desktop/DataScience/projects/images/time.PNG")

st.image(img)

img2 = Image.open("C:/Users/serry/Desktop/DataScience/projects/images/temperature.PNG")

st.image(img2)

img3 = Image.open("C:/Users/serry/Desktop/DataScience/projects/images/has_child.PNG")

st.image(img3)


img4 = Image.open("C:/Users/serry/Desktop/DataScience/projects/images/dest.PNG")

st.image(img4)



#df_selection

fig = plt.figure()
df_selection[["temperature"]].value_counts().plot(kind="bar")
st.pyplot(fig)
fig = plt.figure()
df_selection[["destination"]].value_counts().plot(kind="bar")
st.pyplot(fig)
fig = plt.figure()
df_selection[["passanger"]].value_counts().plot(kind="bar")
st.pyplot(fig)
fig = plt.figure()
df_selection[["weather"]].value_counts().plot(kind="bar")
st.pyplot(fig)
fig = plt.figure()
df_selection[["time"]].value_counts().plot(kind="bar")
st.pyplot(fig)
fig = plt.figure()
df_selection[["coupon"]].value_counts().plot(kind="bar")
st.pyplot(fig)
fig = plt.figure()
df_selection[["expiration"]].value_counts().plot(kind="bar")
st.pyplot(fig)
fig = plt.figure()
df_selection[["gender"]].value_counts().plot(kind="bar")
st.pyplot(fig)
fig = plt.figure()
df_selection[["age"]].value_counts().plot(kind="bar")
st.pyplot(fig)
fig = plt.figure()
df_selection[["maritalStatus"]].value_counts().plot(kind="bar")
st.pyplot(fig)


# kde, bar 

# a very good course https://www.youtube.com/watch?v=4it828NLuIk

    # the answers of the modeling 

# before CV
# KNN 71 
# RF 77

# after CV 

# KNN 69
# RF 70.5











imge12 = Image.open("C:/Users/serry/Desktop/DataScience/projects/images/prec.PNG")

st.image(imge12)
