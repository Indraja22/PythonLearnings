def tweet_length(tweet):
    length_of_tweet = len(tweet)
    if length_of_tweet > 140:
        print(f"Your {length_of_tweet} tweet is {length_of_tweet - 140} chars too long!")
    else:
        print(f"That {length_of_tweet} char tweet will work!")

tweet_length("Hello World!")
tweet_length("Hello World!I have an announcement to make today.I have joined a new job.")
tweet_length("loqeodncjdcnc  cndckjwcbhwrbhwbhewhbcwhbfwhlcb hefbefhwfbkhfhebfbhwefufb hbchewekcbhcbchwkcchbwj hdjwedvwkcvgcvwcvwcgewcgvcwkegcgcevkqvcvgcvcwkehvckwyyewyeyyfvfywvfeveycwyvcygeygku")