# for i in range(0, 15, 1):
#     print(i)

# print("********************")
# for i in range(15, 0, -1):
#     print(i)

# n = 5 
# stars = ""
# for i in range(n):
#     stars = stars + "*"
# print(stars)

# n = 5
# m = 2
# stars = ""
# for i in range(n):
#     stars = stars + "*"
# for i in range(m):
#     print(stars)

# n = 5
# stars = ""
# for i in range(n):
#     for nb_spaces in range(n-i-1): 
#         stars += " "
#     for nb_stars in range(2*i-1):
#         stars += "*"
#     stars += "\n"

# print(stars)

# temp = 16
# if temp > 20:
#     if temp > 30:
#         print("J'ai trop chaud !")
#     else:
#         print("je suis bien")
# else:
#     print("j'ai froid")

# if temp > 30:
#     print("trop chaud")
# else:
#     if temp > 20:
#         print("je suis bien")
#     elif temp > 15:
#         print("ca pique")
#     else:  
#         print("j'ai froid")

# for i in range(100):
#     if i % 2 == 0:
#         print(str(i) + "est pair")
#     else:
#         print(str(i) +"est impair")

for i in range(10):
    print("table de multiplication" + str( i ))
    for j in range(10):
        print(str(i) + " x " + str(j) + " = " + str( i * j))