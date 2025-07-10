def main(n):
    if n > 100:
        print("vous dépasez la plage autoriser")
    else:
        lst = []
        for i in range(n):
            if i % 3 == 0:
                lst.append("Fizz")
            elif i % 5 == 0:
                lst.append("Buzz")
            else:
                lst.append(i)
        return lst


if __name__ == "__main__":
    n = int(input("Entrez votre nombre : "))
    print(f"votre série est la suivant : {main(n)}")
