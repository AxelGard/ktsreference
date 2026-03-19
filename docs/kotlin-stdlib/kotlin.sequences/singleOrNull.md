

# singleOrNull

Returns single element, or null if the sequence is empty or has more than one element.

```kotlin
fun <T> Sequence<T>.singleOrNull(): T?(source)
```

```kotlin
fun main() {
    val singleValue   = sequenceOf("only").singleOrNull()      // → "only"
    val emptySequence = emptySequence<Int>().singleOrNull()    // → null
    val manyValues    = sequenceOf(1, 2).singleOrNull()        // → null

    println(singleValue)   // prints: only
    println(emptySequence) // prints: null
    println(manyValues)    // prints: null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/single-or-null.html)

    