

# toMutableList

Returns a new MutableList filled with all elements of this sequence.

```kotlin
fun <T> Sequence<T>.toMutableList(): MutableList<T>(source)
```

```kotlin
fun main() {
    val sequence = sequenceOf(10, 20, 30, 40, 50)
    val mutableList = sequence.toMutableList()   // converts the sequence to a MutableList
    mutableList.add(60)                         // modify the list
    println(mutableList)                        // prints: [10, 20, 30, 40, 50, 60]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/to-mutable-list.html)

    