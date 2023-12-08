athlete_times = []

for i in range(5):
    time = float(input("Enter the time it takes for the athlete to run the 100-meter race (in seconds): "))
    athlete_times.append(time)

average_time = sum(athlete_times) / len(athlete_times)


print("The average time for the athlete to run the 100-meter race is:", average_time, "seconds")


