

# groupByTo

Groups elements of the original array by the key returned by the given keySelector function applied to each element and puts to the destination map each group key associated with a list of corresponding elements.

```kotlin
@IgnorableReturnValueinline fun <T, K, M : MutableMap<in K, MutableList<T>>> Array<out T>.groupByTo(destination: M, keySelector: (T) -> K): M(source)
```

```kotlin
val fruits = arrayOf("apple", "apricot", "banana", "blueberry", "cherry")
val groups = mutableMapOf<Char, MutableList<String>>()

fruits.groupByTo(groups) { it.first() }

println(groups) // {a=[apple, apricot], b=[banana, blueberry], c=[cherry]}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/group-by-to.html)

    