birth_year = None

while birth_year == None: 
    birth_year_input = input("What is your birth year?" )

    if birth_year_input.isdigit(): 
        birth_year = int(birth_year_input)

        age = 2019 - birth_year

        print("You are " + str(age) + " years old.")
    else: 
        print("Enter a valid birth year")
  #  birth_year_question regarding correct age
  
        



    


    