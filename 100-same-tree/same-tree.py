class Solution(object):
    def isSameTree(self, p, q):

        # agar dono null hain
        if not p and not q:
            return True

        # agar ek null hai aur dusra nahi
        if not p or not q:
            return False

        # agar values different hain
        if p.val != q.val:
            return False

        # left aur right subtree check karo
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)