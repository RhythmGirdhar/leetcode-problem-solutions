class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for passenger in details:
            passenger_age = passenger[11:13]
            if int(passenger_age) > 60:
                count += 1
        return count