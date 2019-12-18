class KthSymbolInGrammar:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1 and K == 1:
            return 0
        if N == 2 and K == 1:
            return 0
        if N == 2 and K == 2:
            return 1
        else:
            previous = self.kthGrammar(N - 1, (K + 1) // 2)
            if previous == 0:
                if K % 2 == 0:
                    return 1
                else:
                    return 0
            elif previous == 1:
                if K % 2 == 0:
                    return 0
                else:
                    return 1


if __name__ == "__main__":
    # 0
    # 01
    # 0110
    # 01101001
    assert 1 == KthSymbolInGrammar().kthGrammar(4, 5)
