def is_isogram(string):
	k=[]
	for i in string:
		if i==" ":
			continue
		if i=="-":
			continue
		if i.lower() in k:
			return False
			break
		k.append(i.lower())
	return True
			


