

# groupingBy

Creates a Grouping source from a sequence to be used later with one of group-and-fold operations using the specified keySelector function to extract a key from each element.

```kotlin
inline fun <T, K> Sequence<T>.groupingBy(crossinline keySelector: (T) -> K): Grouping<T, K>(source)
```

```kotlin
val fruits = sequenceOf("apple", "apricot", "banana", "avocado")
val counts = fruits.groupingBy { it.first() }.eachCount()
println(counts)  // {a=3, b=1}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/grouping-by.html)

    