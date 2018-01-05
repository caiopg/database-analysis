import dbquery


def print_views(results):
    answer_template = "{0} - {1} views"

    print("\n")
    for result in results:
        result_1, result_2 = result
        print(answer_template.format(result_1, result_2))
    print("\n")


def print_fail_percentage(results):
    answer_template = "{0} - {1}% errors"

    print("\n")
    for result in results:
        result_1, result_2 = result
        print(answer_template.format(result_1.strftime('%B %d, %Y'),
                                     result_2, "views"))
    print("\n")


instructions = "Press 1 to view the 3 most popular articles of all time.\n" \
               "Press 2 to view the most popular authors of all time.\n" \
               "Press 3 to view days where more than 1% of requests failed.\n" \
               "Press 0 to exit program.\n" \
               "\n" \
               "Press enter after option selected.\n"

while True:
    option = input(instructions)

    if not option.isdigit() or int(option) < 0 or int(option) > 3:
        print("Please select a valid option\n")
        continue

    if option == '0':
        print("\nBye!\n")
        break

    if option == '1':
        response = dbquery.top_three_articles()
        print_views(response)

    if option == '2':
        response = dbquery.top_authors()
        print_views(response)

    if option == '3':
        response = dbquery.more_one_percent_requests_failed()
        print_fail_percentage(response)
