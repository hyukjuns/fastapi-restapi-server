from pydantic import BaseModel

class Test(BaseModel):
    id: int 
    name: str
    foo: bool | None = None

test_list = []

arg1 = Test(id=1,name="one", foo=True)
arg2 = Test(id=2,name="two", foo=False)
arg3 = Test(id=3,name="three", foo=True)
test_list.append(arg1)
test_list.append(arg2)
test_list.append(arg3)

print(test_list)
for i in test_list:
    print(i)
