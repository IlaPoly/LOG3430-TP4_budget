import os
os.system("git bisect start $badhash $goodhash")
os.system("git bisect run python -m pytest")
if result == 0:
        # Récupérer le premier commit identifié comme mauvais
        bad_commit = subprocess.check_output("git bisect bad", shell=True).decode().strip()
        print(f"First bad commit: {bad_commit}")
os.system("git bisect reset")