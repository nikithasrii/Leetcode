class Solution:
    def convertDateToBinary(self, date: str) -> str:
        
        year,month,date=map(int,date.split("-"))

        year_bin = bin(year)[2:]
        month_bin=bin(month)[2:]
        day_bin=bin(date)[2:]

        return year_bin + "-" + month_bin + "-" + day_bin

        