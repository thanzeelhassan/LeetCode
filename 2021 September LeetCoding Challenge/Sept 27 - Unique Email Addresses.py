class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        l = set()
        for item in emails:
            name , domain = item.split("@")
            if "+" in name:
                name , _ = name.split("+", 1)
            name = name.replace(".", "")
            l.add(name + "@" + domain)
        return len(l)
