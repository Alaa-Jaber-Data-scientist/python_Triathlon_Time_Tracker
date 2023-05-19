"""
This Python program calculates the total time taken to complete a triathlon
and determines the corresponding award category based on the qualifying time.
It prompts the user to enter the timings for swimming, cycling, and running,
calculates the total time by summing up the individual timings, and compares
it with the qualifying time. The program then displays the total time and the
award category. It provides a straightforward way to track triathlon timings 
and determine the level of achievement based on predefined criteria.
"""

# Prompt the user to enter the timings for swimming, cycling, and running
print("Please enter the following timings in minutes:")

# Get the swimming time from the user
swimming = int(input(" Swimming time: "))

# Get the cycling time from the user
cycling = int(input(" Cycling time: "))

# Get the running time from the user
running = int(input(" Running time: "))

# Calculate the total time by summing up the individual timings
total_time = swimming + cycling + running

# Display the total time taken to complete the triathlon
print("Total time taken to complete the triathlon:", total_time, "minutes")

# Define the qualifying time for awards
qualifying_time = 100

# Compare the total time with the qualifying time and determine the award category
if total_time <= qualifying_time:
    print("The award is: Provincial Colours")  
elif total_time <= qualifying_time + 5:
    print("The award is: Provincial Half Colours")  
elif total_time <= qualifying_time + 10:
    print("The award is: Provincial Scroll")  
else:
    print("No award")  