class Solution:
    def totalMoney(self, n: int) -> int:
        count = 1
        money = 0
        start_money = 1
        week_count = 1
        while(n > 0):
            money = money + start_money
            if count % 7 == 0 :
                start_money = week_count + 1
                week_count = week_count + 1
            else :
                start_money = start_money + 1
            n = n - 1
            count = count + 1
        return money