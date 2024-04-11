is_male = True
is_tall = True

if is_male and is_tall:
    print("you are a tall man")
elif is_male and not(is_tall):
    print("you are a short man")
elif not (is_male) and is_tall:
    print("you are a tall not man")
else:
    print("you short not man")