def remove(s):
    return s[:-1] if s.endswith("!") else s


# Code to rome all ending exclamation marks
 
# def remove(s):
#     for i in range(len(s)):
#         if s[::-1][i] == "!":
#             continue
#         else:
#             return s[:-i]
            