import pandas as pd
from sklearn.linear_model import LinearRegression

# read the csv
df = pd.read_csv(r'playerdata.csv')


# start a GUI
from tkinter import *
root = Tk()
root.title('2K21 Prediction')

def test(*entry):
    df = pd.read_csv(r'playerdata.csv')
    POS, INS, OUT, PLY = entry[0], int(entry[1]), int(entry[2]), int(entry[3])
    ATH, DEF, REB = int(entry[4]), int(entry[5]), int(entry[6])

    # choose position
    if POS == 'PG':
        df = df[df["POS"] == "PG"]
    elif POS == 'SG':
        df = df[df["POS"] == "SG"]
    elif POS == 'SF':
        df = df[df["POS"] == "SF"]
    elif POS == 'PF':
        df = df[df["POS"] == "PF"]
    elif POS == 'C':
        df = df[(df["POS"] != "PG") & (df["POS"] != "SG") & (df["POS"] != "SF") &
        (df["POS"] != "PF")]

    # selecting targets
    X = df.drop(['Name', 'OVR', 'POS'], axis=1)
    y = df.OVR

    # create model
    reg = LinearRegression().fit(X, y)

    # print the prediction
    predict = reg.predict([[INS,OUT,PLY,ATH,DEF,REB]])
    predict = round(predict[0])
    pre = Label(root,text='Predicted rating: '+str(predict), font=60)
    pre.grid(row=14, column=0)


label1 = Label(root, text="Enter the player's position (PG/SG/SF/PF/C): ")
label2 = Label(root, text="Enter the Inside scoring rating: ")
label3 = Label(root, text="Enter the Outside scoring rating: ")
label4 = Label(root, text="Enter the Playmaking rating: ")
label5 = Label(root, text="Enter the Athleticism rating: ")
label6 = Label(root, text="Enter the Defending rating: ")
label7 = Label(root, text="Enter the Rebounding rating: ")

x=5
y=5
label1.grid(row=0, column=0, padx=x, pady=y)
label2.grid(row=2, column=0, padx=x, pady=y)
label3.grid(row=4, column=0, padx=x, pady=y)
label4.grid(row=6, column=0, padx=x, pady=y)
label5.grid(row=8, column=0, padx=x, pady=y)
label6.grid(row=10, column=0, padx=x, pady=y)
label7.grid(row=12, column=0, padx=x, pady=y)


a=5
b=10
e1 = Entry(root, width=a)
e1.grid(row=0,column=1, padx=b)
e2 = Entry(root, width=a)
e2.grid(row=2,column=1, padx=b)
e3 = Entry(root, width=a)
e3.grid(row=4,column=1, padx=b)
e4 = Entry(root, width=a)
e4.grid(row=6,column=1, padx=b)
e5 = Entry(root, width=a)
e5.grid(row=8,column=1, padx=b)
e6 = Entry(root, width=a)
e6.grid(row=10,column=1, padx=b)
e7 = Entry(root, width=a)
e7.grid(row=12,column=1, padx=b)

button = Button(root, text='Predict', padx=20, pady=10,
                command=lambda: test(
                    e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), e7.get()))
button.grid(row=14,column=1, padx=30, pady=15)


root.mainloop()









