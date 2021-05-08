import sqlite3


def my_update_to_database(user_name):


    conn = sqlite3.connect('/Users/admin/Dev/trydjango/src/db.sqlite3')

    mycursor = conn.cursor()

    mycursor.execute("SELECT * FROM Parking_Slots")

    myresult = mycursor.fetchall()

    print(myresult)

    # print(myresult[0][0])

    name = user_name

    processed_array = sorted(sorted(myresult, key=lambda x: x[0]), key=lambda x: x[2], reverse=False)
    print(processed_array)

    temp = processed_array

    min = processed_array[0][2]


    for i in range(0, 7):

        if temp[i][1] == 0:

            min = temp[i][2]
            value = temp[i][0]
            break

        else:
            continue


    print("The nearest parking is: {}m away {}".format(min / 100, value))

    query = 'UPDATE Users SET Parking_Allotted = "{}" where Name = "{}" '.format(value, name)
    query_two = 'update Parking_Slots set Available = 1 where Parking_Slot = "{}"'.format(value)

    mycursor.execute(query)
    mycursor.execute(query_two)

    conn.commit()

    mycursor.execute("SELECT * FROM Parking_Slots")
    mycursor.execute('select * from users')

    my_new_result = mycursor.fetchall()

    print(my_new_result)

    print(myresult[0][1])
    
    for x in myresult:
        print(x)
        
    return value
