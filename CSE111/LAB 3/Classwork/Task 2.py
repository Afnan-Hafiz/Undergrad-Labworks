class MangoTree:
    def __init__(self,v,height=1,n=0):
        self.variety=v
        self.height=height
        self.number_of_mangoes=n

#DRIVER CODE STARTS
mangoTree1= MangoTree("Gopalbhog")
# Display the details of the mango tree
print("=====================================")
print("Mango Tree Details:")
print(f"Variety: {mangoTree1.variety}")
print(f"Height: {mangoTree1.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree1.number_of_mangoes}")
print("=====================================")

mangoTree2= MangoTree("Amrapali")
# Display the details of the mango tree
print("Mango Tree Details:")
print(f"Variety: {mangoTree2.variety}")
print(f"Height: {mangoTree2.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree2.number_of_mangoes}")
print("=====================================")
#DRIVER CODE ENDS


mangoTree1.height+=(5*3)
mangoTree1.number_of_mangoes+=((mangoTree1.height)*10)

mangoTree2.height+=(5*3)
mangoTree2.number_of_mangoes+=((mangoTree2.height)*15)

#DRIVER CODE AFTER 5 YEARS STARTS//////////////////////////////////////////

#Display the details of the mango tree
print("Updated details after 5 years")
print("=====================================")
print(f"Variety: {mangoTree1.variety}")
print(f"Height: {mangoTree1.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree1.number_of_mangoes}")
print("=====================================")

# # Display the details of the mango tree
print(f"Variety: {mangoTree2.variety}")
print(f"Height: {mangoTree2.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree2.number_of_mangoes}")
print("=====================================")

#DRIVER CODE AFTER 5 YEARS ENDS////////////////////////////////////////