print("Hi, and welcome to the Grade Generator! Please input the necessary datas to get your score calculated.")
score = int(input("What score did you get? "))
percentage = round(float(score / 50 )* 100, 2)
if score < 50:
	print(f"""Your score is \033[1;33m{percentage}\033[1;0m%, and you got an \033[0;31mU\033[0m for that. Sorry, I think this field is just not for you :(""")
elif score >= 50 and score < 60:
	print(f"Your score is \033[1;33m{percentage}\033[1;0m%, and you got a \033[1;30mD\033[0m for that. Please study harder, I know you got this.")
elif score >= 60 and score < 70:
	print(f"Your score is \033[1;33m{percentage}\033[1;0m%, and you got a \033[1;35mC!\033[0m Not too shabby. Let's see what your Asian parents think about it.")
elif score >= 70 and score < 80:
	print(f"\033[1;34mB\033[0m is really not a bad score, with the percentage of \033[1;33m{percentage}\033[1;0m. You're just almost there!")
elif score >= 80 and score < 90:
	print(f"Woo! Your grade is \033[0;32mA\033[0m. You got a pretty good score out there, pal! \033[1;33m{percentage}\033[1;0m% is very impressive! I hope your parents are proud and not comparing you to that nerd next door. 🤓")
elif score >= 90 and score <= 100:
	print(f"Astounding! \033[1;32mA++\033[0m for a change! Your friends are going to envy you, and your existence is in danger if you're from some extreme states of the world. Worry not! You're already this smart with {percentage}% to finish this code so you'd have to know how to hide yourself from CIA agents. 👮‍♂️👮‍♂️")
