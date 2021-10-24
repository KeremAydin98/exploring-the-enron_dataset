
import joblib
import numpy as np

enron_data = joblib.load(open("../final_project/final_project_dataset.pkl", "rb"))

print("people: ",len(enron_data)) #how many people work on this?
print("features: ",len(enron_data["SKILLING JEFFREY K"])) #how many features are associated per person?

#The number of POIs
counter=0
for person in enron_data:
    if (enron_data[person]["poi"]==True):
        counter+=1
    else:
        pass
print("how many pois are there? :",counter)

#How many people are there in poi_names file
file=open("../final_project/poi_names.txt","r")
line_count = 0
for line in file:
    if line[0] == "(":
        line_count += 1
file.close()

print("number of poi_names: ",line_count)

print("All features: ",enron_data["PRENTICE JAMES"])

print("Prentice's stock belongings: ",enron_data["PRENTICE JAMES"]["total_stock_value"])

print("Number of messages by Wesley Colwell: ",enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

print("What’s the value of stock options exercised by Jeffrey K Skilling?",enron_data["SKILLING JEFFREY K"]["exercised_stock_options"] )

#Which of these three people have earned the most money and how much did they earn
Skilling=enron_data["SKILLING JEFFREY K"]['total_payments']
Lay=enron_data["LAY KENNETH L"]['total_payments']
Fastow=enron_data["FASTOW ANDREW S"]['total_payments']
x=np.array([[Skilling],[Lay],[Fastow]])

y=np.amax(x)

if y==Skilling:
    print("Skiiling got the most money: ",y)
elif y==Lay:
    print("Lay got the most money: ",y)
else:
    print("Fastow got the most money: ",y)

#How many of the people have a quantified salary and a quantified email address"
quantified_salary = 0
quantified_email_address = 0
for person,value in enron_data.items():
    if value['salary'] != "NaN":
        quantified_salary += 1
    if value['email_address'] != "NaN":
        quantified_email_address += 1

print("Number of quantified salary: ",quantified_salary)
print("Number of quantified email address: ",quantified_email_address)



