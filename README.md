# Predicting Autistic Traits in Toddlers
## Background
> 
## Goals
- Identify which toddlers display traits of autism
## Initial Hypotheses:
- Which questions in q chat have a greater correlation with being labeled as "autistic"
- Is having a family member with autism have a corrleation with autistic traits?
- Is there a significant difference between ethinicities and autistic traits?
- Is there a signigicant difference between age and autistic traits?
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

## Planning
[Follow along with me!](https://trello.com/b/kZhzTUYs/individual-project-board)

## Acquire and Prep Dataset
[Use this module to grab the data! ](https://github.com/segovialori/toddler_autism_predictor/blob/master/wrangle.py)