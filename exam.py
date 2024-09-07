### 1 Question
# Дар бораи рекурсия нависед. 
#  recursia in yak navi funcsiya meboshad ki khudash khudashro faryod mekuned amale ki 
# mo bo for loop va while loop kor mekunem in niz kor kardA metavonad vale rafti kori on kamtar sust meboshad.
#  baroi in ki vay aval yak malumothoro dar xotirai favri sabt mekunad va badan to ijroi vazifa yaktoi mebinad 
# in ba monandi varaqi stack ki agar mo taskhoyamonro 
# ijro kunem va stackhoro boloi yakdigar monem va agar xohem onhoro binem yaktogi kanda az nazar meguzaronem. 

### 2 Question
# Closure(Замыкания) - ро бо мисолҳо фаҳмонед.
# bo yorii in mo metavonem yak elementi global budaro xosi yak joi digar kunem  bo yorii nonlocal





### 3 Question
# Контейнерҳоро ба хотир оварда онҳоро нависед. 
# List in yak navi kontinere meboshad ki  mo metavonem hamai namudi  datatyphoro dar on nigoh dorem  mo metavonem listro ivaz kunem tagirot vorid kunem va ilova kunem.
# tuple in conteynery ivaz nashavanda meboshad ki yak navi datayyphoro kabul mekunad.tuple nazar ba List teztar kor mekunad baroi on ki 
# set  in yak navi konteynere meboshad ki tartib nadorad duplicat kabul namekunad.
# dictionary  in yak navi conteynere meboshad ki dar daruni xudash key va value dorad  yane mo metavonem ki indexhoro xudamon nom monem.




### 4 Question
# Дар бораи list, dict comprehension ва args,kwargs нависед.

# list--> in yak navi kontinere meboshad ki  mo metavonem hamai namudi  datatyphoro dar on nigoh dorem  mo metavonem listro ivaz kunem tagirot vorid kunem va ilova kunem.

# dict comprehension--> in yak navi kutohkuni meboshad mo metavonem yak chand amalro yakjoya dar yak satr nishon medihad.
# args,kwargs--> inro mo dar daruni funksiya ba monandi dictionary istifoda burda metavonem.






### 5 Question
# Кадом методҳои модули datetime ва randome - ро медонед. Бо мисолҳо фаҳмонед.

# datime
# today- misol " n= datetime.today()" in vaqti imruzaro nishon medihad
# strftime("%Y-%m-%d")) in yak qolab baroi vaqtro muayan kardan  misol sol moh va ruzro bo - dar mobayni haryak nishon medihad
# %Y baroi sol
# %m baroi moh
# %d baroi ruz
# %A -baroi hafta

# Random
# randint--> raqam qabul mekunad
# choice-->yak tagiryobanda qabul mekunad
# sample--> du qimmat qabul mekunad 










# ### 1 Task
# Write a Python program that converts currency from one denomination to another.
# Создайте программу, которая конвертирует валюту одного номинала в другой.
# # input
#     Enter the amount in TJS: 1
# # output
#     Rub -> 8.33
#     USD -> 0.094
#     EUR -> 0.084
#     UZ_SUM -> 1000

# def currency(n):
#     print(f"Rub ->{n*8.33}")
#     print(f"USD ->{n*0.094}")
#     print(f"EUR ->{n*0.084}")
#     print(f"UZ_SUM->{n*1000}")






# ### 2 Task
# Write a Python program to convert a list of multiple integers into a single integer.
# Напишите программу на Python для преобразования списка из нескольких целых чисел в одно целое число.
# # input
#     Sample list: [11, 33, 50]
# # output
#     Expected Output: 113350

# def Lst(k):
#     n = "".join(map(str, k))
#     a = int(n)
#     return a
# lst1 = list(map(int, input().split()))
# res = Lst(lst1)
# print(res)




# ### 3 Task
# Create a closure that concatenates a given string with another string.
# Создайте замыкание, которое объединяет заданную строку с другой строкой.

# # input
#     Tajikistan
# # otput
#     Salom Tajikistan




# def salom(n):
#     def salom1(a):
#         return f"{n} {a}"
#     return salom1
# k = salom("Salom")
# f = "Tajikistan"
# print(k(f)) 




### 4 Task
# Write a recursive function to find the minimum element in a list.
# Напишите рекурсивную функцию для поиска минимального элемента в списке.

# # input
#     2 3 54 2 4 0 5 3 2 54
# # output
#     0




# def minn(my_list):
#     if len(my_list) == 1:
#         return my_list[0]
#     else:
#         minnn = minn(my_list[1:])
#         return my_list[0] if my_list[0] < minnn else minnn
# a = list(map(int, input().split()))
# print(minn(a))  






