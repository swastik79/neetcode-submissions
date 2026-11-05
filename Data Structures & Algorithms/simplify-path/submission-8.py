class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        res = []

        for p in path:
            if p == '..' and res:
                res.pop()
            elif p not in ('/', '', '.', '..'):
                res.append(p)
        
        return '/' + '/'.join(res)