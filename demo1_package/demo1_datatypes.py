print("helloWorld")
print("Hi", "Hello")

a=10
b=10.5
c=a+b
print(c)
print(type(c))
print(a,b,c)


my_name=("Himanshu")
print(my_name)
print(my_name[0])

print(my_name.upper())
print(my_name.lower())

colors=["Red", "Yellow", "Green"]
print(len(colors))
print(type(colors))
print(colors[0])

colors.append("blue")
print(colors)

colors.insert(0,"pink")
print(colors)

colors.remove("Yellow")
print(colors)


# Tuple - for fixed set of collections/ immutable ( cant add or remove items after creation)
signal=("Red", "Yellow", "Green")
print(signal[1])
print(type(signal))
print(len(signal))

# Boolean
flag=True
print(flag)
print(type(flag))


# Dictionary - Key -Value
employee_record={
    "id":101,
    "name":"Himanshu",
    "role":"Manager",
    "mobile":[12345,123456]
}

print(type(employee_record))
print(employee_record["id"])
print(employee_record["mobile"][1])
