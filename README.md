![autism banner](https://mycanopy.org/wp-content/uploads/2020/01/Autism-Puzzle-Banner.jpg)
# Predicting Autistic Traits in Toddlers
## Background
> "Autism spectrum disorder (ASD) is a developmental disorder that affects communication and behavior. Although autism can be diagnosed at any age, it is said to be a “developmental disorder” because symptoms generally appear in the first two years of life." [National Institute of Mental Health](https://www.nimh.nih.gov/health/topics/autism-spectrum-disorders-asd/index.shtml)
## Goals
- Identify which toddlers display traits of autism
## Initial Hypotheses:
> Hypothesis 1:
    - Ho: Having a family member with autism does not effect autistic traits
    - Ha: Having a family member with autism does effect autistic traits
    - Outcome: We fail to reject the null hypothesis.
> Hypotheis 2:
    - Ho: Having a jaundice as a baby does not effect autistic traits
    - Ha: Having a jaundice as a baby not effect autistic traits
    - Outcome: We reject the null hypothesis.
## Key Takeaways:
-
## Data Dictionary

| column_name                 | description                                                                                                         | dtype    |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------|----------|
| `A1`                  | Does your child look at you when you call his/her name?                                                                                |  int64    |
| `A2`                 | How easy is it for you to get eye contact with your child?                                                           |              float64  |
| `A3`                  | Does your child point to indicate that s/he wants something? (e.g. a toy that is out of reach)  |  int64  |                                                                                
| `A4`          | Does your child point to share interest with you? (e.g. pointing at an interesting sight)                                |  int64    |   
| `A5`                      | Does your child pretend? (e.g. care for dolls, talk on a toy phone)                                                                    |                 float64  |
| `A6`                      | Does your child follow where you’re looking?  |                 int64    |
| `A7`                  | If you or someone else in the family is visibly upset, does your child show signs of wanting to comfort them? (e.g. stroking hair, hugging them)                                                             |                 float64  |
| `A8`                 | Would you describe your child’s first words as:                                                             |                 float64  |
| `A9`                  | Does your child use simple gestures? (e.g. wave goodbye)                                                                                       |                 float64  |
| `A10`    | Does your child stare at nothing with no apparent purpose?                                |                 float64  |
| `Age_Mons `              | Age of toddler in months                                                                      |                 float64  |
| `Qchat-10-Score`                  | Qchat score recieved in app                                                                           |                 int64    |
| `Sex`                   | The gender of the toddler                                                                    |                 object    |
| `Ethnicity`                   | Ethnicity of the toddler                                  |                 | object    |
| `Jaundice`                 | Whether the child was born with jaundice                                                                          |                 object    |
| `Family_mem_with_ASD`           | Family member with autism diagnosis                                                             |                 | object |
| `Class/ASD Traits`           | Toddler displays autistic traits or does not display autistic traits                                                             |                 object  |

## How to reproduce:
1. Clone or fork this repository
2. Download the following files into the directory you wish to work in: wrangle.py, explore.py, model.py and final_autism.ipynb
3. Run the final_autism jupyter notebook in its entirety
4. Modify features/models/etc how you see fit
5.  Follow the guide below to get started!
### Planning
[Follow along with me!](https://trello.com/b/kZhzTUYs/individual-project-board)

### Acquire and Prep Dataset
- [Use this module to grab the data! ](https://github.com/segovialori/toddler_autism_predictor/blob/master/wrangle.py)
- Or you can visit kaggle [here](https://www.kaggle.com/fabdelja/autism-screening-for-toddlers) to grab the data set and data dictionary 

### Explore
- Use the explore.py module to generate different types of visualizations

### Model
- Use the model.py module to make feature engineering a little easier