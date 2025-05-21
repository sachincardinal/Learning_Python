#Task 2: Sum of Integers from 1 to 50 Using a Loop


# Initialize the sum variable
total_sum = 0

# Step 1 & 2: Use a for loop to iterate from 1 to 50 and calculate the sum
for number in range(1, 51):  # range is exclusive of the end, so use 51
    total_sum += number

# Step 3: Display the final sum
print(f"The sum of integers from 1 to 50 is: {total_sum}")