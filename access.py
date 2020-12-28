commands to demonstrate how to access and perform operations on a main file
#run the MODULE of MAIN FILE and import mainfile as a library 
import root as r 
#importing the main file("root" is the name of the file that I have used) as a library 
r.create("santa",25)
#creating a key with key_name,value given and with no time-to-live property
r.create("src",70,3600) 
#creating a key with key_name,value given and with time-to-live property value given(number of seconds)
r.read("santa")
#returning the value of the respective key in Jasonobject format 'key_name:value'
r.read("src")
#returning the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR
r.create("santa",50)
#returning an ERROR since the key_name already exists in the database
#To overcome this error either use modify operation to change the value of a key or use delete operation and recreate it
r.modify("santa",55)
#it replaces the initial value of the respective key with new value 
r.delete("santa")
#it deletes the respective key and its value from the database(memory is also freed)
#we can access these using multiple threads like
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout))
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t2.start()
t2.sleep()
#the code also returns other errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB
