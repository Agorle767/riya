# # Creating a csv file

import csv

 

# data = [

#     ['ID', 'Name', 'Age'],

#     [0, 'Riya', 10],

#     [1, 'Ram', 9],

#     [2, 'Sindhu', 15],

#     [3, 'Aditya', 14],

#     [4, 'Bhavani', 80],

#     [5, 'Rajesh', 79]

# ]

 

# myfile = open('C:/Python/input_csv.csv','w',newline='')

# csvwriter = csv.writer(myfile,delimiter=',')

# csvwriter.writerows(data)

# myfile.close()

 



 

def bubble_sort_by_age(file_path):

    with open(file_path, 'r') as file:

        reader = csv.reader(file)

        rows = list(reader)

 

   

    header = rows[0]

    data = rows[1:]

 

   

    age_index = 1  

 

   

    numeric_data = []

    non_numeric_rows = []

 

    for row in data:

        try:

           

            row[age_index] = int(row[age_index])

            numeric_data.append(row)

        except ValueError:

           

            non_numeric_rows.append(row)

 

   

    for i in range(len(numeric_data)):

        for j in range(0, len(numeric_data) - i - 1):

            # Swap rows if the current row's age is greater than the next row's age

            if numeric_data[j][age_index] > numeric_data[j + 1][age_index]:

                numeric_data[j], numeric_data[j + 1] = numeric_data[j + 1], numeric_data[j]

 

   

    sorted_data = [header] + numeric_data + non_numeric_rows  

 

   

    with open('C:/Python/sorted_output.csv', 'w', newline='') as file:

        writer = csv.writer(file)

        writer.writerows(sorted_data)
 

    print("Data sorted by age and written to 'sorted_output.csv'. Non-numeric rows were skipped during sorting.")

 

bubble_sort_by_age('C:/Python/input_csv.csv')