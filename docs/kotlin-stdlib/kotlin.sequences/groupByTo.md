

# groupByTo

Groups elements of the original sequence by the key returned by the given keySelector function applied to each element and puts to the destination map each group key associated with a list of corresponding elements.

```kotlin
@IgnorableReturnValueinline fun <T, K, M : MutableMap<in K, MutableList<T>>> Sequence<T>.groupByTo(destination: M, keySelector: (T) -> K): M(source)
```

```kotlin
val numbers = listOf(1, 2, 3, 4, 5, 6).asSequence()

val groupedByEven = mutableMapOf<Boolean, MutableList<Int>>()
numbers.groupByTo(groupedByEven) { it % 2 == 0 }

println(groupedByEven)  // {false=[1, 3, 5], true=[2, 4, 6]}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/group-by-to.html)

    