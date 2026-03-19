

# toMutableList

Returns a new MutableList filled with all elements of this array.

```kotlin
fun <T> Array<out T>.toMutableList(): MutableList<T>(source)
```

```kotlin
val array = arrayOf("apple", "banana", "cherry")

// Convert the array to a mutable list
val mutableList: MutableList<String> = array.toMutableList()

// Modify the list
mutableList.add("date")
mutableList.removeAt(0)

println(mutableList) // prints [banana, cherry, date]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-mutable-list.html)

    