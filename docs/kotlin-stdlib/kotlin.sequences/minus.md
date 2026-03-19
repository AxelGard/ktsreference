

# minus

Returns a sequence containing all elements of the original sequence without the first occurrence of the given element.

```kotlin
operator fun <T> Sequence<T>.minus(element: T): Sequence<T>(source)
```

```kotlin
val numbers = sequenceOf(1, 2, 3, 2, 4)
val result = numbers - 2          // removes the first 2
println(result.toList())          // prints [1, 3, 2, 4]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/minus.html)

    