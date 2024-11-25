names = ["Ankush", "Gauro"]
letters = [6,5]

zipped_list = zip(names, letters)
print(list(zipped_list))


#to unzip the tuple

znames, letters = zip(*zipped_list)
print(list(znames))