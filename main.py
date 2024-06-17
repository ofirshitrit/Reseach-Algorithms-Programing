import sqlite3, requests

with open("poll.db", "wb") as file:
    response = requests.get("https://github.com/erelsgl-at-ariel/research-5784/raw/main/06-python-databases/homework/poll.db")
    file.write(response.content)
db = sqlite3.connect("poll.db")

def print_codes_for_answers_range(start: int, end: int):
    query = f"SELECT * FROM codes_for_answers LIMIT {end - start + 1} OFFSET {start - 1}"
    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    # Print column names
    column_names = [description[0] for description in cursor.description]
    print("\t".join(column_names))

    # Print rows
    for row in rows:
        print("\t".join(str(cell) for cell in row))


def print_list_of_answers():
    query = "SELECT * FROM list_of_answers"
    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    # Print column names
    column_names = [description[0] for description in cursor.description]
    print("\t".join(column_names))

    # Print rows
    for row in rows:
        print("\t".join(str(cell) for cell in row))


def print_codes_for_questions():
    query = "SELECT * FROM codes_for_questions"
    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    # Print column names
    column_names = [description[0] for description in cursor.description]
    print("\t".join(column_names))

    # Print rows
    for row in rows:
        print("\t".join(str(cell) for cell in row))



def net_support_for_candidate1(candidate1:str, candidate2:str)->int:
    """
     Returns the net support for candidate1 over candidate2.

     Net support is defined as the number of people who prefer candidate1 over candidate2
     minus the number of people who prefer candidate2 over candidate1.

     :param candidate1: Name of the first candidate
     :param candidate2: Name of the second candidate
     :return: Net support for candidate1 over candidate2


     >>> candidate1, candidate2 = "בני גנץ", "יאיר לפיד"
     >>> net_support_for_candidate1(candidate1,candidate2)
     47

     >>> candidate1, candidate2 = "בנימין נתניהו", "יולי אדלשטיין"
     >>> net_support_for_candidate1(candidate1,candidate2)
     11

     >>> candidate1, candidate2 = "ניר ברקת", "נפתלי בנט"
     >>> net_support_for_candidate1(candidate1,candidate2)
     -45
     """
    cursor = db.cursor()

    # Get variable names for candidates from codes_for_questions
    cursor.execute("SELECT Variable FROM codes_for_questions WHERE label=?", (candidate1,))
    variable1 = cursor.fetchone()[0]
    cursor.execute("SELECT Variable FROM codes_for_questions WHERE label=?", (candidate2,))
    variable2 = cursor.fetchone()[0]

    # Count preferences
    cursor.execute(f"""
        SELECT 
            SUM(CASE WHEN {variable1} > {variable2} THEN 1 ELSE 0 END) AS prefer_candidate1,
            SUM(CASE WHEN {variable2} > {variable1} THEN 1 ELSE 0 END) AS prefer_candidate2
        FROM list_of_answers
    """)
    result = cursor.fetchone()

    prefer_candidate1 = result[0] if result[0] is not None else 0
    prefer_candidate2 = result[1] if result[1] is not None else 0

    return prefer_candidate2 - prefer_candidate1

def condorcet_winner() -> str:
    """
    Check if there is a Condorcet winner among the candidates.
    Returns the name of the Condorcet winner if one exists, otherwise "none".
    """
    cursor = db.cursor()

    # Get all candidate variable names and labels from codes_for_questions
    cursor.execute("SELECT variable, label FROM codes_for_questions WHERE variable LIKE 'Q6_%'")
    candidates = cursor.fetchall()

    for candidate1_var, candidate1_name in candidates:
        is_condorcet_winner = True

        for candidate2_var, candidate2_name in candidates:
            if candidate1_var == candidate2_var:
                continue

            # Get the net support for candidate1 over candidate2
            cursor.execute(f"""
                SELECT 
                    SUM(CASE WHEN {candidate1_var} > {candidate2_var} THEN 1 ELSE 0 END) AS prefer_candidate1,
                    SUM(CASE WHEN {candidate2_var} > {candidate1_var} THEN 1 ELSE 0 END) AS prefer_candidate2
                FROM list_of_answers
            """)
            result = cursor.fetchone()

            prefer_candidate1 = result[0] if result[0] is not None else 0
            prefer_candidate2 = result[1] if result[1] is not None else 0

            if prefer_candidate1 <= prefer_candidate2:
                is_condorcet_winner = False
                break

        if is_condorcet_winner:
            return candidate1_name

    return "none"


if __name__ == '__main__':
    party = input()
    if party == "condorcet_winner":
        print(condorcet_winner())
    else:
        candidate1,candidate2 = party.split(",")
        print(net_support_for_candidate1(candidate1,candidate2))

    # print_codes_for_answers_range(582, 645)
    # # print_list_of_answers()
    # print_codes_for_questions()
    # db.close()
    # candidate1, candidate2 = "יאיר לפיד", "בני גנץ"
    # print(net_support_for_candidate1(candidate1,candidate2))

