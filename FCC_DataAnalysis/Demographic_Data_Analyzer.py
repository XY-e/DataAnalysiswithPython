import pandas as pd

def analyze_demographic_data():
    # Load the dataset
    df = pd.read_csv('census_data.csv')
    
    # Question 1: How many people of each race are represented in this dataset?
    race_counts = df['race'].value_counts()
    
    # Question 2: What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()
    
    # Question 3: What is the percentage of people who have a Bachelor's degree?
    total_people = df.shape[0]
    bachelors_percentage = (df['education'] == 'Bachelors').sum() / total_people * 100
    
    # Question 4: What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    advanced_education_salary = df[advanced_education]['salary'] == '>50K'
    percentage_advanced_education_high_salary = advanced_education_salary.sum() / advanced_education.sum() * 100
    
    # Question 5: What percentage of people without advanced education make more than 50K?
    no_advanced_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    no_advanced_education_salary = df[no_advanced_education]['salary'] == '>50K'
    percentage_no_advanced_education_high_salary = no_advanced_education_salary.sum() / no_advanced_education.sum() * 100
    
    # Question 6: What is the minimum number of hours a person works per week?
    min_hours_per_week = df['hours-per-week'].min()
    
    # Question 7: What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_hours_salary = df[df['hours-per-week'] == min_hours_per_week]['salary'] == '>50K'
    percentage_min_hours_high_salary = min_hours_salary.sum() / (df['hours-per-week'] == min_hours_per_week).sum() * 100
    
    # Question 8: What country has the highest percentage of people that earn >50K and what is that percentage?
    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts(normalize=True) * 100
    highest_percentage_country = country_salary.idxmax()
    highest_percentage = country_salary.max()
    
    # Question 9: Identify the most popular occupation for those who earn >50K in India.
    india_high_salary = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    most_popular_occupation = india_high_salary['occupation'].mode()[0]
    
    # Print the results
    print("People of each race represented in this dataset:")
    print(race_counts)
    print("\nAverage age of men:", round(average_age_men, 1))
    print("Percentage of people with a Bachelor's degree:", round(bachelors_percentage, 1))
    print("Percentage of people with advanced education who make more than 50K:", round(percentage_advanced_education_high_salary, 1))
    print("Percentage of people without advanced education who make more than 50K:", round(percentage_no_advanced_education_high_salary, 1))
    print("Minimum number of hours a person works per week:", min_hours_per_week)
    print("Percentage of people who work the minimum number of hours per week and earn more than 50K:", round(percentage_min_hours_high_salary, 1))
    print("Country with the highest percentage of people earning >50K:", highest_percentage_country)
    print("Percentage of people in that country earning >50K:", round(highest_percentage, 1))
    print("Most popular occupation for those who earn >50K in India:", most_popular_occupation)

# Run the function
analyze_demographic_data()
