s = ['short', 'medium', 'loooooooooooooooooooooo', 'loooooooooooooooooooong', 'long']
print([word for word in s if len(word) == max([len(w) for w in s])])
