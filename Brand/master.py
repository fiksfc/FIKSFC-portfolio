print("--- fiksfc master v4.1 ---")
print("slogan: strive to observe, build, test and secure.")
import subprocess, os
while True:
    print("\n--- FIKSFC MASTER ---")
    print("[1] Scanner")
    print("[2] Mini Assistant")
    print("[3] Flashing Machine")
    print("[4] Poster")
    print("[5] View Notes")
    print("[6] Exit")
    c=input("Choose 1-6: ").strip()
    if c=="1": subprocess.run(["python3","scanner.py"])
    elif c=="2": subprocess.run(["python3","mini_assistant.py"])
    elif c=="3": subprocess.run(["python3","flashing_machine.py"])
    elif c=="4": subprocess.run(["python3","poster.py"])
    elif c=="5": print(open("cyber_project/DAILY_LOG.txt").read()[-1000:] if os.path.exists("cyber_project/DAILY_LOG.txt") else "No notes")
    elif c=="6": print("Exiting - strive to observe, build, test and secure."); break
