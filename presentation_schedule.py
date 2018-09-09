__author__ = 'sofiat'
 import csv
 """
A program that assigns students to courses for presentation during the Review phase at AIMS-Ghana, 2015.
The algorithm is deterministic, students are assigned courses according to how early their response was received.
Each students has an opportunity to choose up to 3 courses from most preferred to least preferred, and the algorithm
assigns students to their preference accordingly, with the condition that not more than 3 students can be assigned
to a course. Thus if a student's most preferred course is not available, they are assigned to their least preferred...
"""
 # a dictionary that keeps all the courses available during the review phase.
courses = {'A': 'Quantum Computing', 'B': 'Modern topics in algebra', 'C': 'Complex Analysis',
           'D': 'Complex Networks with Computations', 'E': 'Introduction to Finance', 'F': 'Functional Analysis',
           'G': 'Ordinary Differential Equations', 'H': 'Combinatorial Algebraic Topology', 'I': 'Solitons',
           'J': 'The mysterious affair of exp(π * sqrt(163))', 'K': 'Statistics', 'L': 'Biological Physics',
           'M': 'Analytic Number Theory', 'N': 'Dynamical Systems', 'O': 'Introduction to Quantum Field Theory',
           'P': 'Pattern Recognition and Machine Learning', 'Q': 'Special and General Relativity', 'R': 'Galois Theory'}
 def read_file():
    """
    this function reads the students responses from the text file into a dictionary
    """
    f = open('responses.csv').read().split('\n')[4:]
    database = {}  # point each student to their choice
    students = []  # keep track of 48 students according to how their response was received
    for line in f:
        temp = line.split(',')  # a students parameter
        email = temp[-1]  # get the email
        username = email[0:email.find('@')]  # get the username before the @
        students.append(username)
        database[username] = [temp[i][0] for i in range(1, len(temp)-1)]  # get the three choices and store
        # accordingly
    return database, students
 def make_schedule():
    """
    This function makes the schedule, ensuring that not more than 3 students are assigned to a course.
    :return: returns the course and the students assigned to it. it also returns the students without assignment.
    """
    database, students = read_file()
    schedule = {}  # dictionary that keeps the scheduling
    no_assignment = []  # keep track of students that cannot be assigned
    for name in students:  # pick each student according to how their response was received
        choice = database[name]  # temporarily store the choice of each students [E, N, F]
        for i in range(0, len(choice)):  # to make a key for every students choice in the schedule dictionary
            if choice[i] not in schedule:  # if the course is not in the schedule,
                schedule[choice[i]] = []  # point it to an empty set to keep the first 3 students that selected it
         i = 0  # this counts the first, second and third preference,
        while True:
            try:
                if len(schedule[choice[i]]) != 3:  # if the student's i-th option has not been assigned to 3 students
                    schedule[choice[i]].append(name)  # assign the course to the student
                    break  # pick another student....
            except IndexError:  # if the student cannot be assigned, i.e. all the options are filled.
                no_assignment.append(name)
                break
            i += 1  # else, increment the preference
    return schedule, no_assignment
 # schedule, no_assignment = make_schedule()
# print(no_assignment)
# for key in schedule:
#     if len(schedule[key]) != 0:
#         for student in schedule[key]:
#             print(student, '==>', courses[key])
#
 def write_to_csv():
    """
    We proceed to write the schedule to a csv file.
    :return: csv file is stored as assignment.csv on the directory.
    """
    schedule, no_assignment = make_schedule()
    t = open('assignment.csv', 'w', newline='')
    target = csv.writer(t)
    for key in schedule:
        if len(schedule[key]) != 0:
            target.writerow([courses[key] + ' ==>', schedule[key]])
     target.writerow([''])
    target.writerow(['Students with no assignment'])
    for name in no_assignment:
        target.writerow([name])
    del target
    t.close()
 if __name__ == '__main__':
     write_to_csv()
