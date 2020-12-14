# json parsor
import csv
import json

file_path = input("path to your csv file(add the name of your csv file as well):")  # takes file path
base_new = "\\".join(file_path.split("\\")[:-1])


file_name = input(
    "name of th file that you want to save as after conversion(no extension required):")  # takes name of file you want to save as
file_name = base_new + "\\" + file_name + ".json"  # adds extension to file name
with open(file_path, "r") as qna:  # opens g n fileive
    with open(file_name, "w") as qnajson:  # makes new file as you entered
        final_json = []
        reader = csv.reader(qna)
        headings = next(reader)  # reads header of csv file
        for line in reader:
            x = {}
            for i in range(len(headings)):
                x[headings[i]] = line[i]
            ready_json = json.dumps(x)
            final_json.append(ready_json)

        new_json = ",".join([str(elem) for elem in final_json])
        last_json = "[" + new_json + "]"
        qnajson.write(last_json)
        print("your json file has been created at " + base_new)
