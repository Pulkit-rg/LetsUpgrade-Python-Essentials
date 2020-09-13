#Make a Lambda function for capitalizing the whole sentence passed using arguments.
#And map all the sentences in the List, with the lambda functions
#[“hey this is sai”,I am in mumbai”,....]
#o/p- [“Hey This Is Sai”, I Am In Mumbai”,....]

dav= ["hello everyone, how are you all?"]

nav=map(lambda nav : nav.title(), dav)
print(list(nav))
