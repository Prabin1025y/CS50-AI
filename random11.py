def hanoi(n,source, destination, temp):
    if n==1:
        print(f"Move disk 1 from rod {source} to rod {destination}")
        return
    hanoi(n-1, source, temp, destination)
    print(f"Move disk {n} from rod {temp} to rod {destination}")
    hanoi(n-1, temp, destination, source)
    
n= int(input("Enter the number of disks: "))
hanoi(n,1,3,2)
    