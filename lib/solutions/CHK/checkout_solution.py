
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if not isinstance(skus, str): 
            return -1

        prices = {"A" : 50, "B" : 30, "C" : 20, "D" :15, "E": 40, "F" : 10, "G" : 20, "H" : 10, "I": 35, "J" : 60, "K" : 70,
                 "L" : 90, "M" : 15, "N" : 40, "O" : 10, "P" : 50, "Q" : 30, "R" : 50, "S" : 20, "T" : 20, "U" : 40, "V" : 50, "W" : 20, 
                 "X" : 17, "Y" : 10, "Z" : 21}

        multiPriceOffers = {"A" : [(5, 200), (3, 130)],
                            "B" : [(2,45)],
                            "H" : [(10, 80), (5, 45)],
                            "K" : [(2, 120)],
                            "P" : [(5, 200)],
                            "Q" : [(3, 80)],
                            "V" : [(3, 130), (2, 90)]}
     #   "BuyThisItem" : (QuantityToTrigger, getThisItemFree)
        freeItemOffers = {"E" : (2, "B"),
                          "F" : (3, "F"),
                          "N" : (3, "M"),
                          "R" : (3, "Q"),
                          "U" : (4, "U") }

        counts = {}
        for item in skus:
            if item not in prices:
                return -1
            counts[item] = 1 + counts.get(item, 0)
        
        def cnt(item): return counts.get(item, 0)

        for item, (itemQuantityToTrigger, freeItem) in freeItemOffers.items():
            itemQuantityToBuy = cnt(item)
            freeItemCount = itemQuantityToBuy // itemQuantityToTrigger
            if freeItem in counts:
                counts[freeItem] = max(0, counts[freeItem] - freeItemCount)

        
        checkoutTotal = 0
        #Group logic here
        def getPrice(item): return prices[item]
        



        for item, quantityItem in counts.items():
            if quantityItem <= 0:
                continue

            if item in multiPriceOffers:
                for bundleQuantity, bundlePrice in multiPriceOffers[item]:
                    numBundles = quantityItem // bundleQuantity
                    quantityItem -= numBundles * bundleQuantity
                    checkoutTotal += numBundles * bundlePrice

            checkoutTotal += quantityItem * prices[item] 
        
        return checkoutTotal






        


