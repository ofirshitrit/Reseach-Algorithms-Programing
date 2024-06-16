import pandas
import pandas as pd

codes_for_questions = pandas.read_csv("https://raw.githubusercontent.com/erelsgl-at-ariel/research-5784/main/06-python-databases/homework/codes_for_questions.csv")
codes_for_answers = pandas.read_csv("https://raw.githubusercontent.com/erelsgl-at-ariel/research-5784/main/06-python-databases/homework/codes_for_answers.csv")
list_of_answers = pandas.read_csv("https://raw.githubusercontent.com/erelsgl-at-ariel/research-5784/main/06-python-databases/homework/list_of_answers.csv")



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
   >>> support_in_one_party_elections('ב')
   54
   >>> support_in_one_party_elections('ט')
   33
   >>> support_in_one_party_elections('מפלגה אחרת')
   11
   >>> support_in_one_party_elections('פתק לבן | לא אצביע')
   53
   """
    # Extract the relevant part of the party string before the '-' character if it exists
    party = party.split('-')[0].strip()

    # Find the code corresponding to the given party in codes_for_answers
    party_code_row = codes_for_answers[codes_for_answers['Label'].str.contains(f"^{party}(?: -|$)", na=False)]
    if party_code_row.empty:
        return 0
    party_code = party_code_row.iloc[0]['Code']

    # Count the number of people who chose this party in Q2
    count = list_of_answers['Q2'].value_counts().get(party_code, 0)
    return count




def get_party_code_mapping(label):
    # Split by the first ' - ' to extract the party code
    # Handle cases where the label might contain additional information after the party code
    return label.split('-')[0].strip()



def support_in_multi_party_elections(party: str) -> int:
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
    >>> support_in_multi_party_elections('מפלגה אחרת')
    8
    """
    party = party.split('-')[0].strip()

    # Create the dynamic mapping from Q3 columns to party codes
    q3_columns = codes_for_questions[codes_for_questions['Variable'].str.startswith('Q3_')]
    q3_mapping = q3_columns.set_index('Variable')['Label'].to_dict()

    # Create the final mapping from party codes to Q3 columns
    party_to_q3_column = {get_party_code_mapping(label): column for column, label in q3_mapping.items()}

    # Check if party_code exists in the mapping
    if party not in party_to_q3_column:
        # Handle invalid party code gracefully
        # print(f"Invalid party code: {party}")
        return 0

    q3_column = party_to_q3_column[party]
    support_count = int(list_of_answers[q3_column].sum())
    return support_count




def parties_with_different_relative_order() -> tuple:
    """
    Checks if there is a pair of parties whose relative order is different in the two methods.

    Returns:
        tuple: A tuple of party names whose relative order differs, or None if no such pair exists.
    """
    # Get all party labels
    party_labels = codes_for_answers[codes_for_answers['Value'] == 'Q2']['Label'].unique()

    # Create a dictionary to store support counts for each party in both systems
    q2_support = {}
    for party in party_labels:
        if party == 'פתק לבן | לא אצביע':
            continue
        try:
            q2_support[party] = support_in_one_party_elections(party)
        except AttributeError:
            print(f"Issue with party: {party}")
    # print(f"q2_support: {q2_support}")


    q3_support = {}
    for party in party_labels:
        if party == 'פתק לבן | לא אצביע':
            continue
        try:
            q3_support[party] = support_in_multi_party_elections(party)
        except AttributeError:
            print(f"Issue with party: {party}")
    # print(f"q3_support: {q3_support}")

    # Sort parties based on the support counts
    q2_sorted = sorted(q2_support.items(), key=lambda x: x[1], reverse=True)
    q3_sorted = sorted(q3_support.items(), key=lambda x: x[1], reverse=True)

    # Extract sorted party names
    q2_order = [party for party, _ in q2_sorted]
    q3_order = [party for party, _ in q3_sorted]

    # Debug: print the sorted party orders
    # print("Q2 Order:", q2_order)
    # print("Q3 Order:", q3_order)

    # Find pairs with different relative orders
    for i, party_a in enumerate(q2_order):
        for j, party_b in enumerate(q2_order):
            if i < j:  # Ensure we only consider pairs (A, B) where A is before B in Q2
                if q2_support[party_a] > q2_support[party_b] and q3_support[party_a] < q3_support[party_b]:
                    return (party_a, party_b)

    return None





if __name__ == '__main__':
    # party = input()
    # if party == "parties_with_different_relative_order":
    #     print(parties_with_different_relative_order())
    # else:
    #     print(support_in_one_party_elections(party), support_in_multi_party_elections(party))

    # Testing the function
    result = parties_with_different_relative_order()
    print(result)