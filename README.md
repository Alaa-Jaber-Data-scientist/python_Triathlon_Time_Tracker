# Triathlon Time Tracker

This program calculates the total time taken to complete a triathlon based on the individual timings for swimming, cycling, and running. It also determines the type of award based on the qualifying time.

## Features:
- Input the timings for swimming, cycling, and running in minutes.
- Calculate the total time by summing up the individual timings.
- Compare the total time with the qualifying time to determine the award category.
- Awards are categorized as follows:
  - If the total time is less than or equal to the qualifying time: Provincial Colours
  - If the total time is within 5 minutes of the qualifying time: Provincial Half Colours
  - If the total time is within 10 minutes of the qualifying time: Provincial Scroll
  - If the total time exceeds the qualifying time by more than 10 minutes: No award

## Usage:
1. Run the program.
2. Enter the timings for swimming, cycling, and running when prompted.
3. The program will calculate the total time and display it.
4. The program will determine the award category based on the total time and display the corresponding award.

Note: The qualifying time is set to 100 minutes by default. Modify the `qualifying_time` variable in the code if necessary.
