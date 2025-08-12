
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if not isinstance(skus, str): 
            return -1

        prices = {"A" : 50, "B" : 30, "C" : 20, "D" :15}
        offers = {"A" : (3,130), "B" : (2, 45)}

        counts = {}
        for item in skus:
            if item not in prices:
                return -1
            counts[item] = 1 + counts.get(item, 0)
        

        checkoutTotal = 0

        for sku, itemQuantity in counts.items():
            if sku in offers:
                offerQuantity, offerPrice = offers[sku]
                numOfferApplied = itemQuantity // offerQuantity
                quantityRem = 

            else:
                checkoutTotal += prices[sku] * quantity


        





