from pathlib import Path
import limepy as lp
import pandas as pd

def download_write_responses(sid=419977,filename="responses.csv"):
    try:
        f = open('data/'+filename, "x")
        f.close()
    except FileExistsError:
        pass
    csv = lp.download.get_responses("https://userpage.fu-berlin.de/~girim00/survey/limesurvey/index.php/admin/remotecontrol", "admin", "password", 1, sid)
    path = Path('data/'+filename)
    path.write_text(csv)

#Not working at the moment
def getSurveyObject(filename="responses.csv",language=None):
    df = pd.read_csv('data/'+str(filename), sep=';')
    with open('data/structure.lss') as f: #Structure needs to be downloaded manually
        my_structure = f.read()
    return lp.wrangle.Survey(df, my_structure) #Error in function Code

def getsurveyDataframe(filename="responses.csv",language=None):
    return pd.read_csv('data/'+str(filename), sep=';')

def getMeansCSV(df):
    ls = []
    question_columns = ["G01Q01","G01Q02","G01Q03"]
    for id in question_columns:
        ls += df[i].mean()
    return ls

#Für jede Frage, den Durschnitt der Ergebnisse als Float. Wobei Antworten die älter als eine halbe Stunde sind ignoriert werden.
import pandas as pd
import spheremain as spm
import datetime
from datetime import datetime, timedelta


spm.download_write_responses() 
responses_file = spm.getsurveyDataframe() 
responses_file.dropna(how= 'all')


def selectTime(df_resp):
    # for exhibition purposes only display the last 30min of responses
    timediff = timedelta(minutes=30)
    
    #drop responses without submitdate
    
    df_resp= df_resp.dropna(subset=['submitdate'])
    df_resp = df_resp.reset_index(drop=True)

    for i in range(0,len(df_resp['submitdate'])):

        datetimestr = str(df_resp['submitdate'][i])
        datetime_object = datetime.strptime(datetimestr, '%Y-%m-%d %H:%M:%S')
        ct = datetime.now()-datetime_object
       
        if datetime.now()-datetime_object >= timediff:
            df_resp=df_resp.drop(i)
            
        
    return df_resp


def calcMeans(df_resp):
    df_resp = selectTime(df_resp)
    df_resp.dropna(how= 'all')

    # first question [0,4]
    sum = 0
    count = (df_resp['q1[SQ001]']=='Y').sum()
    sum += count*0.
    count = (df_resp['q1[SQ002]']=='Y').sum()
    sum += count*0.25
    count = (df_resp['q1[SQ003]']=='Y').sum()
    sum += count*0.5
    count = (df_resp['q1[SQ004]']=='Y').sum()
    sum += count*0.75
    count = (df_resp['q1[SQ005]']=='Y').sum()
    sum += count*1.
    
    mean1 = sum / len(df_resp['q1[SQ005]'])
    
    # second question 
    sum = 0
    count = (df_resp['q2[SQ001]']=='Y').sum()
    sum += count*0.
    count = (df_resp['q2[SQ002]']=='Y').sum()
    sum += count*0.25
    count = (df_resp['q2[SQ003]']=='Y').sum()
    sum += count*0.5
    count = (df_resp['q2[SQ004]']=='Y').sum()
    sum += count*0.75
    count = (df_resp['q2[SQ005]']=='Y').sum()
    sum += count*1.
    
    mean2 = sum / len(df_resp['q1[SQ005]'])

    # third question 
    sum = 0
    count = (df_resp['q3[SQ001]']=='Y').sum()
    
    sum += count*0.
    count = (df_resp['q3[SQ002]']=='Y').sum()
    
    sum += count*0.25
    count = (df_resp['q3[SQ003]']=='Y').sum()
    
    sum += count*0.5
    count = (df_resp['q3[SQ004]']=='Y').sum()
    
    sum += count*0.75
    count = (df_resp['q3[SQ005]']=='Y').sum()
    
    sum += count*1.
    
    mean3 = sum / len(df_resp['q1[SQ005]'])

    return(mean1, mean2, mean3)



