

# toMutableSet

Returns a new MutableSet containing all distinct elements from the given array.

```kotlin
fun <T> Array<out T>.toMutableSet(): MutableSet<T>(source)
```

```kotlin
val array = arrayOf("apple", "banana", "apple", "cherry")
val mutableSet = array.toMutableSet()

mutableSet.add("date")          // add a new element
mutableSet.remove("banana")     // remove an element

println(mutableSet)             // prints something like [apple, cherry, date]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-mutable-set.html)

    