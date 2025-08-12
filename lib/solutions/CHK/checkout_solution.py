
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if not isinstance(skus, str): 
            return -1

        prices = {"A" : 50, "B" : 30, "C" : 20, "D" :15, "E": 40}

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
            quantityA -= numA5Bundles * 3
            totalA += numA5Bundles * 130

            totalA += quantityA * prices["A"]
        
        checkoutTotal += totalA

        quantityB = chargeableB
        totalB = 0
        if quantityB > 0:
            numB2Bundles = quantityB // 2
            quantityB -= numB2Bundles * 2 
            totalB += numB2Bundles 







        






