import numpy as np
#np.set_printoptions(threshold=np.nan)
import csv



def main():
    ## Open data file and read values into array
    with open('data/data_train.csv', 'r') as datafile:
        reader = csv.reader(datafile)
        data_list = list(reader)

    # Allocate array for data from file
    data_array = np.zeros(shape=(10000,1000))

    iterate = len(data_list)
    # 0th row is header, so start from row 1
    for i in range(1,iterate):
        # Print progress in %
        if(i%100000==0):
            print(int(i/iterate*100), "%")

        # Extract column, row and value from entry and save data in data_array
        length = len(data_list[i][0])
        place_r = data_list[i][0].find("r")
        place__ = data_list[i][0].find("_")
        place_c = data_list[i][0].find("c")
        row = int(data_list[i][0][place_r + 1:place__])
        column = int(data_list[i][0][place_c + 1:length + 1])
        data_array[row-1][column-1] = data_list[i][1]

    # Calculate mean of all non-zero values for each item (each column)
    a = np.true_divide(data_array.sum(0), (data_array != 0).sum(0)) #everage rating for each item by neglecting zero values

    # Allocate submission list
    submission_array = []

    # Open sampleSubmission file
    with open('data/sampleSubmission.csv', 'r') as subfile:
        reader = csv.reader(subfile)
        sub_list = list(reader)
        iterate = len(sub_list)

        # 0th row is header, so start from row 1
        for i in range(1, iterate):
            # Print progress in %
            if (i % 100000 == 0):
                print(int(i / iterate * 100), "%")

            # Extract column for each submission entry
            # Each column defines an item and so far,
            # only mean for each item in total implemented as prediction
            length = len(sub_list[i][0])
            place_c = sub_list[i][0].find("c")
            column = int(sub_list[i][0][place_c + 1:length + 1])

            # Put 'id' and prediction value into one entry and append it to submission_array
            liste = [sub_list[i][0], a[column-1]]
            submission_array.append(liste)

    # Dump results to file
    with open("final_sub.csv", "w", newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['Id','Prediction'])
        for i in submission_array:
            writer.writerow(i)

    return 0

main()