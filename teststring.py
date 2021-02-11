import sys

txt="hellothis is kalesha"
txt1="How are you!"

##length of the string
print(len(txt))

##looping the string and printing the every word
for x in txt:
 print(x)

##checking if the word is present in given string
print("kalesha" in txt)
if "this" in txt:
 print("this is in given string")
else:
 print("this not in given string")


###If not in 
if "kaleshapasha" not in txt:
 print("kaleshapasha is no in given txt")
else:
 print("kaleshapasha is in given txt")
 
####################Slicing a String############
print(txt[3:7]) ## It will disply the string from index 3 to index 6

#########slice from the startswith
print(txt[:6])  #######it output from starting the string index[0] to index[5]


##############slic to the endswith
print(txt[2:])   #it output from start index[2] to end of the string

print(txt1[-8:-1])

##########modify the string
print(txt.upper())
print(txt.lower())
##remove whitespaces whth the method strip
txt2="   pasha   "
print(txt2.strip())

###replace string
print(txt.replace("h","J"))

########split the string
txt3="hello this is Arshia"
print(txt3.split(" "))

##############format the string
txt4="Hello my name is {} and I am {} years old. I got {} marks in all subjects"
age=40
marks=540
st="kalesha"
print(txt4.format(st,age,marks))

print(txt.count("a"))