# ### 5 Task
# Given a natural number n, compute the sum 1^2+2^2+...+n^2.
# Create a function that takes single natural number n. You need to withdraw the calculated amount. Don’t forget to return the result. Solve this problem using the recursion function.

# Дано натуральное число n, вычислите сумму 1^2+2^2+...+n^2.
# Создайте функцию, которая принимает одно натуральное число n. Вам нужно вывести вычисленную сумму. Не забудьте вернуть результат. Решите эту задачу с помощью функции рекурсии.

# # input
#     n = 2
# # output
#     Expected Output: 5


# def paydarhami(n):
#     if n == 1:
#         return 1
#     else:
#         return n**2 + paydarhami(n-1)
# n = int(input())
# print(paydarhami(n)) 




### 6 Task
# Given a natural number N, find the sum of the numbers 1+1/1!+1/2!+1/3!+...+1/N!. The number of actions should be proportional to N.
# По данному натуральному числу N найдите сумму чисел 1+1/1!+1/2!+1/3!+...+1/N!. Количество действий должно быть пропорционально N.
# # input
#     1
# # output
#     2    



# def paydarhami(n):
#     cnt = 1
#     cnt1 = 1  
#     for i in range(1, n + 1):
#         cnt1 *= i  
#         cnt += 1 //cnt1  
#     return cnt
# n = int(input())
# res = paydarhami(n)
# print( res)







# ### 7 Task
# Write a Python program to replace each character of a word of length five and more with a hash character (#).
# Напишите программу на Python, заменяющую каждый символ слова длиной пять и более символом решетки (#).
# # input
#     Count the lowercase letters in the said list of words:
# # output
#     ##### the ######### ####### in the said list of ######
# (Dont use string method creat it and the client should input number with  itself)


# def reshotka(n):
#     my_list = []
#     r = ""
#     for i in n:
#         if i == " ":  
#             if len(r) >= 5: 
#                 my_list.append("#" * len(r)) 
#             else:
#                 my_list.append(r)  
#             my_list.append(" ")  
#             r = "" 
#         else:
#             r += i  
#     if len(r) >= 5:
#         my_list.append("#" * len(r))
#     else:
#         my_list.append(r)

#     return ''.join(my_list)
# a = input()
# k = reshotka(a)
# print(k)
    


### 8 Task
# Given a natural number N, find the sum of numbers 1+1/1!+1/2!+1/3!+...+1/N!. The number of actions must be proportional to N.
# Create a function that takes a single number N. It is necessary to display the result of the calculation as a real number with an accuracy of 5 decimal places. Don’t forget to return the result.

# Дано натуральное число N, найдите сумму чисел 1+1/1!+1/2!+1/3!+...+1/N!. Количество действий должно быть пропорционально N.
# Создайте функцию, которая принимает одно число N. Необходимо вывести результат вычисления в виде действительного числа с точностью до 5 знаков после запятой. Не забудьте вернуть результат.

# # input
#     N = 1
# # output
#     res = 2




# def paydarhami(n):
#     cnt = 1
#     cnt1 = 1  
#     for i in range(1, n + 1):
#         cnt1 *= i  
#         cnt += 1 /cnt1  
#     return cnt
# n = int(input())
# res = paydarhami(n)
# print(res)





# ### 10 Task
# Given a string containing only English letters (upper and lower case). Add opening and closing brackets as follows: "example" -> "e(x(a(m)p)l)e" (Opening brackets are added before the middle, closing brackets are added after the middle. If the string length is even, there should be 2 symbols in the brackets located in the middle. ("card -> c(ar)d", but not "c(a()r)d"). Solve this problem using the recursion function.

# Дана строка, содержащая только английские буквы (большие и маленькие). Добавить открывающиеся и закрывающиеся скобки по следующему образцу: "example" -> "e(x(a(m)p)l)e" (До середины добавлены открывающиеся скобки, после середины – закрывающиеся. В случае, когда длина строки четна в скобках, расположенных в середине, должно быть 2 символа. ("card -> c(ar)d", но не "c(a()r)d"). Решите эту задачу с помощью функции рекурсии.

# # input                           # input
#     hello                           khayriddin
# # output                          # output
#     h(e(l)l)o                       k(h(a(y(ri)d)d)i)n




# def Qavsak(d, cnt=0, cnt1=0):
#     if cnt1 == 0:  
#         cnt1 = len(d) - 1
#     if cnt > cnt1:
#         return ""
#     if cnt == cnt1:
#         return d[cnt]
#     if cnt + 1 == cnt1:
#         return d[cnt:cnt1+1]
#     return d[cnt] + "(" + Qavsak(d, cnt + 1, cnt1 - 1) + ")" + d[cnt1]
# d = input()
# print(Qavsak(d))
















































































    