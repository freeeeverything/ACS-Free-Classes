from bs4 import BeautifulSoup
x = 1
class_list = {}
r = input("how many classes do you have: ")
r = int(r) + 1
for x in range(1, r):
    class_list[x] = open(
        f"E:\\ACS-Free-Classes\\python-automation\\fsfd\\{x}.html", "r", encoding="utf8")
    index = class_list[x].read()
    soup = BeautifulSoup(index, 'html.parser')
    scr = soup.find_all("script")[-1].
    hi = scr
    print(hi)
    # class_list[x].write(scr)
    # class_list[x].close()


# html = open(r"E:\\ACS-Free-Classes\\python-automation\\hm7.html",
#             "r", encoding="utf8")
# index = html.read()
# soup = BeautifulSoup(index, 'html.parser')

# img = soup.find_all("img")
