if len(fruits) > 1:
            beg = 0
            end = 0
            types = [fruits[0]]
            basket_1 = 0
            basket_2 = 0
            max_sum = 0
            while beg < len(fruits) and end < len(fruits):
                if len(types) < 2 and fruits[end] != types[0]:
                    types.append(fruits[end])
                elif fruits[end] == types[0]:
                    basket_1 += 1
                    end += 1
                elif fruits[end] == types[1]:
                    basket_2 += 1
                    end += 1
                else:
                    beg += 1
                    if end - beg > 1:
                        beg = end
                        while fruits[beg-1] == fruits[end-1]:
                            beg -= 1
                        basket_1 = 0
                        basket_2 = 0
                        types = [fruits[beg]]
                        end = beg
                    else:
                        types.pop(0)
                        basket_1 = basket_2
                        basket_2 = 0
                max_sum = max(max_sum, basket_1+basket_2)

            return max_sum
        else:
            return 1
