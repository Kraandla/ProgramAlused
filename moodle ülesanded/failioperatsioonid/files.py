import csv
# with open("numbers.txt") as f:  # f = open("numbers.txt")
#     n = 5
#     content = f.readline().strip()
#     print(content)
#     f.close()

# with open("test.txt", "w", encoding="UTF-8") as file:  # f = open("numbers.txt")
#     data = [["name", "age"], ["john", "11"], ["mary", "15"]]
#     for x in data:
#         name = x[0]
#         age = x[1]
#         line = name + "," + age
#         file.writelines(f"{line}\n")

# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     with open('new_names.csv', 'w') as new_file:
#         fieldnames = ['first_name', 'last_name', 'email']
#         csv_writer = csv.writer(new_file, delimiter='\t')
#
#         for line in csv_reader:
#             csv_writer.writerow(line)

if __name__ == "__main__":
    with open("names.csv", 'r') as csv_file:
        sniffer = csv.Sniffer().sniff(csv_file.read(1024))
        print(sniffer)
        csv_file.seek(0)

        r = csv.reader(csv_file, sniffer)
        print(r)
        for row in r:
            print(row)
