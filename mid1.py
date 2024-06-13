# len1 = {12.23,23.23,12,23,'sanu','chinu'};
# print(type(len1));



# avenger  = ["hulk" ,"spider man ","black widow","new ","wanda","thor","panther"];
# avenger.insert(2,"bjnhsd");
# avenger.append("orange");
# print(avenger[2:5]); 
# print(avenger[-2:-1]); 
# print(avenger[-4:-1]); 
# print(avenger[1:]);  RETURN THE ITEM FROM THE ENTER NUMBER 
# print(avenger[:4]);
# print(avenger[3:2]);

# avenger.clear();
# print(avenger)




# to copty this we have to build a new method 
# av    =["panther","sumno","vision"]
# avcopy  = av.copy();
# print(avcopy);



# list method to cnvert a the iterable  daatatype to a list 
# convert a string object  to a string 
# str  = "purnendu";
# strlist   = list(str);
# print(strlist)



# sort method  = this sort the element of the list in asening order /desending 




# syntex  = list.sort() - aassending order  
# l1  = [12,42,3,23,23,23,23,23];
# l1.sort();
# print(l1);



# decending order 
# l1  = [12,42,3,23,23,23,23,23];
# l1.sort(reverse = True);
# print(l1);

# we can also find the max,min and len 
# l1  = [12,42,3,23,23,23,23,23];
# max(l1);
# print(l1)

# repetation of the 
# l1  = [12,42,3,23,23,23,23,23];
# l1*2;
# print(l1);



# replace the number 
# new = [12,23,34,34,45,45,45,354,4];
# new  = new[2:4] = [12,12]
# print(new)



# many to one 
# new = [12,23,34,34,45,45,45,354,4];
# new  = new[2:3] = [12];
# print(new);


# # new = [12,23,34,34,45,45,45,354,4];
# # for i in new:
# #     print(i);

# new = [12,23,34,34,45,45,45,354,4];
# sum  = 0;
# for i in new:
#         sum += i;
#         print("sum =",sum)


# # DAY2 
# new1  = [];
# new1.insert(1,"chinu");
# new1.extend(["chinu","prince of persia","pawn star",12,34,56,68]);
# new1.append("sanu");
# maximum  = max(new1);

# minimum  = min(new1);

# print(new1);




# emp =n=eval(input("Enter a list"))
# a=n
# b=n
# c=n
# x=[]
# a.reverse()
# print("reverse",a)
# b.sort(reverse=True)
# print("sorting",b)
# print("maximun",max(n))
# print("minimun",min(n))
# for i in c:
#     if i not in x:
#         x.append(i)
# print("After removing duplicate elementrs",str(x))






# emplist = []
# n = int(input("enter the number of element you want to pass "))
# for i in range(0,n):
#         emplist.append(int(input ("enter number")));
#         print(emplist);
#         emplist.reverse();
#         emplist.sort(reverse=True);
#         print(max(emplist));
#         print(min(emplist));
#         emplist;
#         un1st = []
#         dup1st = []
#         for i in emplist:
#                 if i not in un1st:
#                         un1st.append(i);
#                 elif i not in dup1st:
#                         dup1st.append(i);
#                         print(emplist)
#                         print(un1st);
#                         print(dup1st);
                        


# list1 = [1,2,3,4,5];
# list2  = [3,4,5,6,7,8];
# for i in range(6,10):
#         list1.append(i);
# for i in range(9,13):
#         list2.append(i);
# commonlist = [];
# for element in list1:
#         if element in list2:
#                 commonlist.append(element);              
# print(list1);
# print(list2);
# print(commonlist);

# list  = ["chinu","sanu","pradeep","purnendu"];
# if "chin" in list:
#         print("yes");   
        
        
# newlist  = ["chinu","this is newlist","newlist","list"];
# new  = ["this is old","old","olds"];
# newlist.extend(new); 
# print(newlist);
# newlist.remove("chinu");
# print(newlist) ;


# newlist  = ["chinu","this is newlist","newlist","list"];
# for i in range(len(newlist)):
#         print(newlist[i]);
        
        
# LIST COMPARISION
# fruit =["mango","banana","pinaapple","kiwi","fruits"];
# newlist = []
# for x in fruit:
#         if "a" in x :
#                 newlist.append(x);
#                 print(newlist);

# fruit =["mango","banana","pinaapple","kiwi","fruits"];
# newlist = [x for x in fruit if "a" in x];
# print(newlist);



# fruit =["mango","banana","pinaapple","kiwi","fruits"];
# newlist = ["chinu" for x in fruit ]
# print(newlist);



# fruit =["mango","banana","pinaapple","kiwi","fruits"];
# newlist  = [x if x != "banana" else "kiwi" for x in fruit];
# print(newlist);


# fruit =["mango","banana","pinaapple","kiwi","fruits"];
# fruit.sort();
# print(fruit);

# num = [12,3,34,34,3,87,7,8,9,3];
# num.sort();
# print(num);

# SORT NUMBER DESENDING
# thissort  = ["mango","kiwi","banana","pineaple","mono"];
# thissort.sort(reverse = True);
# print(thissort);


# CHECK HOW CLOSE THE NUMBERS FROM THE NUMBER
# def func(n):
#         return abs(n-5);

# this  = [1,2,3,4,5,6,7,8,9];
# this.sort(key=func);
# print(this);

# thissort  = ["NAMGO","kiwi","banana","pineaple","mono"];
# thissort.reverse();
# print(thissort);


# old  = [2,3,4,5,6,7,8];
# old1 = old.copy();
# print(old1);




# n = int(input("enter numebr to check the number "));
# print("even palindrome upto n",n);
# for i in range(0,n+1,2):
#     rev  =   int(str(i)[::-1]);
#     if rev == i:
#         print(i);
        
        
# print("enter the number");
# for i in range(2,20,5):
#        print(i);
       

# str  = str(input("enter any string")).split();

# for stri in str:
#     if stri==str[::-1]:
#         print("true");
#     else:
#         print("false");
                

# 1. WAP to sort the following list.
#   LISTT = [25, 47, -23, 0, -50, 24 8 1 9 10]

list = [25, 47, -23, 0, -50, 24, 8, 1, 9, 10];
list.sort();
print(list);

# 2. WAP to find the odd numbers and even numbers from entered list and display them in two list.
# n = eval(input("enter the number"));
# e = [];
# o = [];
# for i in range(0,len(n)):
#     if n[i]%2==0:
#         e.append(n[i]);
#     else:
#         o.append(n[i]);
        
#         print("even",e);
#         print("odd",o);
        
        
# n = eval(input("enter the name"));
# a = 0;
# b = 0;
# c = 0;
# for i in range(0,len(n)):
#     if n[i]>0:
#         a+=1;
        
#     if n[i]<0:
#         b+=1;
        
#     else:
#         c+=1;
#         print(a);
#         print(b);
#         print(c);


x = [5,10,7,4,50,3];
print(x);
y = set();
print(y);
    
    

