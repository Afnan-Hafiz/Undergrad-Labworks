class Foodie:
    def __init__(self,n):
        global menu
        self.menu=menu
        self.name=n
        self.total_spent=0
        self.n_items=0
        self.items=[]
    def show_orders(self):
       return f'{self.name} has {self.n_items} item(s) in the cart.\nItems: {self.items}\nTotal spent: {self.total_spent}.'



    def order(self,*ordr):
        l1=[]
        l2=''
        l3=''
        price=0
        sum=0
        self.n_items+=len(ordr)
        for i in ordr:
            l1=i.split('-')
            l2=l1[0]
            self.items.append(l1[0])
            l3=int(l1[1])
            for key in self.menu:
                if key==l2:
                    price=self.menu[key]
            print(f'Ordered - {l2}, quantity - {l3},price (per unit) - {price}.')
            sum= l3*price
            self.total_spent+=sum
            print(f'Total price - {sum}')

    def pay_tips(self,a=None):
        if a!=None:
            print(f'Gives {a}/- tips to the waiter.')
            self.total_spent+=a
        else:
            print('No tips to the waiter.')


#DRIVER CODE
menu = {'Chicken Lollipop':15,'Beef Nugget':20,'Americano':180,'Red Velvet':150,'Prawn Tempura':80,'Saute Veg':200}
f1 = Foodie('Frodo')
print(f1.show_orders())
print('1----------------------')
f1.order('Chicken Lollipop-3','Beef Nugget-6','Americano-1')
print('2----------------------')
print(f1.show_orders())
print('3----------------------')
f1.order('Red Velvet-1')
print('4----------------------')
f1.pay_tips(20)
print('5----------------------')
print(f1.show_orders())
f2 = Foodie('Bilbo')
print('6----------------------')
f2.order('Prawn Tempura-6','Saute Veg-1')
print('7----------------------')
f2.pay_tips()
print('8----------------------')
print(f2.show_orders())