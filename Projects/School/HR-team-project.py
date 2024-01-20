with open("C:/Users/alext/Documents/Programs/Projects/School/Files/hr_system.txt") as file:
    
    for pieces in file:
        parts = pieces.strip().split()

        name = parts[0]
        title = parts[2]
        salary = float(parts[3])
        id = parts[1]

        paycheck = salary / 24

        if title == 'Engineer':
            paycheck += 1000
        
        print(f"{name} (ID: {id}), {title} - ${paycheck:.2f}")
