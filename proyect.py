from random import randint


print("Keling o'ylagan sonni topish o'ynaymiz!\n1 dan 10 gacha son o'yladim. Topa olasizmi?: ")
num = randint(1,10)
cnt = 0
number = int(input())
while number != num:
    if number < num:
        print("Xato men o'ylagan son bundan kattaroq. Yana harakat qiling!")
    else:
        print("Xato men o'ylagan son bundan kichikroq. Yana harakat qiling!")
    cnt += 1
    number = int(input())
cnt += 1
print(f"TOPDINGIZ!!! {num} sonini o'ylagan edim {cnt} ta taxmin bilan topdingiz. Tabriklayman!!!")

print("1 dan 10 gacha son o'ylang. Men topishga harakat qilaman.")
_ = input("Son o'ylagan bo'lsangiz start tugmasini bosing")

cnt1 = 0
num2 = randint(1,10)
ans = input(f"Siz {num2} sonini o'yladingiz: To'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)??")
left = 1
right = 10

while ans != "T" and ans != "t":
    if ans == "+":
        left = num2+1
        num2 = randint(left, right)
    else:
        right = num2-1
        num2 = randint(left, right)
    cnt1 += 1
    ans = input(f"Siz {num2} sonini o'yladingiz: To'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)??")

cnt1 += 1

print(f"Soningizni {cnt1} ta taxmin bilan topdim!!!")
if cnt == cnt1:
    print(f"Durrang ikkimiz ham {cnt} ta taxmin bilan topdik!!")
elif cnt < cnt1:
    print(f"Siz {cnt} ta taxmin bilan topdingiz va yutdingiz!!")
else:
    print(f"Men {cnt1} ta taxmin bilan topdim va yutdim!!!")

