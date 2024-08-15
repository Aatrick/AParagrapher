def paragrapher(file):
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()

    text_list = list(text)
    char_count = 0
    min_size_limit = 50  # Define the minimum size limit
    max_size_limit = 300  # Define the maximum size limit

    for i in range(len(text_list)):
        char_count += 1

        # Handle dialogues
        if (
            text_list[i] == '"'
            and i + 2 < len(text_list)
            and text_list[i + 1] == " "
            and text_list[i + 2] == '"'
        ):
            text_list[i + 1] = "\n\n"
            char_count = 0
        if (
            text_list[i] == '"'
            and i + 2 < len(text_list)
            and text_list[i + 1] == " "
            and text_list[i + 2].isupper()
        ):
            text_list[i + 1] = "\n\n"
            char_count = 0
        if text_list[i] == '"' and i + 1 < len(text_list) and text_list[i + 1] == ",":
            text_list[i + 2] = "\n\n"
            char_count = 0
        if (
            text_list[i] == "."
            and i + 2 < len(text_list)
            and text_list[i + 1] == " "
            and text_list[i + 2] == '"'
        ):
            text_list[i + 1] = "\n\n"
            char_count = 0
        # if (
        #     text_list[i] == ","
        #     and i + 2 < len(text_list)
        #     and text_list[i + 1] == " "
        #     and text_list[i + 2] == '"'
        # ):
        #     text_list[i + 1] = "\n\n"
        #     char_count = 0
        # if text_list[i] == "　":
        #     text_list[i] = "\n\n"
        #     char_count = 0

        # Handle character count conditions
        if char_count < min_size_limit and text_list[i] == ".":
            if i + 1 < len(text_list) and text_list[i + 1] == '"':
                text_list[i + 2] = "\n\n"
                char_count = 0
        if (
            char_count > max_size_limit
            and text_list[i] == "."
            and i + 1 < len(text_list)
        ):
            if (
                text_list[i + 1] == "."
                and text_list[i + 2] == "."
                and i + 2 < len(text_list)
            ):
                if text_list[i + 3] == '"' and i + 4 < len(text_list):
                    text_list[i + 4] = "\n\n"
                    char_count = 0
                else:
                    text_list[i + 3] = "\n\n"
                    char_count = 0

            # if in the next 50 characters there is a '."' then add a /n/n after the '."' and reset the char_count else add a /n after the '.'
            elif i + 50 < len(text_list):
                for j in range(50):
                    if text_list[i + j] == "." and text_list[i + j + 1] == '"':
                        text_list[i + j + 2] = "\n\n"
                        char_count = 0
                        break
                else:
                    text_list[i + 1] = "\n\n"
                    char_count = 0
            else:
                text_list[i + 1] = "\n\n"
                char_count = 0

    output_text = "".join(text_list)

    with open("ATE1.txt", "w", encoding="utf-8") as output:
        output.write(output_text)
    print("success")


paragrapher(".//Vol1-en.txt")
