def solve_poison_wine():
    """
    毒酒问题：30 瓶酒中有 1 瓶毒酒，用 5 只老鼠找出毒酒
    核心思想：二进制编码 + 过滤法

    数学基础：
    - 5 只老鼠 → 5 bit 信息 → 最多表示 2^5 = 32 种结果
    - 30 瓶酒 < 32，所以 5 只老鼠足够
    - 每只老鼠代表一个二进制位的"探针"，权重分别为 1, 2, 4, 8, 16
    """
    TOTAL_BOTTLES = 30
    TOTAL_MICE = 5

    # 假设第 18 号酒是毒酒
    actual_poison_bottle = 18
    print(f"【系统设定】{TOTAL_BOTTLES} 瓶酒中有 1 瓶毒酒，编号 = {actual_poison_bottle}")
    print(f"   二进制: {actual_poison_bottle:0{TOTAL_MICE}b}")
    print(f"   因为 {TOTAL_BOTTLES} ≤ 2^{TOTAL_MICE} = {2 ** TOTAL_MICE}，所以 {TOTAL_MICE} 只老鼠足够\n")

    # ============================================================
    # 第一阶段：分配试酒方案 —— 每只老鼠喝哪些瓶酒
    # ============================================================
    print("=" * 60)
    print("【第一阶段】分配试酒方案")
    print("=" * 60)
    print(f"原理：编号第 i 位为 1 的酒 → 由第 (i+1) 只老鼠喝")
    print(f"本质：{TOTAL_MICE} 只老鼠 = {TOTAL_MICE} 个二进制位的'探针'")
    bit_weights = [f"鼠{i+1}=2^{i}={2**i}" for i in range(TOTAL_MICE)]
    print(f"位权表: {', '.join(bit_weights)}\n")

    # mouse_drinks[i] 存储第 i 只老鼠需要喝的所有酒瓶编号
    mouse_drinks = [[] for _ in range(TOTAL_MICE)]

    for bottle in range(1, TOTAL_BOTTLES + 1):
        for mouse_idx in range(TOTAL_MICE):
            # 如果瓶子编号的第 mouse_idx 位是 1，则该老鼠喝这瓶酒
            if (bottle >> mouse_idx) & 1:
                mouse_drinks[mouse_idx].append(bottle)

    # 输出每只老鼠喝的酒瓶列表
    for mouse_idx in range(TOTAL_MICE):
        drinks = mouse_drinks[mouse_idx]
        drink_list = ", ".join(str(x) for x in drinks)
        print(
            f"🐭 老鼠 {mouse_idx + 1} (第 {mouse_idx} 位, 权重 2^{mouse_idx}={2 ** mouse_idx}): "
            f"共喝 {len(drinks):2d} 瓶 → [{drink_list}]"
        )

    # ============================================================
    # 第二阶段：实验过程 —— 24 小时后观察老鼠死亡
    # ============================================================
    print("\n" + "=" * 60)
    print("【第二阶段】实验观察 (24 小时后)")
    print("=" * 60)

    # 找出实际死亡的老鼠
    dead_mice = []
    for mouse_idx in range(TOTAL_MICE):
        if (actual_poison_bottle >> mouse_idx) & 1:
            dead_mice.append(mouse_idx)

    print(f"死亡的老鼠编号: {[m + 1 for m in dead_mice]}")
    print(f"说明: 第 {', '.join(str(m + 1) for m in dead_mice)} 只老鼠喝的酒中包含第 {actual_poison_bottle} 号酒\n")

    # ============================================================
    # 第三阶段：过滤法反推 —— 每死一只老鼠缩小嫌疑范围
    # ============================================================
    print("=" * 60)
    print("【第三阶段】根据死亡情况过滤嫌疑酒")
    print("=" * 60)
    print(f"初始嫌疑范围: 1 ~ {TOTAL_BOTTLES} 共 {TOTAL_BOTTLES} 瓶酒\n")

    # 嫌疑酒瓶集合（每死一只老鼠就过滤一次）
    suspects = set(range(1, TOTAL_BOTTLES + 1))

    # 逐只处理死亡的老鼠
    for step, mouse_idx in enumerate(dead_mice, 1):
        print(f"── 第 {step} 步：老鼠 {mouse_idx + 1} 死亡 ──")
        print(f"   含义: 毒酒一定在老鼠 {mouse_idx + 1} 喝过的酒中")
        print(f"   老鼠 {mouse_idx + 1} 喝的酒: {len(mouse_drinks[mouse_idx])} 瓶")

        # 过滤：毒酒必须在死亡老鼠喝过的酒中
        before_count = len(suspects)
        suspects &= set(mouse_drinks[mouse_idx])
        after_count = len(suspects)

        eliminated = before_count - after_count
        print(f"   过滤前嫌疑: {before_count} 瓶 → 过滤后: {after_count} 瓶 (排除 {eliminated} 瓶)")
        print(f"   ✅ 嫌疑范围缩小了 {eliminated / before_count * 100:.1f}%\n")

    print(f"🎯 最终嫌疑范围: {sorted(suspects)}")
    print(f"🎯 嫌疑瓶数: {len(suspects)} 瓶\n")

    # ============================================================
    # 第四阶段：二进制解码
    # ============================================================
    print("=" * 60)
    print("【第四阶段】二进制解码")
    print("=" * 60)

    calculated_poison_bottle = 0
    for mouse_idx in dead_mice:
        calculated_poison_bottle += (1 << mouse_idx)
        print(f"  累加 2^{mouse_idx} = {2 ** mouse_idx:3d} (来自老鼠 {mouse_idx + 1})")

    print(f"\n  二进制结果: {calculated_poison_bottle:0{TOTAL_MICE}b}")
    print(f"  十进制结果: 第 {calculated_poison_bottle} 号酒")

    # ============================================================
    # 验证
    # ============================================================
    print("\n" + "=" * 60)
    print("【验证】")
    print("=" * 60)
    if calculated_poison_bottle == actual_poison_bottle:
        print(f"✅ 测试成功：推算的 {calculated_poison_bottle} 号 = 实际的 {actual_poison_bottle} 号")
        print("🎉 程序完美找出了毒酒！")
    else:
        print(f"❌ 测试失败：推算 {calculated_poison_bottle} ≠ 实际 {actual_poison_bottle}")


if __name__ == "__main__":
    solve_poison_wine()
