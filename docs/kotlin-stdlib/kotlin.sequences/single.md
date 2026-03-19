

# single

Returns the single element, or throws an exception if the sequence is empty or has more than one element.

```kotlin
fun <T> Sequence<T>.single(): T(source)
```

```kotlin
fun main() {
    val singleElementSeq = sequenceOf(10)
    println(singleElementSeq.single()) // prints 10
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/single.html)

    