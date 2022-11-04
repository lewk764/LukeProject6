################ Provided Function Definitions ################

# Shows the user what options they have
def displayMenu():

  # This option will involve you adding a student and a collection for their grades to a dictionary!
  print("1. Add a Student")

  # This option will involve you removing a pair from a dictionary!
  print("2. Remove a Student")

  # This option will require you to grab a student from a dictionary and add a quiz grade to it's corresponding collection of grades!
  # You'll also need to use a pre-written function that ensures the user is entering a valid grade (a decimal number)
  print("3. Add Quiz Grade for Student")

  # This option will require you to use a loop to list all of the grades for an INDIVIDUAL student!
  print("4. List a Student's Quiz Grades")

  # This option will have you write a function that takes in a student's grade as a number and return the letter grade equivalent!
  print("5. Get Student's Letter Grade")

  print("6. Quit")

# Prompts the user to enter a numeric grade
# This function works, and ensures the user entered a valid float for the grade
# It's not important HOW this function works, but how to USE this function
def getNumberGradeFromUser():

  val = None

  while(val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None
  
  return val

  ################ My Function Definitions ################

#Adds a specified student to the dictionary
def addStudent(dictionary):
  
  print()
  #Prompt for a student to add
  studentName = input("Enter student name: ")
  
  #Add the given student name to the dictionary; overwrites existing students of same name!
  #Key == studentName | Value == empty list
  dictionary[studentName] = []

  #Confirm that the student has been added
  print(f"{studentName} added!")

#Removes a specified student from the dictionary
def removeStudent(dictionary):
  print()
  
  #Prompt for student to remove
  studentName = input("Enter name of student to remove: ")

  #if student is in the dict, remove them
  if studentName in dictionary:
    dictionary.pop(studentName)
    print(f"{studentName} removed!")
  #If student isn't in dict, tell the user
  else:
    print(f"{studentName} is not in the list of students!")

#Adds a quiz grade to the student in the dictionary
def addQuiz(dictionary):
  print()

  #Prompt for a student to add a grade for
  studentName = input("Enter name of student: ")

  #If student is in the list, proceede with adding a grade
  if studentName in dictionary:
    #Prompt for a grade
    grade = getNumberGradeFromUser()
    #Add grade to the list value of the specified student in the dictionary
    dictionary[studentName].append(grade)
    print(f"Added {grade} to {studentName}'s quizzes")

  #If student doesn't exist, tell user
  else:
    print(f"{studentName} is not in the list of students!")

#Lists the quiz grades for the specified student
def listQuiz(dictionary):
  print()

  #Prompt for a student to list the quiz grades of
  studentName = input("Enter name of student: ")

  #If student is in the list, proceede
  if studentName in dictionary:
    print()
    print(f"{studentName}'s Quiz Grades:")
    for grade in dictionary[studentName]:
      print(grade)
      
  #If student doesn't exist, tell user
  else:
    print(f"{studentName} is not in the list of students!")

#Calculate the letter grade based on student's quiz scores
def calcLetterGrade(dictionary):
  print()

  #Prompt for a student
  studentName = input("Enter name of student: ")

  #If student is in the list, proceede
  if studentName in dictionary:
    print()

    #Calculate average of student's grades
    sumOfGrades = 0
    numOfGrades = 0
    for grade in dictionary[studentName]:
      sumOfGrades += grade
      numOfGrades += 1
    
    averageGrade = sumOfGrades / numOfGrades

    #Determine letter grade based on average
    if averageGrade >= 90:
      letterGrade = "A"

    elif averageGrade >= 80:
      letterGrade = "B"

    elif averageGrade >= 70:
      letterGrade = "C"

    elif averageGrade >= 60:
      letterGrade = "D"

    elif averageGrade >= 50:
      letterGrade = "E"

    elif averageGrade < 50:
      letterGrade = "F"

    #Print studen't letter grade
    print(f"{studentName}'s current grade is a {letterGrade}")
    
      
  #If student doesn't exist, tell user
  else:
    print(f"{studentName} is not in the list of students!")



################ Main Program ################

#Program Icon
print("""
   ____               _        ____              _    
  / ___|_ __ __ _  __| | ___  | __ )  ___   ___ | | __
 | |  _| '__/ _` |/ _` |/ _ \ |  _ \ / _ \ / _ \| |/ /
 | |_| | | | (_| | (_| |  __/ | |_) | (_) | (_) |   < 
  \____|_|  \__,_|\__,_|\___| |____/ \___/ \___/|_|\_\
                                                      
""")
# Default variables / other info

menuOption = ""
studentDict = {}
  
# Application Loop
while(menuOption != "6"):

  # Prompt the user to select an option
  print()
  displayMenu()
  menuOption = input("Select an Option: ")

  #Option 1: Add a student
  if menuOption == "1":
    addStudent(studentDict)

  #Option 2: Remove a student
  elif menuOption == "2":
    removeStudent(studentDict)

  #Option 3: Add a quiz grade for a student
  elif menuOption == "3":
    addQuiz(studentDict)

  #Option 4: List a student's quiz grades
  elif menuOption == "4":
    listQuiz(studentDict)

  #Option 5: Get student's letter grade
  elif menuOption == "5":
    calcLetterGrade(studentDict)

#End of application loop (exiting)
print("Program ended.")
print("""
   ____                 _ _                _ 
  / ___| ___   ___   __| | |__  _   _  ___| |
 | |  _ / _ \ / _ \ / _` | '_ \| | | |/ _ \ |
 | |_| | (_) | (_) | (_| | |_) | |_| |  __/_|
  \____|\___/ \___/ \__,_|_.__/ \__, |\___(_)
                                |___/       
""")
