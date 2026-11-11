rate = float(input("Enter the per KM rate: "))
distance = float(input("Enter the total distance: "))
fare = rate * distance

split_fare = input("Do you want to split the fare? (yes/no): ").strip().lower()

if split_fare == "yes":
    num_people = int(input("Enter the number of people to split the fare with (maximum 4): "))
    
    if num_people > 4:
        print("Maximum number of people allowed is 4.")
    elif num_people < 2:
        print("The number of people must be at least 2.")
    else:
        remaining_distance = distance
        
        # Loop through all people except the last one
        for i in range(1, num_people):
            p_dist = float(input(f"Enter the distance traveled by person {i}: "))
            p_fare = rate * p_dist
            remaining_distance -= p_dist
            print(f"Person {i}'s distance is {p_dist:.2f} and share is: {p_fare:.2f}")

        # The last person takes the remaining distance
        p_last_fare = rate * remaining_distance
        print(f"Person {num_people}'s distance is {remaining_distance:.2f} and share is: {p_last_fare:.2f}")
else:
    print(f"The total fare is: {fare:.2f}")