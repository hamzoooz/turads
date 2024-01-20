from django.conf import settings
from core.models import Item

class Cart(object):
    def __init__(self , request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        for b in self.cart.keys():
            self.cart[str(b)]['book'] = Item.objects.get(pk=b)        
        for item in self.cart.values():
            item['total_price'] = int(item['book'].selling_price * item['quantity']) / 100
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values() )
    
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, book_id, quantity=1, update_quantity=False):
        book_id = book_id    
        if book_id not in self.cart:
            self.cart[book_id] = {'quantity':int(quantity), 'id':book_id}
        if update_quantity :
            self.cart[book_id]['quantity'] += int(quantity)
            if self.cart[book_id]['quantity'] == 0:
                self.remove(book_id)    
        self.save()

    def total_cost(self):
        for b in self.cart.keys():
            self.cart[str(b)] = Item.objects.get(pk=b)
        return int(sum(item['book'].selling_price * item['quantity'] for item in self.cart.values() )) / 100 

    def remove(self, book_id):
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()
    # def clear(self):
    #     del self.session[settings.CART_SESSION_ID]
    #     self.session.modified = True
    