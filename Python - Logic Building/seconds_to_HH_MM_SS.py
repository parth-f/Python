# WAP to convert input number of seconds to HH:MM:SS.

sec = int(input("Enter a number in Seconds - "))

hrs, sec = divmod(sec,3600)

min, sec = divmod(sec,60)

print(hrs,"hours",min,"minutes",sec,"seconds")