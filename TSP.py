'''旅行商问题（Traveling Salesman Problem,TSP）'''
class Tsp:
    def __init__(self, start):
        self.start = start
    # 用邻接表表示带权图
    n = 5  # 节点数
    a, b, c, d, e = range(n)  # 节点名称
    graph = [
        {b: 7, c: 9, d: 6, e: 10},
        {a: 7, c: 4, d: 1, e: 8},
        {a: 9, b: 4, d: 5, e: 3},
        {a: 6, b: 1, c: 5, e: 3},
        {a: 10, b: 8, c: 11, d: 3}
    ]
    x = [0] * (n + 1)  # 一个解（n+1元数组，长度固定）
    best_path = [0] * (n + 1)  # 已找到的最佳解（路径）
    min_cost = 0  # 最小旅费

    # 冲突检测
    def conflict(self, k):
        # 第k个节点，是否前面已经走过
        if k < self.n and self.x[k] in self.x[:k]:
            return True
        # 回到出发节点
        if k == self.n and self.x[k] != self.x[0]:
            return True
        # 前面部分解的旅费之和超出已经找到的最小总旅费
        cost = sum([self.graph[node1][node2] for node1, node2 in zip(self.x[:k], self.x[1:k + 1])])
        if 0 < self.min_cost < cost:
            return True
        return False  # 无冲突

    # 旅行商问题（TSP）
    def tsp(self, k):  # 到达（解x的）第k个节点
        if k > self.n:  # 解的长度超出，已走遍n+1个节点 （若不回到出发节点，则 k==n）
            cost = sum([self.graph[node1][node2] for node1, node2 in zip(self.x[:-1], self.x[1:])])  # 计算总旅费 x[:-1]除了最后一位的前面的元素 x[1:]除了第一位之后的后面所有元素
            # print([graph[node1][node2] for node1, node2 in zip(x[:-1], x[1:])])
            if self.min_cost == 0 or cost < self.min_cost:
                self.best_path = self.x[:]
                self.min_cost = cost
                # print(x)
        else:
            for node in self.graph[self.x[k - 1]]:  # 遍历节点x[k-1]的邻接节点（状态空间）
                self.x[k] = node
                if not self.conflict(k):  # 剪枝
                    self.tsp(k + 1)
    def run(self):
        self.x[0] = self.start
        self.tsp(1)# 开始处理解x中的第2个节点
        print(self.best_path)
        print(self.min_cost)

if __name__ == "__main__":
    a, b, c, d, e = range(5)  # 节点名称
    tsp = Tsp(b) # 出发节点：路径x的第一个节点（随便哪个）
    tsp.run()