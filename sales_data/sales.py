# category = "Sports"
# with open("sales_data.txt", "r") as sports:
#     lines = sports.readlines()

# for line in lines:
#     # Split the line on whitespace
#     data = line.split()
#     number = data[0]
#     value = data[1]

#     # Put this through to SQL using an INSERT statement...
#     cursor.execute("""INSERT INTO tablename (person_id, category, type)
#                    VALUES(%s, %s, %s)""", (number, category, value))

# file = open("sales_data.txt")

# data = file.read()

# # print data

# for i in data:
#     set = 0
#     if "$" in i:
#         set += 1
#     print set

# file.close()


with open('sales_data.txt') as f:
    raw_data = f.readlines()

    raw_data[:9]
