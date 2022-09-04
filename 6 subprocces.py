import subprocess as sp

p1 = sp.run(["dir"], capture_output=True, shell=True, text=True)
print(p1.stdout)

p2 = sp.Popen(["powershell.exe", "ls"])
p2.communicate()