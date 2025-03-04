# Udemy Courses Dataset Analysis

## Project Overview

This project involves analyzing a dataset of Udemy courses using Python and Pandas. The goal is to explore the dataset, answer specific business questions, and uncover insights about the types of courses offered, pricing, subscriber counts, and more. The analysis provides valuable insights for potential course creators, marketers, or anyone interested in understanding trends within Udemy's offerings.

## Table of Contents

- [Project Overview](#project-overview)
- [Data Sources](#data-sources)
- [Project Structure](#project-structure)
- [Analysis](#analysis)
  - [Key Questions and Insights](#key-questions-and-insights)
- [Results and Recommendations](#results-and-recommendations)
- [Acknowledgments](#acknowledgments)

## Data Sources

The dataset used in this project is a **Udemy Courses Dataset**, which contains detailed information about various courses offered on Udemy. The dataset includes the following columns:

- **course_title**: Title of the course.
- **subject**: Subject category of the course (e.g., Web Development, Graphic Design).
- **is_paid**: Whether the course is paid or free.
- **num_subscribers**: Number of subscribers enrolled in the course.
- **price**: Price of the course.
- **published_timestamp**: Date when the course was published.
- **level**: Difficulty level of the course (e.g., Beginner, Intermediate, Advanced).

## Project Structure

The project is structured as follows:

```
Udemy-Courses-Analysis/
│
├── data/
│   └── file.csv                  
│
├── notebooks/
│   └── udemy_courses_analysis.ipynb 
│
├── README.md                     
```

## Analysis

### Key Questions and Insights

The project answers several key questions about the Udemy courses dataset, including:

Q. 1) What are all different subjects for which Udemy is offering courses ?
Q. 2) Which subject has the maximum number of courses.
Q. 3) Show all the courses which are Free of Cost.
Q. 4) Show all the courses which are Paid.
Q. 5) Which are Top Selling Courses ?
Q. 6) Which are Least Selling Courses ?
Q. 7) Show all courses of Graphic Design where the price is below 100 ?
Q. 8) List out all the courses that are related to 'Python'.
Q. 9) What are courses that were published in the year 2015 ?
Q. 10) What is the Max. Number of Subscribers for Each Level of courses ?

### Example Code to Extract Insights:

Here’s a sample of how the dataset is explored in the notebook:

```python
import pandas as pd

# Load the dataset
dat = pd.read_csv('path_to_your_file.csv')

# Show unique course subjects
print(dat.subject.unique())

# Count the number of courses per subject
print(dat.subject.value_counts())

# Filter and display free courses
free_courses = dat[dat.is_paid == False]
print(free_courses)

# Show top-selling courses by number of subscribers
top_selling_courses = dat.sort_values('num_subscribers', ascending=False)
print(top_selling_courses.head())

# Filter Python-related courses
python_courses = dat[dat.course_title.str.contains('Python')]
print(python_courses)
```

## Results and Recommendations

### Key Insights:

1. **Most Popular Subject**:
   - Web Development is the leading subject with the highest number of courses offered. This indicates a strong demand for web development skills.

2. **Free Courses**:
   - A significant portion of the Udemy courses are available for free, providing learners with accessible options for learning without financial commitment.

3. **Top-Selling Courses**:
   - Courses with the highest number of subscribers indicate high demand and relevance in specific topics. These courses can be used as benchmarks for course creation.

4. **Pricing Strategy for Graphic Design**:
   - Since there are no graphic design courses priced below $100, it could be an opportunity for course creators to explore affordable pricing models in this subject.

5. **Python Courses**:
   - There is a strong interest in Python courses. If you are a course creator, targeting the Python niche could be a lucrative opportunity.

### Recommendations:

- **Course Creation Strategy**: Focus on creating courses in high-demand subjects such as Web Development, or explore subtopics within Python to cater to growing demand.
- **Pricing Adjustments**: Consider introducing affordable pricing options for Graphic Design courses to attract more learners.
- **Marketing**: Courses with high subscriber counts can be leveraged for targeted marketing campaigns, emphasizing their popularity and success.


## Acknowledgments

- Thanks to Udemy which provided the data used in this analysis.
- Special thanks to the Python and Pandas communities for their continuous support in data science and analysis.
