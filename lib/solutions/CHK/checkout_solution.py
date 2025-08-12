
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if not isinstance(skus, str): 
            return -1

        prices = {"A" : 50, "B" : 30, "C" : 20, "D" :15, "E": 40, "F" : 10, "G" : 20, "H" : 10, : "I": 35, : "J" : 60, "K" : 80,
                 "L" : 90, "M" : 15, "N" : 40, "O" : 10, "P" : 50, "Q" : 30, "R" : 50, "S" : 30, "T" : 20, "U" : 40, "V" : 50, "W" : 20, 
                 "X" : 90, "Y" : 10, "Z" : 50}

        multiPriceOffers = {"A" : [(5, 200), (3, 130)],
                            "B" : [(2,45)],
                            "H" : [(10, 80), (5, 45)],
                            "K" : [(2, 150)],
                            "P" : [(5, 200)],
                            "Q" : [(3, 80)],
                            "V" : [(3, 130), (2, 90)]}
     #   "BuyThisItem" : (QuantityToBuy, getThisItemFree)
        freeItemOffers = {"E" : (2, "B"),
                          "F" : (3, "F"),
                          "N" : 3, "M",
                          ""}

        counts = {}
        for item in skus:
            if item not in prices:
                return -1
            counts[item] = 1 + counts.get(item, 0)
        
        def cnt(item): return counts.get(item, 0)


        

        checkoutTotal = 0

        #assuming 2 Es only makes the Bs in the basket free here
        freeB = min(cnt("B"), cnt("E")//2)
        chargeableB = cnt("B") - freeB

        quantityA = cnt("A")
        totalA = 0
        if quantityA > 0:
            numA5Bundles = quantityA // 5
            quantityA -= numA5Bundles * 5
            totalA += numA5Bundles * 200

            numA3Bundles = quantityA // 3
            quantityA -= numA3Bundles * 3
            totalA += numA3Bundles * 130

            totalA += quantityA * prices["A"]
        
        checkoutTotal += totalA

        quantityB = chargeableB
        totalB = 0
        if quantityB > 0:
            numB2Bundles = quantityB // 2
            quantityB -= numB2Bundles * 2 
            totalB += numB2Bundles * 45

            totalB += quantityB * prices["B"]
        
        checkoutTotal+= totalB

        checkoutTotal += cnt("C") * prices["C"]
        checkoutTotal += cnt("D") * prices["D"]
        checkoutTotal += cnt("E") * prices["E"]


        quantityF = cnt("F")
        totalF = 0
        if quantityF > 0:
            chargeableF = quantityF - (quantityF // 3)
            totalF += chargeableF * prices["F"]
        
        checkoutTotal += totalF
        
        return checkoutTotal






        







