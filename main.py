import pandas

codes_for_questions = pandas.read_csv("https://raw.githubusercontent.com/erelsgl-at-ariel/research-5784/main/06-python-databases/homework/codes_for_questions.csv")
codes_for_answers = pandas.read_csv("https://raw.githubusercontent.com/erelsgl-at-ariel/research-5784/main/06-python-databases/homework/codes_for_answers.csv")
list_of_answers = pandas.read_csv("https://raw.githubusercontent.com/erelsgl-at-ariel/research-5784/main/06-python-databases/homework/list_of_answers.csv")


# codes_for_answers:
def support_in_one_party_elections(party:str)->int:
    """
   Returns the number of people who support the given party in the current election system (Q2).

   >>> support_in_one_party_elections('מחל')
   134
   >>> support_in_one_party_elections('פה')
   109
   >>> support_in_one_party_elections('ר')
   3
   >>> support_in_one_party_elections('עם')
   21
   """
    # Find the code corresponding to the given party in codes_for_answers
    party_code_row = codes_for_answers[codes_for_answers['Label'].str.contains(party, na=False)]
    if party_code_row.empty:
        return 0
    party_code = party_code_row.iloc[0]['Code']

    # Count the number of people who chose this party in Q2
    count = list_of_answers['Q2'].value_counts().get(party_code, 0)
    return count


# Create the dynamic mapping from Q3 columns to party codes
q3_columns = codes_for_questions[codes_for_questions['Variable'].str.startswith('Q3_')]
q3_mapping = q3_columns.set_index('Variable')['Label'].to_dict()

def get_party_code_mapping(label):
    # Extract the party code from the label
    # Assuming the party code is the part of the label before the first space
    return label.split(' - ')[0]

# Create the final mapping from party codes to Q3 columns
party_to_q3_column = {get_party_code_mapping(label): column for column, label in q3_mapping.items()}

def support_in_multi_party_elections(party_code: str) -> int:
    """
    Returns the number of people who support the given party in the alternative election system.

       >>> support_in_multi_party_elections('מחל')
       162
       >>> support_in_multi_party_elections('פה')
       131
       >>> support_in_multi_party_elections('ר')
       13
       >>> support_in_multi_party_elections('עם')
       27
    """
    if party_code not in party_to_q3_column:
        raise ValueError("Invalid party code")

    q3_column = party_to_q3_column[party_code]
    support_count = int(list_of_answers[q3_column].sum())
    return support_count




def parties_with_different_relative_order()->tuple:
    """
     Checks if there is a pair of parties whose relative order is different in the two methods.
     Returns the pair of party codes if found, otherwise returns None.

     >>> parties_with_different_relative_order()
     ('B', 'A')
     """
     # Create the dynamic mapping from Q3 columns to party codes
    q3_columns = codes_for_questions[codes_for_questions['Variable'].str.startswith('Q3_')]
    q3_mapping = q3_columns.set_index('Variable')['Label'].to_dict()


if __name__ == '__main__':
    print(list(codes_for_answers.columns))
    print(list(codes_for_questions.columns))
    print(list(list_of_answers.columns))
    # print(list_of_answers)


    # 33
    # party_code = 'כן'

    # 134
    # party_code = 'מחל'

    # 34
    # party_code = 'אמת'
    # support_count = support_in_one_party_elections(party_code)
    # print(f"The number of people who support the party '{party_code}' is: {support_count}")

    # party_code = 'כן'
    # party_code = 'מחל'
    # party_code = 'ב'
    # party_code = 'שס'
    # support_count = support_in_multi_party_elections(party_code)
    # print(f"The number of people who support the party '{party_code}' is: {support_count}")

    # party = input()
    # if party == "parties_with_different_relative_order":
    #     print(parties_with_different_relative_order())
    # else:
    #     print(support_in_one_party_elections(party), support_in_multi_party_elections(party))