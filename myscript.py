import os
os.system("git bisect start $badhash $goodhash")
if os.system("git bisect run python -m pytest") == 0:
    bad_commit = os.popen("git bisect bad").read().strip()
    print(f"First bad commit: {bad_commit}")
os.system("git bisect reset")