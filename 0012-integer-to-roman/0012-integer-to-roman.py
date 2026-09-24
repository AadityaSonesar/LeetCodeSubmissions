class Solution:
    def intToRoman(self, num: int) -> str:
        ones={
            "0":"",
            "1":"I",
            "2":"II",
            "3":"III",
            "4":"IV",
            "5":"V",
            "6":"VI",
            "7":"VII",
            "8":"VIII",
            "9":"IX"
        }
        tens={
            "0":"",
            "1":"X",
            "2":"XX",
            "3":"XXX",
            "4":"XL",
            "5":"L",
            "6":"LX",
            "7":"LXX",
            "8":"LXXX",
            "9":"XC"
        }
        hundreads={
            "0":"",
            "1":"C",
            "2":"CC",
            "3":"CCC",
            "4":"CD",
            "5":"D",
            "6":"DC",
            "7":"DCC",
            "8":"DCCC",
            "9":"CM"
        }
        thousands={
            "0":"",
            "1":"M",
            "2":"MM",
            "3":"MMM"
        }
        num=str(num)
        roman=""
        for i in range(len(num)):
            if len(num)-i==4:
                roman+= thousands[num[i]]
            if len(num)-i==3:
                roman+= hundreads[num[i]]
            if len(num)-i==2:
                roman+= tens[num[i]]
            if len(num)-i==1:
                roman+= ones[num[i]]

        return roman