

# plusElement

Returns a list containing all elements of the original collection and then the given element.

```kotlin
inline fun <T> Iterable<T>.plusElement(element: T): List<T>(source)
```

```kotlin
val numbers = listOf(1, 2, 3)
val extended = numbers.plusElement(4)

println(extended) // Output: [1, 2, 3, 4]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/plus-element.html)

    