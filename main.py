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
def addStudent(studentName, dictionary):

  #Add the given student name to the dictionary; overwrites existing students of same name!
  #Key == studentName | Value == empty list
  dictionary[studentName] = ()
  
  print(f"{studentName} added!")


  ################ Main Program ################

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
    studentName = input("Enter student name: ")
    addStudent(studentName, studentDict)

  #Option 2: Remove a student
  elif menuOption == "2":
    print("test2")

  #Option 3: Add a quiz grade for a student
  elif menuOption == "3":
    print("test3")

  #Option 4: List a student's quiz grades
  elif menuOption == "4":
    print("test4")

  #Option 5: Get student's letter grade
  elif menuOption == "5":
    print("test5")

#End of application loop (exiting)
print("Program ended.")


### Testing Zone ###
for key, value in studentDict.items():
  print(f"{key} / {value}")