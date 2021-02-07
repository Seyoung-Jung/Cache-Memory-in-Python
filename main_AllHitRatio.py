from memory import Memory
from cpu import Cpu
import random
import matplotlib.pyplot as plt

hdd = Memory('HDD', 5000, 3.)
hdd.data_init()
# 캐시 메모리가 l1만 있을 때 -> l1의 lower_memory = ram
ram = Memory('RAM', 1000, 1., hdd)
# l3 = Memory('L3', 200, 0.1, ram)
# l2 = Memory('L2', 20, 0.1, l3)
# l1= Memory('L1', 5, 0.1, l2)
l1 = Memory('L1', 5, 0.1, ram)

cpu = Cpu(l1)
hitRatio1 = [] # l1만 있을 때 히트율 저장하는 리스트
for i in range(1000):
    v1 = random.randint(1, 1000)
    v2 = random.randint(1, 1000)
    print(v1, v2)
    print(cpu.plus(v1, v2))
    print("Hit =", Memory.hit)
    hitRatio1.append(Memory.hit/Memory.total_hit)
print('Memory access time of L1, ram, hdd =', round(Memory.total_time,2))

# 캐시 메모리가 l1, l2, l3 3개일 때 -> 각각의 lower_memory는 순차적으로 내려감
# 메모리의 상황이 달라졌기 때문에 다시 초기화한다.
ram = Memory('RAM', 1000, 1., hdd)
l3 = Memory('L3', 200, 0.1, ram)
l2 = Memory('L2', 20, 0.1, l3)
l1 = Memory('L1', 5, 0.1, l2)

cpu = Cpu(l1)
hitRatio2 = [] # l1, l2, l3 있을 때 히트율 저장하는 리스트
for i in range(1000):
    v1 = random.randint(1, 1000)
    v2 = random.randint(1, 1000)
    print(v1, v2)
    print(cpu.plus(v1, v2))
    print("Hit =", Memory.hit)
    hitRatio2.append(Memory.hit/Memory.total_hit)
print('Memory access time of L1, L2, L3, ram, hdd =', round(Memory.total_time,2))

missRatio1 = []
for i in hitRatio1:
    missRatio1.append(1-i)

missRatio2 = []
for i in hitRatio2:
    missRatio2.append(1-i)

plt.plot(hitRatio1, color='red')
plt.plot(hitRatio2, color='blue')
plt.title('Comparing HitRatio')
plt.show()

plt.plot(missRatio1, color='red')
plt.plot(missRatio2, color='blue')
plt.title('Comparing missRatio')
plt.show()
