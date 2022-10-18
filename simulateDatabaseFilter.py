import shutil

#This script only simulates de process of manually filtering the data in database_intermidiate_csv.
#All it does is create a copy with the name "database_complete.csv"

shutil.copyfile("dataset_intermidiate.csv","dataset_complete.csv")