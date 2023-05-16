# open files
file_1 = open("files/reservoir_coordinates.csv", "r")
file_2 = open("files/all_data_1.csv", "r")
file_3 = open("files/output.csv", "w")

# get file data
resv = file_1.read().split("\n")
data = file_2.read().split("\n")

# output array
output = ["Reservoir,Longitude,Latitude,Elevation"]

# for each reservoir line
for i in range(1, len(resv) - 1):
    # split reservoir line
    resv_data = resv[i].split(",")
    # reservoir data
    resv_name = resv_data[0]
    resv_ln_1 = float(resv_data[1]) # longitude 1
    resv_lt_1 = float(resv_data[2]) # latitude 1
    resv_ln_2 = float(resv_data[3]) # longitude 2
    resv_lt_2 = float(resv_data[4]) # latitude 2
    # state log
    print("Running... " + resv_name + " [" + str(i) + "/" + str(len(resv) - 2) + "]")
    # match count
    match = 0
    # for each data line
    for j in range(1, len(data) - 1):
        # split data line
        data_data = data[j].split(",")
        # result data
        data_ln = float(data_data[0]) # data longitude
        data_lt = float(data_data[1]) # data latitude
        data_el = float(data_data[2]) # data elevation
        # match longitude with reservoir data
        check_1 = data_ln < resv_ln_1 and data_ln > resv_ln_2
        check_2 = data_ln > resv_ln_1 and data_ln < resv_ln_2
        # match latitude with reservoir data
        check_3 = data_lt < resv_lt_1 and data_lt > resv_lt_2
        check_4 = data_lt > resv_lt_1 and data_lt < resv_lt_2
        # check match logics
        if((check_1 or check_2) and (check_3 or check_4) or True):
            # append to output
            output.append(resv_name + "," + str(data_ln) + "," + str(data_lt) + "," + str(data_el))
            # increase match count
            match += 1
    # print match count for reservoir
    print("Total Match:", match)

# completed log
print("Writing... files/output.csv")

# output string
output_text = ""

# for each output
for line in output:
    # add to string
    output_text += line + "\n"

file_3.write(output_text)


# close files
file_1.close()
file_2.close()
file_3.close()

# completed log
print("Completed!")
