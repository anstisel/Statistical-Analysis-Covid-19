# Statistical-Analysis-Covid-19
A Python 3 program which reads data from a csv file provided and returns different analytical results of the COVID-19 cases for the entire world. Works by using a dictionary filled with smaller dictionaries, which hold information like lists of total positive cases for each month and total recorded deaths for each month etc . Complete project description provided.
To run:        
python3 Project2.py. 
  
Program will ask you to input a country or a continent of your choosing. The program will analyse the Covid-data.csv file and return a list containing:
  - total number of recorded positive cases of COVID-19 for each month
  - total number of recorded deaths due to COVID-19 for each month
  - total number of days for each month of year, when the recorded postiive cases of COVID-19 for that month were greater than average recorded positive cases of that month of the year
  - total number of days for each month of year, when the recorded deaths due to COVID-19 for that month were greater than average recorded deaths due to COVID-19 for that month of the year
  
Can compare numbers to Project Specification document:     
Note: Numbers for first two lists of oceania have been slightly altered during conversion of csv file. 
Example:  
Afghanistan should yield:  
[[1963, 1, 174, 1952, 13081, 16020, 1681, 1494, 1109, 2157, 4849, 5252], [86, 0, 4, 60, 194, 482, 188, 119, 57, 78, 257, 396], [1, 1, 7, 11, 13, 16, 8, 11, 10, 14, 15, 18], [3, 0, 4, 12, 11, 13, 8, 15, 14, 15, 15, 16]].     
Italy should yield:     
[[169327, 1126, 104664, 99671, 27534, 7729, 6959, 21677, 45647, 364569, 922124, 505612], [4596, 29, 12399, 15539, 5448, 1383, 374, 342, 411, 2724, 16958, 18583], [8, 8, 17, 15, 11, 15, 14, 12, 15, 11, 15, 15], [6, 6, 14, 17, 12, 16, 13, 4, 15, 12, 15, 15]]. 
  
    
