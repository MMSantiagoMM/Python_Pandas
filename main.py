import pandas as pd;
import numpy as np;
import itertools;


names = [
    'John', 'Emily', 'Michael', 'Sophia', 'David', 'Olivia', 'James', 'Ava', 'William', 'Isabella',
    'Benjamin', 'Mia', 'Samuel', 'Charlotte', 'Ethan', 'Amelia', 'Alexander', 'Harper', 'Daniel', 'Evelyn',
    'Matthew', 'Abigail', 'Joseph', 'Emily', 'Andrew', 'Scarlett', 'Jackson', 'Grace', 'Henry', 'Elizabeth',
    'Gabriel', 'Sofia', 'David', 'Victoria', 'Noah', 'Avery', 'Christopher', 'Lily', 'Isaac', 'Ella',
    'Samuel', 'Chloe', 'Benjamin', 'Stella', 'Jack', 'Hannah', 'Nathan', 'Aubrey', 'Caleb', 'Zoey',
    'Luke', 'Lillian', 'Owen', 'Natalie', 'Ryan', 'Addison', 'Isaac', 'Brooklyn', 'Daniel', 'Savannah',
    'Matthew', 'Zoe', 'Levi', 'Leah', 'Anthony', 'Audrey', 'Julian', 'Bella', 'Adam', 'Claire',
    'Eli', 'Nora', 'Zachary', 'Lucy', 'Thomas', 'Samantha', 'Connor', 'Eleanor', 'Hunter', 'Penelope',
    'Christian', 'Anna', 'Aaron', 'Violet', 'Caleb', 'Hazel', 'Adrian', 'Aurora', 'Eli', 'Paisley',
    'Jeremiah', 'Skylar', 'Colton', 'Ellie', 'Charles', 'Sarah', 'Josiah', 'Caroline', 'Hudson', 'Sadie'
]

# Last names
last_names = [
    'Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Anderson', 'Taylor',
    'Thomas', 'Moore', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson',
    'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King',
    'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson', 'Carter',
    'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Collins',
    'Stewart', 'Sanchez', 'Morris', 'Rogers', 'Reed', 'Cook', 'Morgan', 'Bell', 'Murphy', 'Bailey',
    'Rivera', 'Cooper', 'Richardson', 'Cox', 'Howard', 'Ward', 'Torres', 'Peterson', 'Gray', 'Ramirez',
    'James', 'Watson', 'Brooks', 'Kelly', 'Sanders', 'Price', 'Bennett', 'Wood', 'Barnes', 'Ross',
    'Henderson', 'Coleman', 'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson', 'Hughes', 'Flores', 'Washington',
    'Butler', 'Simmons', 'Foster', 'Gonzales', 'Bryant', 'Alexander', 'Russell', 'Griffin', 'Diaz', 'Hayes'
]

# Ages
ages = np.random.randint(18,60 , size=100)

# Subjects
subjectsList = [
    'Math', 'Science', 'History', 'English', 'Physics', 'Chemistry', 'Biology', 'Geography', 'Computer Science', 'Art',
    'Literature', 'Music', 'Physical Education'
]

subjects = list(itertools.islice(itertools.cycle(subjectsList), 100))

# Grades
grades = np.random.randint(50, 101, size=100)



data = {
    'Name': names,
    'Last Name': last_names,
    'Age': ages,
    'Subject': subjects,
    'Grade': grades
}


df = pd.DataFrame(data)

df.to_csv('studentData.csv', index=False)
df.describe()


averageAge = df.iloc[:,2].mean()

print(averageAge)

youngerStudent = df.iloc[:,2].min()
print(df.loc[youngerStudent,'Name'])

olderStudent = df.iloc[:,2].max()
print(df.loc[olderStudent,'Name'])

tenStudentBestGrades = df.nlargest(10,'Grade')['Name']
print(tenStudentBestGrades)

studentPerSubject = df['Subject'].value_counts()
print(studentPerSubject)


subjectGradeLower = df['Grade'].min()
print(df.loc[subjectGradeLower,'Subject'], subjectGradeLower)

subject_with_highest_grade = df.loc[df['Grade'].idxmax(), 'Subject']
highest_grade = df['Grade'].max()
print(subject_with_highest_grade, highest_grade)

averageGrade = df.iloc[:,4].mean()
print(averageGrade)

studentsWhoGain = (df['Grade']>=60).sum()
print(studentsWhoGain)

studentsWhoLose = (df['Grade']<60).sum()
print(studentsWhoLose)


math_df = df[df['Subject'] == 'Math']

best_student_math = math_df.loc[math_df['Grade'].idxmax(), ['Name', 'Grade']]

print(best_student_math.values)


history_df = df[df['Subject'] == 'History']

best_student_history = history_df.loc[history_df['Grade'].idxmax(), ['Name', 'Grade']]

print(best_student_history.values)


filtered_df = df[(df['Age'] >= 30) & (df['Age'] <= 40)]
print(filtered_df.shape[0])

