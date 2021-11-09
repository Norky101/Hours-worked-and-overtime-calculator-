#new code below
sh = input("Enter Hours: ")
sr = input ("Enter Rate: ")
fh = float(sh)
fr = float (sr)
if fh > 40 :
    reg = fr * fh
    overtime = (fh - 40.0) * (fr * 0.5)
    xp = reg + overtime
else:
    xp = fh * fr
print("Pay:",xp)
