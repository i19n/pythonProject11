class MyObject:
    int_field=8
    str_field='a string'
print(MyObject.int_field)
print(MyObject.str_field)

object1=MyObject()
object2=MyObject()

print(object1.int_field)
print(object2.str_field)

MyObject.int_field=10
print(MyObject.int_field)
print(object1.int_field)

object1.str_field='anoth str'
print(MyObject.str_field)
print(object1.str_field)
print(object2.str_field)