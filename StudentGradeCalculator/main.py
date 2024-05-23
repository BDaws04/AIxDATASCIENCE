import pandas as pd 
import matplotlib.pyplot as plt 
from scipy import stats


def load_data():
    try: 
       data = pd.read_csv("C:/Users/hp/Desktop/GitHub-Projects/MACHINELEARNING + AI/StudentGradeCalculator/student-mat.csv", sep=';')
       return data
    except FileNotFoundError:
        print("Unable to read file")
        exit(0)

"""
Explanation of model:
- Begins by calculating the grade using linear regression, based on travel_time and famrel
- Then adjusts the score based on the standard deviation and the other factors which are known to heavily influence the score
"""

def model(gender, school, travel_time, famrel, higher, internet):
    data = load_data()

    standard_deviation = data['G3'].std()
   
    average_tt = data.groupby('traveltime')['G3'].mean()
    average_fr = data.groupby('famrel')['G3'].mean()

    grade = (average_tt.loc[travel_time] + average_fr.loc[famrel]) / 2

    modifier = 0

    if gender == 'M':
        modifier += 0.15
    else:
        modifier -= 0.15

    if school == 'Gp':
        modifier += 0.2
    else:
        modifier -= 0.2

    if higher == 'yes':
        modifier += 0.5
    else:
        modifier -= 0.5

    if internet == 'yes':
        modifier += 0.15
    else:
        modifier -= 0.15
    
    return grade + (modifier * standard_deviation)

    
#Test input 
print(model('M', 'Gp', 2, 3, 'yes', 'no'))
