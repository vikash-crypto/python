my_data={
    "name":["John","Doe","Jane"],
    "class":["1","2","3"],
    "roll_no":["1","2","3"],
    "weight":["50","60","70"],
}
def add(data):
    with open("data.txt", 'a') as file:
        file.write(data + '\n')
    print(f"Data '{data}' added!")
def remove(data):
    try:
        with open("data.txt", 'r') as file:
            datas = file.readlines()
        datas = [t.strip() for t in datas]  
        if data in datas:
            datas.remove(data)
            with open("data.txt", 'w') as file: 
                for t in datas:
                    file.write(t + '\n')
            print(f"Data '{data}' removed!")
        else:
            print(f"Data '{data}' not found.")
    except FileNotFoundError:
        print("No data found.")
def view():
    try:
        with open("data.txt", 'r') as file:
            datas = file.readlines()
            if datas:
                print("\nYour Data:")
                for idx, data in enumerate(datas, 1):
                    print(f"{idx}. {data.strip()}")
            else:
                print("Your data is empty.")
    except FileNotFoundError:
        print("No data found.")
if __name__ == "__main__":
    while True:
        print("\nData Menu:")
        print("1. Add data")
        print("2. Remove data")
        print("3. View data")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            data = input("Enter data to add: ")
            add(data)
        elif choice == '2':
            data = input("Enter data to remove: ")
            remove(data)
        elif choice == '3':
            view()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")