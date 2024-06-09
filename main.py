import pandas

codes_for_questions = pandas.read_csv("https://raw.githubusercontent.com/erelsgl-at-ariel/research-5784/main/06-python-databases/homework/codes_for_questions.csv")
codes_for_answers = pandas.read_csv("https://raw.githubusercontent.com/erelsgl-at-ariel/research-5784/main/06-python-databases/homework/codes_for_answers.csv")
list_of_answers = pandas.read_csv("https://raw.githubusercontent.com/erelsgl-at-ariel/research-5784/main/06-python-databases/homework/list_of_answers.csv")


def support_in_one_party_elections(party:str)->int:
    # Find the code corresponding to the given party in codes_for_answers
    party_code_row = codes_for_answers[codes_for_answers['Label'].str.contains(party, na=False)]
    if party_code_row.empty:
        return 0  # Return 0 if the party is not found
    party_code = party_code_row.iloc[0]['Code']

    # Count the number of people who chose this party in Q2
    count = list_of_answers['Q2'].value_counts().get(party_code, 0)
    return count


def support_in_multi_party_elections(party:str)->int:
    pass
    # Put your code here


def parties_with_different_relative_order()->tuple:
    pass
    # Put your code here


if __name__ == '__main__':
    # # print(codes_for_questions)
    # print(list(codes_for_answers.columns))
    # print(list(codes_for_questions.columns))
    # print(list(list_of_answers.columns))
    #
    # print(list_of_answers)

    # print(list_of_answers['Q2'].to_dict())




    # party_code = 'כן - כחול לבן בראשות בני גנץ'
    party_code = 'מחל - הליכוד בהנהגת בנימין נתניהו לראשות הממשלה'
    support_count = support_in_one_party_elections(party_code)
    print(f"The number of people who support the party '{party_code}' is: {support_count}")

    # party = input()
    # if party == "parties_with_different_relative_order":
    #     print(parties_with_different_relative_order())
    # else:
    #     print(support_in_one_party_elections(party), support_in_multi_party_elections(party))