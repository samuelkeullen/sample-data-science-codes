import pandas as pd

#o pandas serve  para análise e manipulação de dados, possui diversas ferramentas para este cunho
#resumindo... Data Analysis

def working_dataframe():
    csv_path = 'new_songes.csv' #store the path of csv
    #df means DataFrame
    df = pd.read_csv(csv_path) #argument to the read_csv function
    df.head()

    # #we can import Excel file too!
    # #xlsx_path = "file1.xlsx"
    # #df = pd.read_excel(xlsx_path)
    # #df.head()
    # #Para criar um DataFrame, é usado um disctionary
    # #a \ é apenas para pular para outra linha
    # #mas a criação do dataframe é simples
    # #'key':['value1','value2']
    # #keys = columns label, value = value of the row
    songs = {'Album': ['Thriller', 'Back in Black', 'The Dark Side of the Moon',\
        'The Bodyguard', 'Bat Out of Hell'],
        'Released': [1982, 1980, 1973, 1992, 1977],
        'Length': ['00:42:19', '00:42:11', '00:42:49', '00:57:44', '00:46:33']} #here I've created the dictionary for the DF
        
    songs_frame = pd.DataFrame(songs) #here I've created the DataFrame
    x = songs_frame[ ['Length']]#here i just retrieve the column 'Length'
    y = songs_frame[ ['Album','Length']]#now multiple columns

    #songs_frame['Released']>=1980 #in this line, i check if is true each value is bigger or equal than 1980

    #creating a new data_frame with the specific values
    s_df = songs_frame[songs_frame['Released']>= 1980]

    c = songs_frame.iloc[0:3, 0]
    #b = songs_frame.loc['The Bodyguard', 'Released']
    a = songs_frame.loc[0:3, 'Album']
    # print("Iloc com numero e letra: ")
    print(a)
    print(c)

    #b = s_df.loc['The Bodyguard', 'Released']
    #print(b)
    #print(c)
    
    #print(songs_frame)
    # m1 = "Here the first Data Frame with only 1 column (Length):\n{}".format(x) 
    # m2 = "Here the second Data Frame with 2 columns (Length and Album):\n{}".format(y)
    # m3 = "And now the original Data Frame:\n{}".format(songs_frame)
    
    # print(m1)
    # print("")
    # print(m2)
    # print("")
    # print(songs_frame)
    # print("")
    #print("New dataframe with the values from the other dataframe:")
    #print(s_df)
    print("Saving the datafram to a CSV file...")
    s_df.to_csv('new_songes.csv')
    print("Done!")


def saving_data():
    print("In this def we will save the data in other formats")

#saving_data()
working_dataframe()