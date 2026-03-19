

# toList

Returns a List containing all elements.

```kotlin
fun <T> Sequence<T>.toList(): List<T>(source)
```

```kotlin
val numbers = listOf(1, 2, 3).asSequence().toList()
println(numbers)   // Output: [1, 2, 3]
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/to-list.html)

    