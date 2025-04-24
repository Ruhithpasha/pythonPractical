def tower_of_hanoi(n, source, auxiliary, destination):
    """
    Solve the Tower of Hanoi problem and print the steps.

    Args:
        n (int): Number of disks.
        source (str): The name of the source rod.
        auxiliary (str): The name of the auxiliary rod.
        destination (str): The name of the destination rod.
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)

# Example usage:
if __name__ == "__main__":
    num_disks = 3
    tower_of_hanoi(num_disks, 'A', 'B', 'C')