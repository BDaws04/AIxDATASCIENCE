import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import pearsonr

"""
The purpose of this file is to test for patterns so I can most accurately create the prediction model
"""

def generalData():
     data = pd.read_csv("C:/Users/hp/Desktop/GitHub-Projects/MACHINELEARNING + AI/StudentGradeCalculator/student-mat.csv", sep=';') 
     print(data['G3'].mean()) #10.415189873417722
     print(data['G3'].median()) #11.0
     print(data['G3'].std()) #4.5814426109978434
     print(data['G3'].var()) #20.989616397866733

#Notes: no correlation between absences and grades
def linearRegressionTest():
    data = pd.read_csv("C:/Users/hp/Desktop/GitHub-Projects/MACHINELEARNING + AI/StudentGradeCalculator/student-mat.csv", sep=';')
    absences = data['absences']
    grade = data['G3']

    r_value, p_value = pearsonr(absences, grade)
    print(r_value) #0.03424731615006936
    print(p_value) #0.4973317955435264

    plt.figure(figsize=(8, 6))
    plt.scatter(absences, grade, color='blue', alpha=0.5)
    plt.title('Scatter Plot of Absences vs Grade')
    plt.xlabel('Absences')
    plt.ylabel('Grade (G3)')
    plt.grid(True)
    plt.show()

#Minimal correlation found. 
#GO-OUT 2-3 gave best results
#Free-Time 2 or 5 was signifincatly better
#**Famrel follows a general uptrend**
#**Medu and Fedu - Lowest score performs the best, after that follows a general up-trend**
#**Traveltime - grades consistently decrease as traveltime increasesm**
#**Studytime - grades increase until level 4, where they ever so slightly decrease**
def averageLinearRegressionTest():
     """
     Headers to be tested: ['famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health']
     """
     data = pd.read_csv("C:/Users/hp/Desktop/GitHub-Projects/MACHINELEARNING + AI/StudentGradeCalculator/student-mat.csv", sep=';') 
     desired_columns = ['Medu', 'Fedu','famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'traveltime', 'studytime']

     for column in desired_columns:
        average_scores = data.groupby(column)['G3'].mean()
        print(average_scores)


#Minimal effects for: activities
#GP, M, U, LE3, A, no, no, yes, yes, yes, yes, no performed the best.
#school, sex, address, famsize, pstatus, schoolsup, paid, higher, internet, relationship were significant
#Higher and internet were the largest indicators
def binaryDataTests():
     data = pd.read_csv("C:/Users/hp/Desktop/GitHub-Projects/MACHINELEARNING + AI/StudentGradeCalculator/student-mat.csv", sep=';') 
     desired_columns = ['school','sex','address', 'famsize', 'Pstatus', 'schoolsup', 'famsup','paid', 'activities', 'nursery', 'higher', 'internet', 'romantic']

     for column in desired_columns:
         average_scores = data.groupby(column)['G3'].mean()
         print(average_scores)


