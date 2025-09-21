import pandas as pd

# Original data
data = {
    "customer_id": [1,2,3,4,5,6,7,8,9,10],
    "firstname": ["Dhanush","John","Smith","David","Sam","Rocky","Tony","Stark","Bruce","Wayne"],
    "lastname": ["M D","Wick","Wayne","Banner","Stark","Wayne","Rogers","Stark","Wayne","Banner"],
    "age": [24,30,35,40,28,33,29,31,38,45],
    "city": ["Sakleshpura","New York","Gotham","New York","Gotham","New York","Los Angeles","New York","Gotham","New York"],
    "signup_date": ["2022-01-01","2021-05-15","2020-07-20","2019-11-30","2021-03-25","2020-12-10","2022-02-14","2018-09-05","2019-06-18","2021-08-22"]
}
data1 = pd.DataFrame(data)

data1 = data1.drop_duplicates(inplace=False)
print("Original data without exact duplicates:\n")
print(data1)
data1['firstname'] = data1['firstname'].str.title().str.strip()
data1['lastname'] = data1['lastname'].fillna('Unknown').str.title().str.strip()
data1 = data1.drop_duplicates(subset=['firstname','lastname'], keep="first", inplace=False, ignore_index=True)
print("\nAfter removing duplicates based on FirstName and LastName:\n")
print(data1)
data1['FirstName'] = data1['firstname']
data1['LastName'] = data1['lastname']
data1['signup_date'] = pd.to_datetime(data1['signup_date'], errors='coerce', dayfirst=True)
data1['SignUpdate'] = data1['signup_date'].dt.strftime('%Y-%m-%d')
print("\nAfter standardizing date format:\n")
print(data1)
