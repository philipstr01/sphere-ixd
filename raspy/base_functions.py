from pathlib import Path
import limepy as lp
import pandas as pd

def download_write_responses(sid=287768,filename="responses.csv"):
    try:
        f = open('data/'+filename, "x")
        f.close()
    except FileExistsError:
        pass
    csv = lp.get_responses("https://testteamotional.limesurvey.net/admin/remotecontrol", "girim00", "TreamDream23", 1, sid)
    path = Path('data/'+filename)
    path.write_text(csv)


#Not working at the moment
def getSurveyObject(filename="responses.csv",language=None):
    df = pd.read_csv('data/'+str(filename), sep=';')
    with open('data/structure.lss') as f: #Structure needs to be downloaded manually
        my_structure = f.read()
    return Survey(df, my_structure) #Error in function Code

def getsurveyDataframe(filename="responses.csv",language=None):
    return pd.read_csv('data/'+str(filename), sep=';')

def getMeansCSV(df):
    ls = []
    question_columns = ["G01Q01","G01Q02","G01Q03"]
    for id in question_columns:
        ls += df[i].mean()
    return ls
