# Mencari bilangan terbesar dan terkcil dalam tipe data list
nums = list(map(int, input("Masukan Array: ").split()))
terbesar = nums[0]
terkecil = nums[0]
for i in range(len(nums)):
    if terbesar < nums[i]:
        terbesar = nums [i]
    elif terkecil > nums[i]:
        terkecil = nums[i]
print(terbesar, terkecil)
