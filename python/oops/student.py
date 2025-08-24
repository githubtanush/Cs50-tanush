def main():
    # name = get_name()
    # house = get_house()
    # name,house = get_student()
    student = get_student()
    # print(f"{name} from {house}")
    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"
    # print(f"{student[0]} from {student[1]}")
    if(student["name"] == "Padma"):
            student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

# def get_name():
#     return input("Name: ")

# def get_house():    
#     return input("House: ")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     # return (name,house) #this is tupe and cannot change in tuple
#     return [name,house] #this is list is mutable;

#list - [] tuple - ()

#for dictionary we using - {};
def get_student():
    # student = {}
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    # return student
    name = input("Name : ")
    house = input("House : ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()

#tuple is immutable - means unchangable 
#on the other hand list is mutable - means changable
#The datatype which allows the values to not to change
# is what we used like tuple 
#Dictionary is also mutable 
#means other than tuples all are mutable 