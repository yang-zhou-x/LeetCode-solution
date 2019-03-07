class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        pre=[]
        post=[]
        for e in emails:
            aux=e.split('@')
            pre.append(aux[0].replace('.','').split('+')[0])
            post.append(aux[1])
        return len(set(p1+'@'+p2 for p1,p2 in zip(pre,post)))
