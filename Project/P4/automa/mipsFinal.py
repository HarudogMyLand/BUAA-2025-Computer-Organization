from mipsCheck import run_once
import sys

try:
    times = -1

    while times <= 0 or times > 50:
        print("Test start with index 1")
        times = int(input("How many times do you want to run? (input a positive num less than 50): ").strip())

    cnt = 0

    num1 = 10
    num2 = 10
    jump = True

    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        num1 = int(sys.argv[1])
    if len(sys.argv) > 2 and sys.argv[2].isdigit():
        num2 = int(sys.argv[2])
    if len(sys.argv) > 3:
        if sys.argv[3] == "-T" or sys.argv[3] == "-t":
            jump = True
        elif sys.argv[3] == "-F" or sys.argv[3] == "-f":
            jump = False


    while times > 0:
        print(f"No. {cnt} test started".center(20, "="))
        if run_once(num1, num2, jump):
            times -= 1
            cnt += 1
        else:
            print(f"{times} test failed.")
            break
        print(f"End".center(20, "="))

except KeyboardInterrupt:
    print("You have terminated the program")
except Exception as e:
    print(e)