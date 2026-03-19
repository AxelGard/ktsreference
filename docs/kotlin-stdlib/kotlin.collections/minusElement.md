

# minusElement

Returns a list containing all elements of the original collection without the first occurrence of the given element.

```kotlin
inline fun <T> Iterable<T>.minusElement(element: T): List<T>(source)
```

```kotlin
val numbers = listOf(1, 2, 3, 2, 4)
val withoutFirstTwo = numbers.minusElement(2)   // removes the first 2
println(withoutFirstTwo)   // [1, 3, 2, 4]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/minus-element.html)

    