

# plus

Returns a list containing all elements of the original collection and then the given element.

```kotlin
operator fun <T> Iterable<T>.plus(element: T): List<T>(source)
```

```kotlin
fun main() {
    val numbers = listOf(1, 2, 3)
    val extended = numbers + 4
    println(extended)  // Output: [1, 2, 3, 4]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/plus.html)

    