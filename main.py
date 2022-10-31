def colorChange(color):
  if color == 'red':
    return ("\033[31m")
  elif color == 'white':
    return ("\033[0m")
  elif color == 'blue':
    return ("\033[34m")
  elif color == 'yellow':
    return ("\033[33m")
  elif color == 'green':
    return ("\033[32m")
  elif color == 'purple':
    return ("\033[35m")


title = f"{colorChange('red')}={colorChange('white')}={colorChange('blue')}={colorChange('yellow')} Music App {colorChange('red')}={colorChange('white')}={colorChange('blue')}="
print(f"           {title: ^35}")
print(f"🔥▶ \t{colorChange('white')}Radio Gaga")
print(f"    \t{colorChange('yellow')}Queen")
print()

prev = "PREV"
next ="NEXT"
pause ="PAUSE"

print(f"{colorChange('white')}{prev:<35}")
print(f"{colorChange('green')}{next:^35}")
print(f"{colorChange('purple')}{pause:>35}")

print(f"            \t{colorChange('white')}WELCOME TO")
print(f"           \t{colorChange('blue')}--    ARMBOOK    --")

text1 = "Definitely not a rip off of"
text2 = "a certain other social"
text3 = "networking site"
print(f"{colorChange('yellow')}{text1:>35}")
print(f"{colorChange('yellow')}{text2:>35}")
print(f"{colorChange('yellow')}{text3:>35}")
print()
text4 = "Honest"
text5 = "Username:"
text6 = "Password:"
print(f"{colorChange('red')}{text4:^35}")
print()
print(f"{colorChange('white')}{text5:^35}")
print(f"{colorChange('white')}{text6:^35}")