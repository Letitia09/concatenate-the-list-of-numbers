def create_largest_number(number_list):
    number_list.sort(reverse=True)
    b=''
    for i in range(len(number_list)):
        a=str(number_list[i])
        b=b+a
    return int(b)
        
    #remove pass and write your logic here

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
