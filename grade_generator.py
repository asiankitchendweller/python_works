print("Hi, and welcome to the Grade Generator! Please input the necessary datas to get your score calculated.")
score = int(input("What score did you get? "))
percentage = score // 100
if score < 50:
	print(f"""Your score is {percentage}%, and you got an U for that. Sorry, I think this field is just not for you :(""")
elif score > 50:
	print(f"Your score is {percentage}%, and you got a D for that. Please study harder, I know you got this.")
elif score >= 60:
	print(f"Your score is {percentage}%, and you got a C! Not too shabby. Let's see what your Asian parents think about it.")
elif score >= 70:
	print(f"B is really not a bad score, with the percentage of {percentage}. You're just almost there!")
elif score >= 80:
	print(f"Woo! YOu got a pretty good score out there, pal! {percentage}% is very impressive! I hope your parents are proud and not comparing you to that nerd next door.")
elif score >= 90 or score <= 100:
	print("A++")