

# toMutableSet

Returns a new MutableSet containing all distinct elements from the given sequence.

```kotlin
fun <T> Sequence<T>.toMutableSet(): MutableSet<T>(source)
```

```kotlin
fun main() {
    val numbers = sequenceOf(1, 2, 3, 2, 4)
    val mutableSet = numbers.toMutableSet()   // {1, 2, 3, 4}
    
    mutableSet.add(5)                         // add another element
    println(mutableSet)                       // prints: [1, 2, 3, 4, 5]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/to-mutable-set.html)

    