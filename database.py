import pandas as pd # type: ignore


my_data={
    "name":["John","Doe","Jane"],
    "class":["1","2","3"],
    "roll_no":["1","2","3"],
    "weight":["50","60","70"],
}
my_index=["row1","row2","row3"]
of= pd.DataFrame(my_data,index=my_index)
of.to_csv("data.csv")
new_of= pd.read_csv("data.csv")
print(new_of)

